# Expense Tracker 2.0

A simple command-line expense tracker written in Python.

The project allows users to add monthly balances, record expenses, check the current balance for a selected month, and store data in JSON files. It also includes basic input validation and logging.

## Features

* Add balance for a selected month
* Add expenses with:

  * date
  * amount
  * category
  * description
* Check balance by month
* Save expenses to `expenses.json`
* Save monthly balances to `monthly_balance.json`
* Log successful operations to `app.log`
* Validate user input:

  * date format
  * expense amount
  * month format
  * category selection
  * available balance

## Project Structure

```text
expense_tracker_2_0/
│
├── main.py
├── expenses.json
├── monthly_balance.json
├── app.log
└── README.md
```

## Data Storage

The project uses JSON files for simple persistent storage.

### `monthly_balance.json`

Example structure:

```json
{
    "month": {
        "june": {
            "balance": 10000
        },
        "july": {
            "balance": 5000
        }
    }
}
```

### `expenses.json`

Example structure:

```json
{
    "expenses": {
        "14.06.2026": [
            {
                "expense": 3500,
                "category": "products",
                "description": "Groceries"
            }
        ]
    }
}
```

## Main Menu

When the program starts, the user can choose one of the following actions:

```text
1. Add expense
2. Add balance
3. Check Balance
4. Exit
```

## How It Works

### Add Balance

The user enters a month in `mm` format and the amount to add.

Example:

```text
Enter month(mm): 06
Balance for add: 10000
```

If the month does not exist in the JSON file yet, the program creates it automatically.

### Add Expense

The user enters:

```text
Date(dd.mm.yyyy): 14.06.2026
Expense: 3500
```

The program checks:

* whether the date is valid
* whether the expense is a positive number
* whether the selected month has a balance
* whether the balance is enough for the expense

Then the user selects a category:

```text
1. Shopping
2. Products
3. Clothing
4. Marketplace
5. Subscribes
Choice:
```

If the expense is valid, it is saved to `expenses.json`, and the monthly balance is updated.

### Check Balance

The user enters a month in `mm` format.

Example:

```text
Enter month(mm): 06
Balance for june: 6500
```

## Logging

Successful balance and expense operations are written to `app.log`.

Example log entry:

```text
[2026-06-14 15:30:22] - INFO: Expense added. Balance: 6500
```

## Technologies Used

* Python
* `pathlib`
* `datetime`
* `json`
* `logging`

## Current Status

This is a learning project.

Implemented:

* adding expenses
* adding balance
* checking balance
* JSON storage
* basic validation
* logging

In progress:

* viewing all expenses
* viewing expenses by date
* viewing last expenses
* viewing the highest expense
* viewing expenses by category

## Future Improvements

Possible next steps:

* finish the expense checking menu
* add better error handling for missing or corrupted JSON data
* add category-based reports
* add monthly summaries
* add total expenses by category
* migrate from JSON to SQLite
* create a simple CLI command system
* add tests
* improve project structure by splitting logic into separate files

## How to Run

Run the project with:

```bash
python main.py
```

Make sure Python is installed and that the script is launched from the project directory.

## Notes

This project is intended for practicing Python fundamentals:

* functions
* dictionaries
* JSON files
* input validation
* file handling
* basic application structure
* logging
