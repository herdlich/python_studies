import json


def get_user_info():
    user_info = {}

    user_info['name'] = input('Your name?: ')

    user_info['age'] = input('Your age?: ')
    while not user_info['age'].isdigit() or int(user_info['age']) < 0:
        print('Enter a valid age.')
        user_info['age'] = input('Your age?: ')

    user_info['student'] = input('You student? Y/N: ').strip().lower()
    if user_info['student'] == 'y':
        user_info['student'] = True
    elif user_info['student'] == 'n':
        user_info['student'] = False
    else:
        user_info['student'] = None

    user_info['skills'] = input('List your skills: ').split(',')

    goals = input('What are your goals?: ').split(',')
    user_info['goals'] = [item.strip() for item in goals]

    return user_info


def write_json():
    with open('user.json', 'w', encoding='UTF-8') as f:
        user_info = get_user_info()
        json.dump(user_info, f, ensure_ascii=False, indent=4)

    return user_info


def read_json():
    try:
        with open('user.json', 'r', encoding='UTF-8') as f:
            new_data = json.load(f)
            return new_data
    except FileNotFoundError:
        print('File not found.')
        return write_json()


print('Hello! You will now be asked a few questions. Please answer them.')
write_json()
print(read_json())
