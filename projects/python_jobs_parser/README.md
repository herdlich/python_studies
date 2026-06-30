# Python Jobs Parser

A Python parser that collects job listings from the Python.org Jobs page and saves them to a CSV file.

The project is built as a real-world web scraping practice project using `requests`, `BeautifulSoup`, `argparse`, and `csv`.

## Features

* Parse job listings from Python.org Jobs
* Automatically go through all available pages
* Extract job data from listing cards
* Save results to a CSV file
* Support custom output file path
* Handle missing HTML and empty pages
* Normalize job links with absolute URLs
* Add parsing timestamp for each record

## Collected Fields

The parser saves the following fields:

```text
title
company
location
category
date
link
parsed_at
```

## Project Structure

```text
python_jobs_parser/
├── parser.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
    └── jobs.csv
```

The `data/` folder is generated automatically when the parser runs.

## Installation

Clone the repository:

```bash
git clone https://github.com/herdlich/python_studies.git
cd python_studies/python_jobs_parser
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the parser with the default output path:

```bash
python parser.py
```

By default, the result will be saved to:

```text
data/jobs.csv
```

You can also specify a custom output file:

```bash
python parser.py --output data/python_jobs.csv
```

## Example Output

The generated CSV file contains job listings with columns like:

```text
title,company,location,category,date,link,parsed_at
```

Example:

```text
Senior Python Developer,Example Company,Remote,Developer / Engineer,29 June 2026,https://www.python.org/jobs/0000/,2026-06-30 14:14:30
```

## How It Works

1. The parser downloads the Python.org Jobs page.
2. It extracts job cards from the HTML.
3. For each job card, it collects title, company, location, category, date, and link.
4. It continues parsing pages until an empty page is reached.
5. The collected data is saved to a CSV file.

## Dependencies

```text
requests
beautifulsoup4
```

## Notes

This parser is intended for educational purposes and works with publicly available job listing pages.

It does not use browser automation, login, CAPTCHA bypassing, or private data access.

## Status

Project version: `v1`

The current version parses all available listing pages and exports job data to CSV.
