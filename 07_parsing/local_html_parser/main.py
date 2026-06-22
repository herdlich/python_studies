import csv
from pathlib import Path
from bs4 import BeautifulSoup

path_page = Path("page.html")
path_result = Path("result.csv")


def save_csv(csv_file, data):
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["title", "category", "price", "stock", "link"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


def html_parser():
    html_text = path_page.read_text(encoding="utf-8")
    soup = BeautifulSoup(html_text, "html.parser")
    cards = soup.find_all("div", class_="product-card")

    if not cards:
        print("No cards found")
        return

    csv_products = []

    for card in cards:
        title_element = card.find("h2", class_="product-title")
        category_element = card.find("p", class_="category")
        price_element = card.find("p", class_="price")
        stock_element = card.find("p", class_="stock")
        link_element = card.find("a", class_="product-link")

        title = title_element.get_text(strip=True)
        category = category_element.get_text(strip=True)
        price = price_element.get_text(strip=True)
        stock = stock_element.get_text(strip=True)
        link = link_element.get("href")

        print(f"Title: {title}\n"
              f"Category: {category}\n"
              f"Price: {price}\n"
              f"Stock: {stock}\n"
              f"Link: {link}")
        print("-" * 40)

        card_dict = {
            "title": title,
            "category": category,
            "price": price,
            "stock": stock,
            "link": link
        }

        csv_products.append(card_dict)

    print(f"Products found: {len(cards)}")

    save_csv(path_result, csv_products)


html_parser()