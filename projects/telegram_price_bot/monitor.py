import csv
import sqlite3
import logging
import requests
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup as BS

BASE_URL = "https://books.toscrape.com/"

Path("logs").mkdir(exist_ok=True)

time_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(filename="logs/parser.log", level=logging.INFO, encoding="utf-8",
                    format="[%(asctime)s] - %(levelname)s: %(message)s", datefmt=time_format)


def download_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.text

        else:
            logging.warning(f"Page was not downloaded: {url}, status code: {response.status_code}")

            return False

    except requests.RequestException as error:
        logging.error(f"Request error: {error}")
        print(f"Request error: {error}")

        return False


def get_text_or_empty(element):
    if not element:
        return ""

    result = element.get_text(strip=True)

    return result


def get_attr_or_empty(element, attr):
    if not element:
        return ""

    if not attr:
        return ""

    result = element.get(attr)

    return result


def clean_price(price):
    price = price.replace("Â", "")
    price = price.replace("£", "")
    price = price.strip()

    return price


def parse_categories(html_text):
    soup = BS(html_text, "html.parser")
    category_links = soup.select(".side_categories ul.nav-list > li > ul > li > a")
    categories = []

    for link in category_links:
        category_name = get_text_or_empty(link)
        category_name = category_name.lower()

        category_link = get_attr_or_empty(link, "href")
        category_link = urljoin(BASE_URL, category_link)

        category_dict = {
            "name": category_name,
            "link": category_link
        }

        categories.append(category_dict)

    if not categories:
        return []

    return categories


def find_category_link(categories, category_name):
    category_name = category_name.lower()

    for category in categories:
        if category["name"] == category_name:
            return category["link"]

    return None


def parse_products(html_text, category_name, page_url):
    soup = BS(html_text, "html.parser")
    cards = soup.find_all("article", class_="product_pod")

    books = []

    for card in cards:
        title_element = card.find("h3")
        title_element = title_element.find("a")
        price_element = card.find("p", class_="price_color")
        stock_element = card.find("p", class_="availability")

        title = get_attr_or_empty(title_element, "title")

        price = get_text_or_empty(price_element)
        price = clean_price(price)

        stock = get_text_or_empty(stock_element)

        link = get_attr_or_empty(title_element, "href")
        link = urljoin(page_url, link)

        card_dict = {
            "title": title,
            "price": price,
            "category": category_name,
            "stock": stock,
            "link": link
        }

        books.append(card_dict)

    return books


def parse_category_pages(category_name, category_link):
    html_text = download_html(category_link)

    if not html_text:
        return []

    all_books = []

    page_books = parse_products(html_text, category_name, category_link)
    all_books.extend(page_books)

    base_category_url = category_link.replace("index.html", "")

    page_number = 2
    while True:
        page_url = base_category_url + f"page-{page_number}.html"

        html_text = download_html(page_url)

        if not html_text:
            break

        page_books = parse_products(html_text, category_name, page_url)

        if not page_books:
            break

        all_books.extend(page_books)

        page_number += 1

    return all_books


def db_init(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price REAL,
    category TEXT,
    stock TEXT,
    link TEXT UNIQUE
    )
    """)

    connection.commit()
    connection.close()


def save_products_to_db(db_file, products):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    for product in products:
        cursor.execute("""
        INSERT OR IGNORE INTO products (title, price, category, stock, link)
        VALUES (?, ?, ?, ?, ?)
        """, (
            product["title"],
            float(product["price"]),
            product["category"],
            product["stock"],
            product["link"]
        ))

    connection.commit()
    connection.close()


def get_product_by_link(db_file, link):
    connection = sqlite3.connect(db_file)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM products
    WHERE link = ?
    """, (link,))

    product = cursor.fetchone()

    connection.close()

    return product


def calculate_price_change(old_price, new_price):
    if old_price > new_price:
        direction = "decreased"

    elif old_price < new_price:
        direction = "increased"

    else:
        direction = "unchanged"

    difference_price = round(abs(new_price - old_price), 2)

    calculate_dict = {
        "old_price": old_price,
        "new_price": new_price,
        "difference": difference_price,
        "direction": direction
    }

    return calculate_dict


def update_product_price(db_file, product):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE products
    SET price = ?, stock = ?
    WHERE link = ?
    """, (
        float(product["price"]),
        product["stock"],
        product["link"]
    ))

    connection.commit()
    connection.close()


def check_price_changes(db_file, products):
    changes = []

    for product in products:
        old_product = get_product_by_link(db_file, product["link"])

        if old_product is None:
            save_products_to_db(db_file, [product])
            continue

        new_price = float(product["price"])
        old_price = float(old_product["price"])

        if new_price != old_price:
            change = calculate_price_change(old_price, new_price)

            change["title"] = product["title"]
            change["category"] = product["category"]
            change["stock"] = product["stock"]
            change["link"] = product["link"]

            changes.append(change)

            update_product_price(db_file, product)

    return changes


def save_changes_csv(csv_file, changes):
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["old_price", "new_price", "difference", "direction",
                      "title", "category", "stock", "link"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(changes)


def run_monitor(category, db_file="products.db", report_file="price_changes.csv"):
    html_text = download_html(BASE_URL)

    if not html_text:
        return "No HTML found"

    categories = parse_categories(html_text)

    if not categories:
        return "No categories found"

    category_link = find_category_link(categories, category)

    if not category_link:
        return f"Category not found: {category}"

    products = parse_category_pages(category, category_link)

    if not products:
        return "No products found"

    db_init(db_file)

    changes = check_price_changes(db_file, products)

    if changes:
        save_changes_csv(report_file, changes)

        return (
            f"Price changes found: {len(changes)}\n"
            f"Report saved: {report_file}"
        )

    return "No price changes found"
