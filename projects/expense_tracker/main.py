from pathlib import Path
import datetime
import json

# Path to the JSON file
path = Path('expenses.json')

# Welcome message and available actions
print('''Welcome to the Expense Tracker. Here are the available features:
1. Add an expense entry.
2. View all entries.
3. Search for an entry by category or by a keyword in the description.
4. View the total amount of expenses and the amount for a specific category.
5. Delete an entry by ID.''')

print()


# Load data from JSON file
def json_load():
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    # Handle invalid or corrupted JSON
    except json.JSONDecodeError:
        print('Invalid JSON file')
        return []


# Save data into JSON file
def save_json(jl):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(jl, f, indent=4, ensure_ascii=False)


# Create expense entry dictionary
def expense_data():
    expense = {}

    # Generate ID automatically
    if path.exists():
        # First expense in file
        if path.stat().st_size == 0:
            expense['id'] = 1
        # Continue ID sequence
        else:
            data = json_load()
            last_id = data[-1]['id'] + 1
            expense['id'] = last_id
    # Create file if it doesn't exist
    else:
        path.touch()
        expense['id'] = 1

    # User expense input
    expense['amount'] = float(input('Enter amount of the expense: '))
    expense['category'] = input('Enter category of the expense: ')
    expense['description'] = input('Enter description of the expense: ')
    # Current date and time
    expense['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    return expense


# Print one formatted expense entry
def print_expense(expense):
    print(
        f'ID: {expense["id"]}\nAmount: {expense["amount"]}\nCategory: {expense["category"]}'
        f'\nDescription: {expense["description"]}\nDate: {expense["date"]}')
    print("-" * 20)


# Add new expense into JSON
def add_expense():

    # Create expense data
    data = expense_data()

    # If file already contains data
    if path.exists() and path.stat().st_size != 0:
        expenses = json_load()

        # Add new expense
        expenses.append(data)

        # Save updated list
        save_json(expenses)

    # First expense in file
    else:
        expenses = [data]
        save_json(expenses)


# Show all expenses
def show_expenses():
    # Check if file exists and is not empty
    if path.exists() and path.stat().st_size != 0:
        expenses = json_load()

        # Print every expense
        for expense in expenses:
            print_expense(expense)

    else:
        print('No expenses found')


# Search expenses
def filter_expenses():
    # Check if file exists and contains data
    if path.exists() and path.stat().st_size != 0:
        data = json_load()

        # User chooses search type
        user_input = input('Select:\n1. Filter by category\n2. Filter by keyword in the description\nEnter: ')

        # Search by category
        if user_input == '1':
            user_category = input('Enter category of the expense: ')
            matches = 0

            for expense in data:

                # Case-insensitive search
                if user_category.lower() in expense['category'].lower():
                    matches += 1
                    print_expense(expense)

            # No matches found
            if matches == 0:
                print('Category not found')

        # Search by keyword in description
        elif user_input == '2':
            user_string = input('Enter a search term: ')
            matches = 0

            for expense in data:
                # Case-insensitive search
                if user_string.lower() in expense['description'].lower():
                    matches += 1
                    print_expense(expense)

            # No matches found
            if matches == 0:
                print('String not found')

        else:
            print('Select 1 or 2')

    else:
        print('No expenses found')


# Show expense statistics
def show_total():
    # Check if file exists and contains data
    if path.exists() and path.stat().st_size != 0:
        data = json_load()
        total_amount = 0

        # Statistics menu
        user_input = input('Select:\n1. Total expenses.\n2. Expenses by category.\nEnter: ')

        # Total expenses
        if user_input == '1':
            for expense in data:
                total_amount += expense['amount']

            print(f'Total amount: {total_amount}')

        # Expenses by category
        elif user_input == '2':
            matches = 0
            user_category = input('Enter category of the expense: ')
            for expense in data:
                # Category match
                if user_category.lower() in expense['category'].lower():
                    matches += 1
                    total_amount += expense['amount']

            # Category not found
            if matches == 0:
                print('Category not found')
            else:
                print(f'Expenses in the {user_category} category: {total_amount}')

    else:
        print('No expenses found')


# Delete expense by ID
def delete_expense():
    # Check if file exists and contains data
    if path.exists() and path.stat().st_size != 0:
        data = json_load()

        # User enters ID
        user_input = int(input('Enter the ID to delete: '))
        matches = 0

        # Search for matching ID
        for expense in data:
            if user_input == expense['id']:
                matches += 1

                # Remove expense
                data.remove(expense)
                break

        # Save updated data
        if matches > 0:
            print('Successfully deleted!')
            save_json(data)
        else:
            print('ID not found')

    else:
        print('No expenses found')



# Main application loop
while True:
    # User action menu
    user_input = input('Select an action: ')

    # Add expense
    if user_input == '1':
        add_expense()

    # Show all expenses
    elif user_input == '2':
        show_expenses()

    # Search expenses
    elif user_input == '3':
        filter_expenses()

    # Show statistics
    elif user_input == '4':
        show_total()

    # Delete expense
    elif user_input == '5':
        delete_expense()

    # Continue program or exit
    us_continue = input('Would you like to perform another action? y/n: ').strip().lower()

    if us_continue != 'y':
        break