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
* Supports pagination across 50 catalogue pages
* Converts relative product links to full URLs
* Cleans price values
* Saves collected data to `result.csv`
* Writes parser logs to `logs/parser.log`

## Technologies

* Python
* requests
* BeautifulSoup4
* csv
* pathlib
* logging
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

Run the script:

```bash
python main.py
```

After running, the script will:

* scrape book data from 50 catalogue pages
* save results to `result.csv`
* create logs in `logs/parser.log`

Example console output:

```text
Pages processed: 50
Books saved: 1000
```

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

Example log messages:

```text
[2026-06-24 14:30:12] - INFO: Page downloaded: https://books.toscrape.com/catalogue/page-1.html
[2026-06-24 14:30:13] - INFO: Parsed books from page 1: 20
[2026-06-24 14:30:20] - INFO: Books saved: 1000
```

## Project Structure

```text
books_parser/
├── main.py
├── README.md
├── requirements.txt
├── result.csv
└── logs/
    └── parser.log
```

## How It Works

1. The script generates URLs for catalogue pages from 1 to 50.
2. Each page is downloaded with `requests`.
3. HTML content is parsed with `BeautifulSoup`.
4. Book cards are extracted from each page.
5. Book data is cleaned and collected into a list.
6. All collected data is saved to `result.csv`.
7. The script writes progress and errors to `logs/parser.log`.

## Notes

This project is built for learning web scraping basics with Python.
The target website is designed for scraping practice.
