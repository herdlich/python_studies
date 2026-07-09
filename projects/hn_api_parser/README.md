# HN API Parser

A Python API parser that collects Hacker News posts through the Algolia Hacker News Search API and saves structured results to CSV and SQLite.

Unlike HTML scrapers, this project works directly with JSON API responses. It is built as a practical API/XHR parsing project using `requests`, `argparse`, `csv`, `SQLite`, and `logging`.

## Features

- Fetch Hacker News posts from the Algolia API
- Search posts by custom query
- Support multiple API pages
- Parse JSON responses
- Extract structured post data
- Save results to CSV
- Save results to SQLite
- Use API `object_id` as a unique identifier
- Support custom output and database paths
- Log request errors and parser activity

## Collected Fields

The parser saves the following fields:

```text
object_id
title
url
author
points
comments_count
created_at
updated_at
```

## Project Structure

```text
hn_api_parser/
├── api_parser.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── news.csv
│   └── news.db
└── logs/
    └── api_parser.log
```

The `data/` and `logs/` folders are generated automatically when the script runs.

## Installation

Clone the repository:

```bash
git clone https://github.com/herdlich/python_studies.git
cd python_studies/hn_api_parser
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

Run with the default query:

```bash
python api_parser.py
```

By default, the parser searches for:

```text
python
```

Run with a custom query:

```bash
python api_parser.py --query django
```

Run with multiple API pages:

```bash
python api_parser.py --query python --pages 3
```

Use a custom CSV output path:

```bash
python api_parser.py --query python --output data/python_news.csv
```

Use a custom SQLite database path:

```bash
python api_parser.py --db data/custom_news.db
```

Run with all options:

```bash
python api_parser.py --query python --pages 3 --output data/python_news.csv --db data/python_news.db
```

## Command Line Arguments

| Argument | Default | Description |
|---|---:|---|
| `--query` | `python` | Search query for Hacker News posts |
| `--pages` | `1` | Number of API result pages to fetch |
| `--output` | `data/news.csv` | CSV output file path |
| `--db` | `data/news.db` | SQLite database file path |

## Output Files

```text
data/news.csv
```

Contains parsed Hacker News API results.

```text
data/news.db
```

SQLite database with parsed posts. The `object_id` field is used as the primary key.

```text
logs/api_parser.log
```

Log file with request errors and parser activity.

## How It Works

1. The script sends a GET request to the Hacker News Algolia API.
2. Query parameters are passed through `params`.
3. The API returns a JSON response.
4. The parser reads the `hits` list from the response.
5. Each hit is normalized into a clean Python dictionary.
6. Results are exported to CSV.
7. Results are also saved to SQLite using `object_id` as a unique key.

## Example Behavior

```bash
python api_parser.py --query python --pages 2
```

Example output:

```text
News saved: 40
Output: data/news.csv
```

## Dependencies

```text
requests
```

## Notes

This project works with a public API and does not parse private data.

It does not use browser automation, login, CAPTCHA bypassing, private accounts, or anti-bot bypassing.

The project is intended for educational and portfolio purposes. It demonstrates the API/XHR parsing pattern: request data from an API, parse JSON, normalize records, and export structured results.

## Status

Project version: `v1`

Current version supports Hacker News API search, pagination, CSV export, SQLite storage, logging, and command-line arguments.