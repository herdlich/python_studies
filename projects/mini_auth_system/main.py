from pathlib import Path
import logging
import json

print('Welcome!\n')

# Logging configuration
logging.basicConfig(filename='logs/app.log', level=logging.INFO, encoding='utf-8',
                    format='[%(asctime)s]%(name)s - %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')

# Path to users database
path = Path('users.json')

# Path to log file
app_log = Path('logs/app.log')


# Load data from JSON file
def json_load():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    # Handle JSON/file errors
    except Exception as e:
        logging.error(e)
        return {}


# Save data into JSON file
def save_json(data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# User registration
def reg():
    # Registration validation
    def successful_reg(data):

        # User input data
        user_info = {'username': input('Username: '),
                     'password': input('Password: '),
                     'confirm_password': input('Confirm Password: ')}

        # Password confirmation check
        if user_info['password'] == user_info['confirm_password']:

            # Save user into dictionary
            data[user_info['username']] = user_info

            # Save users into JSON
            save_json(data)

            # Log successful registration
            logging.info(f'User "{user_info['username']}" has been successfully registered')
            print('Registration successful')
            return True

        else:
            # Password mismatch
            print('\nPasswords do not match')
            return False

    # Check if users file exists and is not empty
    if path.exists() and path.stat().st_size > 0:

        # Load users data
        data = json_load()

        # Attempt registration
        reg_is = successful_reg(data)

        if not reg_is:
            return False
        else:
            return True

    # Create new users file
    else:
        path.touch()

        # Register first user
        reg_is = successful_reg({})

        if not reg_is:
            return False
        else:
            return True


# User login
def login():
    # Check if users file exists and contains data
    if path.exists() and path.stat().st_size > 0:

        # Load users data
        data = json_load()
        flag = False

        while True:
            # Username input
            username = input('Username: ')

            # Check username existence
            if username in data:

                # Password input
                us_password = input('Password: ')

                # Password validation
                if us_password == data[username]['password']:

                    # Log successful login
                    logging.info(f'User "{username}" is logged in')
                    print('Successfully logged in\n')
                    break

                else:

                    # Wrong password
                    logging.warning(f'Failed login atempt for "{username}"')
                    print('Wrong password, try again\n')

            else:

                # Invalid username
                logging.warning(f'Login attempt with invalid username "{username}"')
                print('Username or password is incorrect\n')

    else:
        print('User List is empty\n')


# Menu actions dictionary
menu_options = {'1': reg,
                '2': login}

# Main application loop
while True:

    # User menu
    user_choice = input('\n1. Sign up.\n2. Log in. \n3. Exit.\n\nSelect: ')

    # Execute selected action
    if user_choice in menu_options:
        menu_options[user_choice]()

    # Exit program
    elif user_choice == '3':
        break

    # Invalid menu option
    else:
        print('Invalid option\n')
