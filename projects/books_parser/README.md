# Books Parser

A Python web scraper that collects book data from [Books to Scrape](https://books.toscrape.com/) and saves the results to a CSV file.

## Features

* Downloads book catalogue pages using `requests`
* Parses HTML with `BeautifulSoup`
* Extracts book data:

  * title
  * price
  * stock status
  * product link
* Supports pagination
* Supports command-line arguments
* Converts relative product links to full URLs
* Cleans price values
* Saves collected data to a CSV file
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

By default, the script parses 50 pages and saves the result to:

```text
result.csv
```

Run with custom page count and output file:

```bash
python main.py --pages 3 --output test.csv
```

Example console output:

```text
Pages processed: 3
Books saved: 60
```

## Command-line Arguments

| Argument   | Description                        | Default      |
| ---------- | ---------------------------------- | ------------ |
| `--pages`  | Number of catalogue pages to parse | `50`         |
| `--output` | Output CSV file name               | `result.csv` |

## Output Format

The output CSV file contains the following columns:

```csv
title,price,stock,link
```

Example row:

```csv
A Light in the Attic,51.77,In stock,https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
```

## Logging

The script creates a log file:

```text
logs/parser.log
```

The log file contains information about:

* downloaded pages
* parsed books from each page
* failed page downloads
* request errors
* final parsing results
* saved CSV file path

Example log messages:

```text
[2026-06-24 14:30:12] - INFO: Page downloaded: https://books.toscrape.com/catalogue/page-1.html, status code: 200
[2026-06-24 14:30:13] - INFO: Parsed books from page 1: 20
[2026-06-24 14:30:20] - INFO: CSV saved: result.csv
```

## Project Structure

```text
books_parser/
├── main.py
├── README.md
├── requirements.txt
└── logs/
    └── parser.log
```

## How It Works

1. The script reads command-line arguments.
2. It generates catalogue page URLs.
3. Each page is downloaded with `requests`.
4. HTML content is parsed with `BeautifulSoup`.
5. Book cards are extracted from each page.
6. Book data is cleaned and collected into a list.
7. All collected data is saved to a CSV file.
8. Progress and errors are written to `logs/parser.log`.

## Notes

This project is built for learning web scraping basics with Python.
The target website is designed for scraping practice.
