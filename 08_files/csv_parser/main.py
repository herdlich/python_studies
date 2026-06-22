import csv
from pathlib import Path

path_products = Path("products.csv")
path_result = Path("result.csv")


def load_csv(csv_file):
    with open(csv_file, "r", encoding="utf-8", newline="") as file:
        reader = list(csv.DictReader(file))

        return reader


def save_csv(csv_file, data):
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["id", "title", "category", "price", "stock"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def price_filter():
    products = load_csv(path_products)
    add_products = []
    user_price = int(input("Price: "))

    for row in products:
        if "price" not in row:
            continue

        if user_price == int(row["price"]):
            add_products.append(row)

    if not add_products:
        print("Products not found")
        return

    save_csv(path_result, add_products)

    print(f"Products found: {len(add_products)}")


price_filter()
