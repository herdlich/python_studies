# Telegram Price Monitor Bot

A Telegram bot that monitors book prices by category, compares current prices with saved data, and sends a CSV report when price changes are found.

The bot uses [Books to Scrape](https://books.toscrape.com/) as a demo website for parsing and price monitoring.

## Features

* Parse book categories from the website
* Monitor prices by selected category
* Store product data in SQLite
* Compare current prices with saved prices
* Detect price increases and decreases
* Generate CSV reports with price changes
* Send CSV reports directly in Telegram
* Restrict access by Telegram user ID
* Show available categories
* Send the latest saved report

## Tech Stack

* Python
* aiogram
* requests
* BeautifulSoup4
* SQLite
* python-dotenv
* CSV

## Project Structure

```text
telegram_price_bot/
├── bot.py
├── monitor.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Commands

```text
/start — greeting
/help — list of commands
/categories — show available book categories
/monitor <category> — check price changes for a selected category
/last_report — send the latest CSV report
/id — show your Telegram user ID
```

Example:

```text
/monitor mystery
```

## How It Works

1. The user sends a command to the Telegram bot.
2. `bot.py` handles Telegram commands using aiogram.
3. `monitor.py` downloads and parses book data from the website.
4. Products are stored in a SQLite database.
5. On the next check, current prices are compared with saved prices.
6. If price changes are found, the bot creates a CSV report.
7. The report is sent to the user in Telegram.

## Installation

Clone the repository:

```bash
git clone https://github.com/herdlich/python_studies.git
cd python_studies/projects/telegram_price_bot
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

## Environment Variables

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_bot_token_here
ALLOWED_USERS=123456789,987654321
```

Where:

* `BOT_TOKEN` is your Telegram bot token from BotFather
* `ALLOWED_USERS` is a comma-separated list of Telegram user IDs that are allowed to use protected commands

You can get your Telegram user ID with:

```text
/id
```

## Example `.env.example`

```env
BOT_TOKEN=your_bot_token_here
ALLOWED_USERS=123456789,987654321
```

## Running the Bot

```bash
python bot.py
```

The bot works only while the script is running.

If the bot is launched locally, all database files, reports, and logs are created on your local machine.

## Generated Files

The project can generate local files:

```text
products.db
price_changes.csv
logs/
```

These files are ignored by Git because they contain local runtime data.

## Git Ignore

Recommended `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
logs/
*.db
*.csv
```

## Notes

This project is built as a learning project for practicing:

* web scraping
* working with SQLite
* separating business logic from bot logic
* Telegram bot development with aiogram
* working with environment variables
* basic access control
* generating and sending reports

## Status

Project version: `v1`

The current version supports category-based price monitoring, CSV reports, and Telegram commands.
