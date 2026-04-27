import secrets

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation = '!#$%&*+-=?@^_'


def generate_password(count, length, chars):
    passwords = []
    for i in range(count):
        password = ''
        while len(password) < length:
            password += secrets.choice(chars)
        passwords.append(password)
    return passwords


chars = ''

number_password = int(input('Enter the number of passwords: '))
length_password = int(input('Enter the password length: '))

should_digits = input('Do you want digits? [y/n]: ').strip().lower()
should_lowercase = input('Do you want lowercase letters? [y/n]: ').strip().lower()
should_uppercase = input('Do you want uppercase letters? [y/n]: ').strip().lower()
should_punctuation = input('Do you want punctuations? [y/n]: ').strip().lower()

if should_digits == 'y':
    chars += digits
if should_lowercase == 'y':
    chars += lowercase_letters
if should_uppercase == 'y':
    chars += uppercase_letters
if should_punctuation == 'y':
    chars += punctuation

if not chars:
    print('You must choose at least one character type')
else:
    print(*generate_password(number_password, length_password, chars), sep='\n')
