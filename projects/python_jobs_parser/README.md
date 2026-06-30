# Python Jobs Parser

A Python web scraper that collects job listings from the Python.org Jobs page, opens each job detail page, extracts full job information, and saves the result to a CSV file.

The project is built as a real-world web scraping practice project using `requests`, `BeautifulSoup`, `argparse`, `logging`, and `csv`.

## Features

- Parse job listings from Python.org Jobs
- Automatically go through all available listing pages
- Collect job detail page links
- Open each job detail page
- Extract full job information
- Extract job descriptions from detail pages
- Save results to a CSV file
- Support custom output file path
- Handle missing HTML, empty pages, and missing fields
- Normalize job links with absolute URLs
- Add parsing timestamp for each record
- Log parser activity and errors
- Use delay between detail page requests

## Collected Fields

The parser saves the following fields:

```text
title
company
location
category
description
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
├── data/
│   └── jobs.csv
└── logs/
    └── parser.log
```

The `data/` and `logs/` folders are generated automatically when the parser runs.

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
title,company,location,category,description,date,link,parsed_at
```

Example:

```text
Senior Python Developer,Example Company,Remote,Developer / Engineer,Full job description text...,29 June 2026,https://www.python.org/jobs/0000/,2026-06-30 14:14:30
```

## How It Works

1. The parser downloads the Python.org Jobs listing page.
2. It extracts links to individual job detail pages.
3. It continues parsing listing pages until an empty page is reached.
4. It opens each job detail page.
5. It extracts title, company, location, category, description, date, and link.
6. It saves the collected data to a CSV file.
7. It writes parser activity and errors to `logs/parser.log`.

## Logging

The parser creates a log file:

```text
logs/parser.log
```

The log contains information about:

- parsed listing pages
- found job links
- parsed vacancy detail pages
- request errors
- empty results
- saved vacancies

## Dependencies

```text
requests
beautifulsoup4
```

## Notes

This parser is intended for educational purposes and works with publicly available job listing pages.

It does not use browser automation, login, CAPTCHA bypassing, or private data access.

A small delay is used between detail page requests to avoid sending too many requests too quickly.

## Status

Project version: `v2`

The current version parses all available listing pages, opens each job detail page, extracts job descriptions, logs parser activity, and exports clean job data to CSV.