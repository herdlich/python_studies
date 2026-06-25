import csv
import logging
import requests
import argparse
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup as BS

BASE_URL = "https://books.toscrape.com/"

Path("logs").mkdir(exist_ok=True)

time_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(level=logging.INFO, filename="logs/parser.log", encoding="utf-8",
                    format="[%(asctime)s] - %(levelname)s: %(message)s",
                    datefmt=time_format)


def save_csv(csv_file, data):
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["title", "price", "category", "stock", "link"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def download_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            html_text = response.text

            return html_text

        else:
            logging.warning(f"Page was not downloaded: {url}, status code: {response.status_code}")
            print(f"Page was not downloaded: {url}, status code: {response.status_code}")

            return False

    except requests.RequestException as error:
        logging.error(f"Request error: {error}")
        print(f"Request error: {error}")
        return False


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--category", default="psychology")
    parser.add_argument("--output", default="result.csv")
    parser.add_argument("--min-price", type=float, default=None)
    parser.add_argument("--max-price", type=float, default=None)

    return parser.parse_args()


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
        category_name = link.get_text(strip=True)

        category_link = get_attr_or_empty(link, "href")
        category_link = urljoin(BASE_URL, category_link)

        category_dict = {
            "name": category_name.lower(),
            "link": category_link
        }

        categories.append(category_dict)

    if not categories:
        print("No categories found")
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

    books_count = 0
    for card in cards:
        title_element = card.find("h3").find("a")
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

        books_count += 1

    print(f"Parsed books in {category_name}: {books_count}")

    return books


def filter_by_price(products, min_price, max_price):
    filtered_products = []

    for book in products:
        price = float(book["price"])

        if min_price is not None and price < min_price:
            continue

        if max_price is not None and price > max_price:
            continue

        filtered_products.append(book)

    return filtered_products


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


def main():
    args = get_args()

    html_text = download_html(BASE_URL)

    if not html_text:
        print("No HTML found")
        return

    categories = parse_categories(html_text)

    category_link = find_category_link(categories, args.category)

    if not category_link:
        print("Category not found")
        return

    books = parse_category_pages(args.category, category_link)

    if not books:
        print("No books found")
        return

    books = filter_by_price(books, args.min_price, args.max_price)

    if not books:
        print("No books found by price filter")
        return

    save_csv(Path(args.output), books)

    print(f"CSV saved: {args.output}")

    print(f"Saved books: {len(books)}")


if __name__ == "__main__":
    main()
