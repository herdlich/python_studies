# 🐍 Python Studies

A comprehensive personal learning repository documenting my Python journey through structured exercises, parsing techniques, file operations, and practical mini-projects.

---

## 📂 Repository Structure

```
python_studies/
│
├── 01_basics/                    # Core Python fundamentals
├── 02_lists_functions/           # Lists, functions, and parameters
├── 03_loops/                     # Iteration (for, while)
├── 04_conditionals/              # Decision-making (if, elif, else)
├── 05_strings/                   # String manipulation and formatting
├── 06_oop/                       # Object-oriented programming basics
├── 07_parsing/                   # HTML and data parsing techniques
├── 08_files/                     # File operations and data processing
├── projects/                     # Practical mini-projects
└── README.md
```

---

## 🎓 Learning Modules

### `01_basics/`
Core Python concepts:
- Variables and data types
- Input/output operations
- Basic syntax and operators

### `02_lists_functions/`
Working with lists and functions:
- List creation and manipulation
- List methods (append, extend, sort, etc.)
- Function definition and parameters
- Return values and scope

### `03_loops/`
Iteration techniques:
- `for` loops
- `while` loops
- Loop control (break, continue)
- Nested loops

### `04_conditionals/`
Decision-making constructs:
- `if`, `elif`, `else` statements
- Logical operators (and, or, not)
- Comparison operators
- Ternary operators

### `05_strings/`
String operations and techniques:
- Indexing and slicing
- String methods (upper, lower, split, join, etc.)
- String formatting (f-strings, format())
- Regular expressions basics

### `06_oop/`
Introduction to object-oriented programming:
- Classes and objects
- Attributes and methods
- Constructors (`__init__`)
- Inheritance basics

### `07_parsing/`
Data parsing and extraction:
- **local_html_parser** — Parse HTML from local files using BeautifulSoup
- **local_pagination_parser** — Handle paginated HTML structures

### `08_files/`
File handling and data processing:
- **csv_basics** — CSV file fundamentals
- **csv_parser** — Parse and extract data from CSV files
- **csv_merger** — Combine multiple CSV files
- **csv_stats_tool** — Analyze and generate statistics from CSV data
- **log_manager** — Read and process log files
- **mirror_list** — Create file system mirrors and listings
- **stop_words** — Filter and process text with stop word removal
- **user_info** — Read and organize user-related data

---

## 🚀 Projects

### Web Scraping & API Integration
- **books_parser** — Scrape book data from Books to Scrape using requests & BeautifulSoup
- **product_parser** — Extract product information from e-commerce sites
- **python_jobs_parser** — Collect Python job listings from job boards
- **hn_api_parser** — Parse Hacker News API data
- **hn_news_watcher** — Monitor and track Hacker News stories
- **price_monitor** — Track price changes across websites
- **price_monitor_api** — REST API for price monitoring with persistence

### Games & Entertainment
- **caesar_cipher** — Encrypt text using Caesar cipher (English & Russian)
- **guess_number** — Interactive number guessing game
- **hangman** — Word guessing game with tries system
- **magic_8_ball** — Fortune telling game with random responses

### Utilities & Tools
- **file_sorter** — Organize files by extension into directories
- **file_sorter_and_unsorter** — Sort and restore original file structure
- **text_searcher** — Search text patterns in files
- **password_generator** — Generate secure random passwords

### Data Management
- **expense_tracker** — Track and manage personal expenses (v1)
- **expense_tracker_2_0** — Enhanced expense tracker with improved features
- **task_manager** — Create, update, and manage tasks
- **notes_manager_json** — Store and organize notes in JSON format

### Security & Authentication
- **mini_auth_system** — Simple user authentication and authorization system

### Telegram Bot
- **telegram_price_bot** — Telegram bot for price monitoring and notifications

---

## ▶️ Quick Start

### Running Individual Exercises
Each exercise file can be run directly with Python:

```bash
python 03_loops/working_with_numbers.py
python 05_strings/string_methods.py
```

### Running Projects
Most projects have their own README with specific instructions. For example:

```bash
# Caesar Cipher
cd projects/caesar_cipher
python main.py

# Books Parser (requires dependencies)
cd projects/books_parser
pip install -r requirements.txt
python main.py --pages 10 --output books.csv

# Expense Tracker
cd projects/expense_tracker_2_0
python main.py
```

### Dependencies
Some projects require external libraries:

```bash
# For web scraping projects
pip install requests beautifulsoup4

# For API projects
pip install requests

# For Telegram bot
pip install python-telegram-bot

# For file operations
# (mostly use Python standard library)
```

---

## 🎯 Purpose

This repository helps me:
- 📚 Master Python fundamentals and advanced concepts
- 🏗️ Build and understand project structures
- 🔧 Practice real-world programming patterns
- 💡 Develop problem-solving skills
- 📈 Track learning progress over time
- 🎨 Explore diverse Python applications

---

## 📝 Topics

`python` `python-learning` `exercises` `beginner-projects` `oop` `algorithms`

---

## 📌 Notes

- This repository is actively maintained as part of my ongoing learning journey
- Code quality and structure improve as I progress
- Each project is a practical application of learned concepts
- Feel free to use these examples for your own learning

---

## 👤 Author

**herdlich** — Continuous learner passionate about Python development

Created: March 2026 | Last Updated: July 2026
