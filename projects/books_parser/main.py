import csv
import logging
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin

path_result = Path("result.csv")

BASE_URL = "https://books.toscrape.com/catalogue/"

Path("logs").mkdir(exist_ok=True)

time_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(level=logging.INFO, filename="logs/parser.log", encoding="utf-8",
                    format="[%(asctime)s] - %(levelname)s: %(message)s", datefmt=time_format)


def download_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            html_text = response.text
            logging.info(f"Page downloaded: {url}, status code: {response.status_code}")

            return html_text

        else:
            print(f"Page was not downloaded: {url}")
            logging.warning(f"Page was not downloaded: {url}, status code: {response.status_code}")
            return False

    except requests.RequestException as error:
        print(f"Request error: {error}")
        logging.error(f"Request error: {error}")
        return False


def save_csv(csv_file, data):
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["title", "price", "stock", "link"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def get_text_or_empty(element):
    if not element:
        result = ""
    else:
        result = element.get_text(strip=True)

    return result


def get_attr_or_empty(element, attr):
    if not element:
        result = ""
    else:
        result = element.get(attr)

    return result


def clean_price(price):
    price = price.replace("Â", "")
    price = price.replace("£", "")
    price = price.strip()

    return price


def parse_books(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    cards = soup.find_all("article", class_="product_pod")

    books = []

    for card in cards:
        price_element = card.find("p", class_="price_color")
        stock_element = card.find("p", class_="availability")
        link_element = card.find("h3").find("a")

        title = get_attr_or_empty(link_element, "title")

        price = get_text_or_empty(price_element)
        price = clean_price(price)

        stock = get_text_or_empty(stock_element)

        link = get_attr_or_empty(link_element, "href")

        link = urljoin(BASE_URL, link)

        card_dict = {
            "title": title,
            "price": price,
            "stock": stock,
            "link": link
        }

        books.append(card_dict)

    return books


def parse_all_pages():
    all_books = []

    pages_count = 0
    for page_number in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"

        html_text = download_html(url)

        if not html_text:
            continue

        books_list = parse_books(html_text)

        all_books.extend(books_list)

        logging.info(f"Parsed books from page {page_number}: {len(books_list)}")

        pages_count += 1

    if not all_books:
        print("No books found")
        logging.info("No books found")
        return

    save_csv(path_result, all_books)

    print(f"Pages processed: {pages_count}")
    print(f"Books saved: {len(all_books)}")

    logging.info(f"Pages processed: {pages_count}")
    logging.info(f"Books saved: {len(all_books)}")

    logging.info(f"CSV saved: {path_result}")


parse_all_pages()
