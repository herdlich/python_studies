# Product Parser

A Python parser for [Books to Scrape](https://books.toscrape.com/).

The script parses book products from a selected category, supports category pagination, filters products by price, saves results to CSV, and stores parsed products in a SQLite database with duplicate protection.

## Features

* Downloads HTML pages using `requests`
* Parses HTML with `BeautifulSoup`
* Extracts available product categories
* Finds a selected category by name
* Supports pagination inside a category
* Parses product data:

  * title
  * price
  * category
  * stock status
  * product link
* Filters products by minimum and maximum price
* Saves results to CSV
* Saves results to SQLite database
* Prevents duplicate database records using unique product links
* Supports command-line arguments
* Logs request errors and failed downloads

## Technologies

* Python
* requests
* BeautifulSoup4
* argparse
* sqlite3
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

By default, the script parses the `psychology` category, saves results to `result.csv`, and stores products in `products.db`.

Parse a specific category:

```bash
python main.py --category travel
```

Save results to a custom CSV file:

```bash
python main.py --category travel --output travel.csv
```

Filter products by price:

```bash
python main.py --category mystery --min-price 20 --max-price 40 --output mystery.csv
```

Use a custom SQLite database file:

```bash
python main.py --category mystery --output mystery.csv --db products.db
```

Full example:

```bash
python main.py --category mystery --min-price 20 --max-price 40 --output mystery_filtered.csv --db products.db
```

## Command-line Arguments

| Argument      | Description               | Default       |
| ------------- | ------------------------- | ------------- |
| `--category`  | Category name to parse    | `psychology`  |
| `--output`    | Output CSV file path      | `result.csv`  |
| `--min-price` | Minimum product price     | `None`        |
| `--max-price` | Maximum product price     | `None`        |
| `--db`        | SQLite database file path | `products.db` |

## Output CSV Format

The CSV file contains the following columns:

```text
title,price,category,stock,link
```

Example row:

```text
It's Only the Himalayas,45.17,travel,In stock,https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html
```

## SQLite Database

The script creates a SQLite database file and stores parsed products in the `products` table.

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

The `link` field is unique, so running the parser multiple times does not create duplicate product records.

Products are inserted using:

```sql
INSERT OR IGNORE
```

This means duplicate products are skipped automatically.

## Project Structure

```text
product_parser/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── logs/
    └── parser.log
```

Generated files such as CSV, database files, logs, and cache folders should not be committed to GitHub.

Recommended `.gitignore`:

```text
__pycache__/
*.pyc
logs/
*.csv
*.db
.venv/
venv/
```

## How It Works

1. The script downloads the main page.
2. It parses available book categories.
3. It finds the selected category by name.
4. It downloads the first category page.
5. It parses products from the page.
6. It generates and downloads paginated category pages such as `page-2.html`, `page-3.html`, etc.
7. It stops when the next page is not available.
8. It filters parsed products by price.
9. It saves filtered products to a CSV file.
10. It creates a SQLite database if needed.
11. It saves products to the database.
12. Duplicate products are ignored by unique product links.

## Notes

This project was built as a practice parser for learning:

* HTTP requests
* HTML parsing
* pagination
* command-line arguments
* CSV export
* SQLite storage
* duplicate protection
* basic project structure

The target website is designed for scraping practice.
