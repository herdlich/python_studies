# HN News Watcher

A Python news watcher that parses Hacker News newest posts, saves parsed items to CSV, stores already seen posts in SQLite, and detects new items between script runs.

The project is built as a practical web scraping and monitoring tool using `requests`, `BeautifulSoup`, `SQLite`, `argparse`, `logging`, and `csv`.

## Features

- Parse Hacker News `/newest`
- Follow pagination through the `More` link
- Support custom page count with `--pages`
- Extract structured news data
- Save all parsed items to CSV
- Save only new items to a separate CSV file
- Store already seen items in SQLite
- Detect new posts between script runs
- Use `item_id` as a unique identifier
- Support custom output paths
- Log parser activity and errors

## Collected Fields

The watcher saves the following fields:

```text
title
link
age
author
points
comments
item_id
parsed_at
```

## Project Structure

```text
hn_news_watcher/
├── watcher.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── news.csv
│   ├── new_items.csv
│   └── news.db
└── logs/
    └── watcher.log
```

The `data/` and `logs/` folders are generated automatically when the script runs.

## Installation

Clone the repository:

```bash
git clone https://github.com/herdlich/python_studies.git
cd python_studies/projects/hn_news_watcher
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

Run the watcher with default settings:

```bash
python watcher.py
```

By default, the script parses 3 pages from Hacker News `/newest`.

Run with a custom number of pages:

```bash
python watcher.py --pages 5
```

Use a custom SQLite database path:

```bash
python watcher.py --db data/custom_news.db
```

Use a custom CSV output path for all parsed news:

```bash
python watcher.py --output data/all_news.csv
```

Use a custom CSV output path for new items only:

```bash
python watcher.py --new-output data/new_only.csv
```

Run with all options:

```bash
python watcher.py --pages 5 --db data/news.db --output data/news.csv --new-output data/new_items.csv
```

## Command Line Arguments

| Argument | Default | Description |
|---|---:|---|
| `--pages` | `3` | Number of Hacker News pages to parse |
| `--db` | `data/news.db` | SQLite database path |
| `--output` | `data/news.csv` | CSV file with all parsed items |
| `--new-output` | `data/new_items.csv` | CSV file with only newly detected items |

## Output Files

```text
data/news.csv
```

Contains all parsed Hacker News items from the current run.

```text
data/new_items.csv
```

Contains only items that were not found in the SQLite database before the current run.

```text
data/news.db
```

SQLite database with already seen Hacker News item IDs.

```text
logs/watcher.log
```

Log file with parser activity and basic errors.

## How It Works

1. The script downloads the Hacker News `/newest` page.
2. It parses news rows from the HTML table.
3. It extracts title, link, age, author, points, comments, item ID, and parsing time.
4. It finds the `More` link and continues parsing the next pages.
5. It saves all parsed items to the output CSV file.
6. It checks every item against the SQLite database.
7. If an item ID is not found in the database, the item is considered new.
8. New items are saved to the database and exported to the new-items CSV file.

## Example Behavior

First run:

```text
Found news: 90
New news: 90
Output file: data/news.csv
```

Second run shortly after:

```text
Found news: 90
New news: 0
Output file: data/news.csv
```

After new Hacker News posts appear:

```text
Found news: 90
New news: 5
Output file: data/news.csv
```

## Dependencies

```text
requests
beautifulsoup4
```

## Notes

This project works with publicly available Hacker News pages.

It does not use browser automation, login, CAPTCHA bypassing, private data access, or anti-bot bypassing.

The project is intended for educational and portfolio purposes. It demonstrates a practical watcher pattern: parsing data, storing seen records, and detecting new items on repeated runs.

## Status

Project version: `v2`

Current version supports Hacker News parsing, pagination, SQLite storage, new item detection, CSV export, logging, and command-line arguments for page count, database path, all-items output, and new-items output.