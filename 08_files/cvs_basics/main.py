import csv
from pathlib import Path

path = Path("products.csv")

def print_product(product):
    print(f"ID: {product['id']}")
    print(f"Title: {product['title']}")
    print(f"Category: {product['category']}")
    print(f"Price: {product['price']}")
    print(f"Stock: {product['stock']}")
    print("-" * 40)


def load_csv(csv_file):
    with open(csv_file, "r", encoding='utf-8', newline='') as csvfile:
        reader = list(csv.DictReader(csvfile))

        return reader


def show_all_products():
    products = load_csv(path)

    for row in products:
        print_product(row)

    print(f"Total products: {len(products)}\n")


def category_filter():
    products = load_csv(path)
    categories = set()

    for row in products:
        if "category" in row:
            categories.add(row["category"])

    if not categories:
        print("Categories not found")
        return

    print("Available categories:")

    for category in categories:
        print(f"{category}\n")

    user_category = input("Category: \n").strip().lower()

    found = False
    matches_count = 0

    for row in products:
        if row["category"].lower() == user_category:
            print_product(row)
            found = True
            matches_count += 1

    print(f"Matches: {matches_count}\n")

    if not found:
        print("Category not found")
        return


menu_option = {
    "1": show_all_products,
    "2": category_filter
}

while True:
    user_choice = input("1. Show all products\n"
                        "2. Filter by category\n"
                        "3. Exit\n"
                        "Enter: ")

    if user_choice in menu_option:
        print()
        menu_option[user_choice]()

    elif user_choice == "3":
        print("End.")
        break

    else:
        print("Invalid choice")