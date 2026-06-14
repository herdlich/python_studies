from pathlib import Path
from datetime import datetime
import json
import logging

exp_path = Path("expenses.json")
balance_path = Path("monthly_balance.json")

time_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(filename="app.log", level=logging.INFO, format="[%(asctime)s] - %(levelname)s: %(message)s",
                    datefmt=time_format)

CATEGORIES = {"1": "shopping",
              "2": "products",
              "3": "clothing",
              "4": "marketplace",
              "5": "subscribes"}

MONTHS = {
    "01": "january",
    "02": "february",
    "03": "march",
    "04": "april",
    "05": "may",
    "06": "june",
    "07": "july",
    "08": "august",
    "09": "september",
    "10": "october",
    "11": "november",
    "12": "december"
}


def json_load(file):
    try:
        with file.open("r", encoding="utf-8") as f:
            return json.load(f)

    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_json(data, file):
    with file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def add_expense():
    exp_data = json_load(exp_path)
    blnc_data = json_load(balance_path)

    date = input("Date(dd.mm.yyyy): ")

    try:
        parsed_date = datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
        print("Invalid date")
        return

    try:
        expense = int(input("Expense: "))
    except ValueError:
        print("Invalid expense")
        return

    if expense <= 0:
        print("Expense must be greater than 0")
        return

    month_number = parsed_date.strftime("%m")
    blnc_month = MONTHS[month_number]

    if "month" not in blnc_data:
        print("Balance file has no 'month' section")
        return

    if blnc_month not in blnc_data["month"]:
        print(f"Balance for {blnc_month} not found")
        return

    if "balance" not in blnc_data["month"][blnc_month]:
        print(f"Balance value for {blnc_month} not found")
        return

    balance = blnc_data["month"][blnc_month]["balance"]

    if balance < expense:
        print("Not enough balance")
        return

    category = input(
        "1. Shopping\n"
        "2. Products\n"
        "3. Clothing\n"
        "4. Marketplace\n"
        "5. Subscribes\n"
        "Choice: "
    ).strip()

    if category not in CATEGORIES:
        print("Invalid category")
        return

    description = input("Description: ")

    new_balance = balance - expense

    exp_data.setdefault("expenses", {})
    exp_data["expenses"].setdefault(date, [])
    exp_data["expenses"][date].append({"expense": expense,
                                       "category": CATEGORIES[category],
                                       "description": description})

    blnc_data["month"][blnc_month]["balance"] = new_balance

    save_json(exp_data, exp_path)
    save_json(blnc_data, balance_path)

    print("Expense added")
    logging.info(f"Expense added. Balance: {new_balance}")


def add_balance():
    data = json_load(balance_path)

    user_month = input("Enter month(mm): ").strip()

    if not (user_month.isdigit() and len(user_month) == 2 and user_month in MONTHS):
        print("Invalid month")
        return

    month_name = MONTHS[user_month]

    try:
        user_add_balance = int(input("Balance for add: "))
    except ValueError:
        print("Invalid balance")
        return

    if user_add_balance <= 0:
        print("Balance must be greater than 0")
        return

    data.setdefault("month", {})
    data["month"].setdefault(month_name, {"balance": 0})

    data["month"][month_name]["balance"] += user_add_balance

    save_json(data, balance_path)

    print("Balance has been updated")
    logging.info(f"Balance in {month_name} has been updated")


def check_balance():
    data = json_load(balance_path)

    user_month = input("Enter month(mm): ").strip()

    if not (len(user_month) == 2 and user_month.isdigit() and user_month in MONTHS):
        print("Invalid month")
        return

    month_name = MONTHS[user_month]

    if "month" not in data or month_name not in data["month"]:
        print("Month not found")
        return

    if "balance" not in data["month"][month_name]:
        print("Balance not found")
        return

    month_balance = data["month"][month_name]["balance"]

    print(f"Balance for {month_name}: {month_balance}")


def show_all_expenses():
    data = json_load(exp_path)
    expenses = data.get("expenses", {})

    if not expenses:
        print("No expenses found")
        return

    for date, expense_list in expenses.items():
        print(f"\nDate: {date}")

        for expense in expense_list:
            amount = expense["expense"]
            category = expense["category"]
            description = expense["description"]
            print(f"–{amount} | {category} | {description}")


def show_expense_by_date():
    data = json_load(exp_path)

    expenses = data.get("expenses", {})

    user_date = input("Enter the date(dd.mm.yyyy): ").strip()

    try:
        datetime.strptime(user_date, "%d.%m.%Y")
    except ValueError:
        print("Invalid date")
        return

    if user_date not in expenses:
        print("Invalid date")
        return

    print(f"\nDate: {user_date}")

    for expense in expenses[user_date]:
        amount = expense["expense"]
        category = expense["category"]
        description = expense["description"]

        print(f"–{amount} | {category} | {description}")


def show_last_expenses(digit):
    pass


def show_highest_expense():
    pass


def show_expense_by_category():
    pass


# TODO: finish expense checking menu
def check_expenses():
    user_choice = input("1. Show all expenses\n"
                        "2. Show expenses by date\n"
                        "3. Show last expenses\n"
                        "4. Show the highest expense\n"
                        "5. Show expenses by category").strip()

    if user_choice == "1":
        show_all_expenses()

    elif user_choice == "2":
        show_expense_by_date()

    elif user_choice == "3":
        try:
            user_digit = int(input("Enter the number of recent expenses: "))
        except ValueError:
            print("Invalid number")
            return

        if user_digit <= 0:
            print("Invalid number")
            return

        show_last_expenses(user_digit)

    elif user_choice == "4":
        show_highest_expense()

    elif user_choice == "5":
        show_expense_by_category()

    else:
        print("Invalid choice")
        return


menu_option = {"1": add_expense,
               "2": add_balance,
               "3": check_balance}

while True:
    user_choice = input("1. Add expense\n"
                        "2. Add balance\n"
                        "3. Check Balance\n"
                        "4. Exit\n"
                        "Choice: ").strip()

    if user_choice in menu_option:
        menu_option[user_choice]()

    elif user_choice == "4":
        break

    else:
        print("Invalid choice")
