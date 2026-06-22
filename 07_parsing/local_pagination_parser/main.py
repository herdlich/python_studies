import csv
from pathlib import Path
from bs4 import BeautifulSoup

# Folder with HTML pages
path_pages = Path("pages")

# Output CSV file
path_result = Path("result.csv")


def save_csv(csv_file, data):
    # Open CSV file for writing
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        # CSV column names
        fieldnames = ["title", "category", "price", "stock", "link"]

        # Create CSV writer
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def get_text_or_empty(element):
    # Return empty string if the element was not found
    if not element:
        result = ""

    else:
        # Get text from HTML element and remove extra spaces
        result = element.get_text(strip=True)

    return result


def parse_page(html):
    # Read HTML file content
    html_text = html.read_text(encoding="utf-8")

    # Create BeautifulSoup object for parsing HTML
    soup = BeautifulSoup(html_text, "html.parser")

    # Find all product cards on the page
    cards = soup.find_all("div", class_="product-card")

    # Stop parsing if there are no products
    if not cards:
        print("No products found")
        return []

    # List for products from one page
    csv_products = []

    # Parse each product card
    for card in cards:
        # Find product elements inside the card
        title_element = card.find("h2", class_="product-title")
        category_element = card.find("p", class_="category")
        price_element = card.find("p", class_="price")
        stock_element = card.find("p", class_="stock")
        link_element = card.find("a", class_="product-link")

        # Extract text from elements
        title = get_text_or_empty(title_element)
        category = get_text_or_empty(category_element)
        price = get_text_or_empty(price_element)
        stock = get_text_or_empty(stock_element)

        # Extract link href attribute
        if not link_element:
            link = ""
        else:
            link = link_element.get("href")

        # Store product data in a dictionary
        card_dict = {
            "title": title,
            "category": category,
            "price": price,
            "stock": stock,
            "link": link
        }

        csv_products.append(card_dict)

    # Stop if the product list is empty
    if not csv_products:
        print(f"No products found in {html.name}")
        return []

    print(f"Products found in {html.name}: {len(cards)}")

    return csv_products


def parse_all_pages():
    # List for products from all HTML files
    all_products = []

    files_count = 0

    # Go through all HTML files in the pages folder
    for file in path_pages.glob("*.html"):
        files_count += 1

        # Parse one HTML file
        products_from_page = parse_page(file)

        if not products_from_page:
            print("No products found")
            continue

        # Add products from this page to the main list
        all_products.extend(products_from_page)

    # Stop if no HTML files were found
    if files_count == 0:
        print("No HTML files found")
        return

    # Stop if no products were found in all files
    if not all_products:
        return

    # Save all products to CSV
    save_csv(path_result, all_products)

    # Print final statistics
    print()
    print(f"Files: {files_count}")
    print(f"Saved products: {len(all_products)}")


# Start the parser
parse_all_pages()
