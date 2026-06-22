import csv
from pathlib import Path

# Input and output CSV file paths
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


def print_product(product):
    print(f"ID: {product['id']}\n"
          f"Product: {product['title']}\n"
          f"Category: {product['category']}\n"
          f"Price: {product['price']}\n"
          f"Stock: {product['stock']}")
    print("-" * 40)


def show_all_products():
    products = load_csv(path_products)

    count_products = 0

    # Print each product one by one
    for row in products:
        print_product(row)

        count_products += 1

    # Handle empty CSV file
    if count_products == 0:
        print("No products found")
        print()
        return

    print()


def category_filter():
    products = load_csv(path_products)
    found_categories = set()
    filtered_products = []

    # Collect unique categories
    for row in products:
        if "category" not in row:
            continue

        found_categories.add(row['category'])

    # Stop if there are no categories
    if not found_categories:
        print("No categories found")
        print()
        return

    print("Available categories:")

    # Show available categories to the user
    for category in found_categories:
        print(category)

    print()

    user_category = input("Choose category: ").strip()
    print()

    if user_category not in found_categories:
        print("Invalid category")
        print()
        return

    # Find products with the selected category
    for row in products:
        if user_category == row['category']:
            filtered_products.append(row)

    print(f"Products added: {len(filtered_products)}")
    print()

    # Save filtered products to result.csv
    save_csv(path_result, filtered_products)


def price_filter():
    products = load_csv(path_products)
    filtered_products = []

    user_price = input("Price: ")
    print()

    # Validate user input
    if not user_price.isdigit():
        print("Price must be a number")
        print()
        return

    user_price = int(user_price)

    # Find products with the selected price
    for row in products:
        if "price" not in row:
            continue

        if user_price == int(row['price']):
            filtered_products.append(row)

    # Stop if no products match the price
    if not filtered_products:
        print("Products not found")
        print()
        return

    print(f"Products added: {len(filtered_products)}")
    print()

    # Save filtered products to result.csv
    save_csv(path_result, filtered_products)


def stats_price():
    products = load_csv(path_products)
    prices = []

    # Collect product prices
    for row in products:
        if "price" not in row:
            continue

        prices.append(int(row['price']))

    # Stop if there are no prices
    if not prices:
        print("Products not found")
        return

    # Print basic price statistics
    print(f"Total price: {sum(prices)}\n"
          f"Average price: {sum(prices) / len(prices)}\n"
          f"Minimal price: {min(prices)}\n"
          f"Maximal price: {max(prices)}")
    print()


# Menu actions mapped to user choices
menu_option = {
    "1": show_all_products,
    "2": category_filter,
    "3": price_filter,
    "4": stats_price
}

# Main menu loop
while True:
    user_choice = input("1. Show all products\n"
                        "2. Filter by category\n"
                        "3. Filter by price\n"
                        "4. Stats price\n"
                        "5. Exit\n\n"
                        "Enter: ")

    # Run selected menu action
    if user_choice in menu_option:
        print()
        menu_option[user_choice]()

    # Exit the program
    elif user_choice == "5":
        print()
        print("End")
        break

    # Handle invalid menu input
    else:
        print()
        print("Invalid choice")