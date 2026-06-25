# Product Parser

A Python command-line web scraper that collects book product data from [Books to Scrape](https://books.toscrape.com/) by selected category and saves the results to a CSV file.

## Features

* Downloads pages using `requests`
* Parses HTML with `BeautifulSoup`
* Extracts available product categories
* Finds a selected category by name
* Parses products from the selected category
* Extracts product data:

  * title
  * price
  * category
  * stock status
  * product link
* Supports price filtering:

  * minimum price
  * maximum price
* Supports command-line arguments
* Saves results to a CSV file
* Writes logs to `logs/parser.log`

## Technologies

* Python
* requests
* BeautifulSoup4
* argparse
* logging
* csv
* pathlib
* urllib.parse

## Installation

Clone the repository or download the project files.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

The project uses the following external libraries:

```text
requests
beautifulsoup4
```

## Usage

Run with default settings:

```bash
python main.py
```

By default, the script parses the `psychology` category and saves the result to:

```text
result.csv
```

Run with a custom category:

```bash
python main.py --category travel --output travel.csv
```

Run with price filters:

```bash
python main.py --category travel --min-price 20 --max-price 50 --output travel_filtered.csv
```

Run with only minimum price:

```bash
python main.py --category travel --min-price 40 --output expensive_travel.csv
```

Run with only maximum price:

```bash
python main.py --category travel --max-price 20 --output cheap_travel.csv
```

## Command-line Arguments

| Argument      | Description               | Default      |
| ------------- | ------------------------- | ------------ |
| `--category`  | Product category to parse | `psychology` |
| `--output`    | Output CSV file name      | `result.csv` |
| `--min-price` | Minimum product price     | `None`       |
| `--max-price` | Maximum product price     | `None`       |

## Output Format

The output CSV file contains the following columns:

```csv
title,price,category,stock,link
```

Example row:

```csv
It's Only the Himalayas,45.17,travel,In stock,https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html
```

## Logging

The script creates a log file:

```text
logs/parser.log
```

The log file contains information about:

* failed page downloads
* request errors

## Project Structure

```text
product_parser/
├── main.py
├── README.md
├── requirements.txt
└── logs/
    └── parser.log
```

Generated CSV files, such as `result.csv` or `travel.csv`, are created after running the script.

## How It Works

1. The script reads command-line arguments.
2. It downloads the main page.
3. It extracts available categories and their links.
4. It finds the selected category.
5. It downloads the selected category page.
6. It parses product cards from the category page.
7. It filters products by price if filters are provided.
8. It saves the result to a CSV file.

## Notes

This project is built for learning web scraping basics with Python.
The target website is designed for scraping practice.
