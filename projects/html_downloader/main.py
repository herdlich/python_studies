import csv
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin

path_page = Path("page.html")
path_result = Path("result.csv")

BASE_URL = "https://books.toscrape.com/"


def download_html():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(BASE_URL, headers=headers, timeout=10)

        if response.status_code == 200:
            path_page.write_text(response.text, encoding="utf-8")
            print("HTML saved successfully")
            return True
        else:
            print("Page was not downloaded")
            return False

    except requests.RequestException as error:
        print(f"Request error: {error}")
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


def clean_price(price):
    price = price.replace("Â", "")
    price = price.replace("£", "")
    price = price.strip()

    return price


def html_parser():
    html_text = path_page.read_text(encoding="utf-8")
    soup = BeautifulSoup(html_text, "html.parser")
    cards = soup.find_all("article", class_="product_pod")

    books = []

    for card in cards:
        price_element = card.find("p", class_="price_color")
        stock_element = card.find("p", class_="availability")
        link_element = card.find("h3").find("a")

        title = link_element.get("title")
        price = get_text_or_empty(price_element)

        price = clean_price(price)

        stock = get_text_or_empty(stock_element)
        link = link_element.get("href")

        link = urljoin(BASE_URL, link)

        print(f"Title: {title}\n"
              f"Price: {price}\n"
              f"Stock: {stock}\n"
              f"Link: {link}")
        print("-" * 40)

        card_dict = {
            "title": title,
            "price": price,
            "stock": stock,
            "link": link
        }

        books.append(card_dict)

    if not books:
        print("No books found")
        return

    print(f"Books found: {len(books)}")

    save_csv(path_result, books)


def main():
    successful = download_html()

    if not successful:
        return

    html_parser()


main()
