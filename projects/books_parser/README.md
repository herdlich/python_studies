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

## Technologies

* Python
* requests
* BeautifulSoup4
* csv
* pathlib
* urllib.parse

## Installation

Clone the repository or download the project files.

Install dependencies:

```bash
pip install requests beautifulsoup4
```

Or, if you use `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python main.py
```

After running, the script will create a CSV file:

```text
result.csv
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

## Project Structure

```text
books_parser/
├── main.py
├── result.csv
├── requirements.txt
└── README.md
```

## How It Works

1. The script generates URLs for catalogue pages from 1 to 50.
2. Each page is downloaded with `requests`.
3. HTML content is parsed with `BeautifulSoup`.
4. Book cards are extracted from the page.
5. Book data is collected and cleaned.
6. All results are saved into one CSV file.

## Notes

This project is built for learning web scraping basics with Python.
The target website is designed for scraping practice.
