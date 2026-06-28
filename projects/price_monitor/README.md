# Price Monitor

A Python price monitoring script for [Books to Scrape](https://books.toscrape.com/).

The script parses products from a selected category, stores them in a SQLite database, compares fresh prices with previously saved prices, detects price changes, updates the database, and saves detected changes to a CSV report.

## Features

* Downloads HTML pages using `requests`
* Parses HTML with `BeautifulSoup`
* Extracts product categories
* Finds a selected category by name
* Supports pagination inside a category
* Parses product data:

  * title
  * price
  * category
  * stock status
  * product link
* Stores products in SQLite
* Uses product links as unique identifiers
* Compares old and new prices
* Detects price increases and decreases
* Calculates price difference
* Updates stored product prices after changes
* Saves price changes to a CSV report
* Supports command-line arguments
* Logs request errors and failed downloads

## Technologies

* Python
* requests
* BeautifulSoup4
* sqlite3
* argparse
* logging
* csv
* pathlib
* urllib.parse

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

```text
requests
beautifulsoup4
```

## Usage

Run with default settings:

```bash
python main.py
```

By default, the script parses the `psychology` category, stores products in `products.db`, and saves detected changes to `price_changes.csv`.

Parse a specific category:

```bash
python main.py --category mystery
```

Use a custom database file:

```bash
python main.py --category mystery --db products.db
```

Use a custom report file:

```bash
python main.py --category mystery --db products.db --report price_changes.csv
```

Full example:

```bash
python main.py --category mystery --db products.db --report price_changes.csv
```

## Command-line Arguments

| Argument     | Description                       | Default             |
| ------------ | --------------------------------- | ------------------- |
| `--category` | Category name to monitor          | `psychology`        |
| `--db`       | SQLite database file path         | `products.db`       |
| `--report`   | CSV report file for price changes | `price_changes.csv` |

## How It Works

1. The script downloads the main page.
2. It parses all available categories.
3. It finds the selected category by name.
4. It downloads the selected category page.
5. It parses products from the category.
6. It follows category pagination such as `page-2.html`, `page-3.html`, etc.
7. It creates a SQLite database if it does not exist.
8. For each parsed product, it searches the database by product link.
9. If the product is not found, it is added to the database.
10. If the product already exists, the script compares the old stored price with the fresh parsed price.
11. If the price changed, the script:

    * calculates the difference
    * detects whether the price increased or decreased
    * adds the change to a CSV report
    * updates the product price in the database

## SQLite Database

The script creates a SQLite database with a `products` table.

Table structure:

```sql
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price REAL,
    category TEXT,
    stock TEXT,
    link TEXT UNIQUE
);
```

The `link` field is unique and is used as the product identifier.

This allows the script to connect a freshly parsed product with its previously stored version.

## Price Change Report

If price changes are found, the script saves them to a CSV file.

Report columns:

```text
old_price,new_price,difference,direction,title,category,stock,link
```

Example row:

```text
45.17,39.99,5.18,decreased,Book Title,mystery,In stock,https://example.com/product
```

If no price changes are found, the script prints:

```text
No price changes found
```

## Testing Price Changes

The target website has static prices, so price changes will not appear naturally.

To test the monitor:

1. Run the script once to fill the database.
2. Open the SQLite database.
3. Manually change the price of one product.
4. Run the script again.
5. The script should detect the difference, create a CSV report, and update the database price.

Example:

```bash
python main.py --category mystery --db products.db --report price_changes.csv
```

## Project Structure

```text
price_monitor/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── logs/
    └── parser.log
```

Generated files such as logs, CSV reports, SQLite databases, and cache folders should not be committed to GitHub.

Recommended `.gitignore`:

```text
__pycache__/
*.pyc
logs/
*.db
*.csv
.venv/
venv/
```

## Notes

This project was built as a practice project for learning:

* web scraping
* pagination
* SQLite storage
* state comparison
* price change detection
* CSV reporting
* command-line interfaces
* basic data monitoring logic

The target website is designed for scraping practice, so price changes are simulated manually during testing.
