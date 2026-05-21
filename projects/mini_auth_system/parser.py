from pathlib import Path

# Path to log file
path_log = Path('logs/app.log')


# Load logs from file
def load_logs():
    try:
        log_list = []

        # Open log file
        with open(path_log, 'r', encoding='utf-8') as f:

            # Read every log line
            for line in f:
                # Remove extra spaces/newline symbols
                log_list.append(line.strip())

            return log_list

    # Handle file reading errors
    except Exception as e:
        return []


# Show all logs
def read_all_logs():
    # Check if log file exists and is not empty
    if path_log.exists() and path_log.stat().st_size > 0:

        # Load logs
        logs = load_logs()

        # Print every log
        for log in logs:
            print(log)
            print('-' * 60)

    else:
        print('No logs found')


# Search logs by level
def level_search():
    # Check if log file exists and contains data
    if path_log.exists() and path_log.stat().st_size > 0:

        # Load logs
        logs = load_logs()

        # User enters log level
        us_level = input('Enter the log level for the search: ').strip().lower()

        # Available log levels
        levels = ['info', 'warning', 'error', 'critical']

        # Validate level input
        if us_level in levels:

            # Iterate through logs
            for log in logs:

                # Remove date part
                clean_line = log[log.find(']') + 1:]

                # Extract log level
                line = clean_line[clean_line.find('-') + 1:clean_line.find(':')].strip()

                # Compare levels
                if us_level == line.lower():
                    print(log)

        else:
            print('An invalid log level has been entered')

    else:
        print('No logs found')

        # Create empty log file
        path_log.touch()


# Search logs by date
def date_search():
    # Check if log file exists and contains data
    if path_log.exists() and path_log.stat().st_size > 0:

        # Load logs
        logs = load_logs()

        # User enters date
        us_date = input('Enter the log date for the search(dd/mm/YYYY): ')

        # Validate date format
        if len(us_date.split('/')) == 3:

            # Iterate through logs
            for log in logs:

                # Extract date from log
                date = log[log.find('[') + 1:log.find(']')].split()

                # Compare dates
                if us_date == date[0]:
                    print(log)

        else:
            print('Please enter a valid date (dd/mm/YYYY): ')

    else:
        print('No logs found')

        # Create empty log file
        path_log.touch()


# Search logs by username
def username_search():
    # Check if log file exists and contains data
    if path_log.exists() and path_log.stat().st_size > 0:

        # Load logs
        logs = load_logs()

        # User enters username
        us_username = input('Enter the username for the search: ')

        # Iterate through logs
        for log in logs:

            # Check if username exists in quotes
            if log.count('"') == 2:

                # Extract username
                clean_line = log[log.find('"') + 1:]
                line = clean_line[:clean_line.find('"')]

                # Compare usernames
                if us_username == line:
                    print(log)

    else:
        print('No logs found')

        # Create empty log file
        path_log.touch()


# Menu actions dictionary
menu_options = {'1': read_all_logs,
                '2': level_search,
                '3': date_search,
                '4': username_search}

# Main parser loop
while True:
    # Parser menu
    print('1. View all logs.\n2. View logs by level.\n3. View logs by date.'
          '\n4. View logs by username.\n5. Exit')

    # User menu input
    user_choice = input('Select an action: ')

    # Execute selected action
    if user_choice in menu_options:
        menu_options[user_choice]()

    # Exit parser
    elif user_choice == '5':
        print('Exiting...')
        break

    # Invalid menu option
    else:
        print('Invalid choice')
