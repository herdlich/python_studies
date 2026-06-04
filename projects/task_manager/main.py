from pathlib import Path
import logging
import json

path = Path('task.json')
Path('logs').mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename='logs/app.log', level=logging.INFO, encoding='utf-8')


def json_load():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    except FileNotFoundError:
        logging.error('FileNotFoundError')
        return {}


def save_json(data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        logging.error(e)


def load_tasks():
    if not path.exists() or path.stat().st_size == 0:
        return {}

    return json_load()


def print_task(task_id, task_info):
    print(f'ID: {task_id} ')
    print(f'Title: {task_info["title"]}\n'
          f'Description: {task_info["description"]}\n'
          f'Priority: {task_info["priority"]}\n'
          f'Status: {task_info["status"]}\n'
          f'Date: {task_info["date"]}')
    print('-' * 60)


def add_task():
    data = load_tasks()

    if data:
        last_id = max(map(int, data.keys()))
        new_id = str(last_id + 1)
    else:
        new_id = '1'

    priority = input('Set a priority:\n1. Low\n2. Medium\n3. High\nEnter:')

    priorities = {'1': 'Low', '2': 'Medium', '3': 'High'}

    if priority not in priorities:
        print('Invalid priority')
        return

    status = input('Set a status\n1. Todo\n2. In progress\n 3. Done\nEnter: ')
    statuses = {'1': 'todo', '2': 'in_progress', '3': 'done'}
    if status not in statuses:
        print('Invalid status')
        return

    data[new_id] = {'title': input('Enter a title: '), 'description': input('Enter a description: '),
                    'priority': priorities[priority],
                    'status': statuses[status],
                    'date': input('Enter a date: ')}


    save_json(data)
    logging.info(f'Added task ID {new_id}')
    print('Task added!')


def read_task():
    data = load_tasks()

    if data:
        for task_id, task_info in data.items():
            print_task(task_id, task_info)

    else:
        logging.error('No tasks found')
        return


def delete_task():
    data = load_tasks()

    if data:
        user_delete = input('Enter the ID to delete: ')

        if user_delete in data:
            deleted_task_info = data[user_delete]
            del data[user_delete]
            save_json(data)
            print('Task deleted!')

            logging.info(f'Deleted task ID {user_delete}: {deleted_task_info}')

        else:
            print('ID not found')

    else:
        logging.error('No tasks found')
        return


def search_task():
    data = load_tasks()

    if data:
        user_search = input('Enter a search query: ').strip().lower()

        for task_id, task_info in data.items():
            title = task_info.get('title', '').lower()
            description = task_info.get('description', '').lower()

            if user_search in title or user_search in description:
                logging.info(f'User query found in {task_id} ID: "{user_search}"')
                print(f'ID {task_id}:\n{task_info}')

    else:
        logging.error('No tasks found')
        return


def change_status():
    data = load_tasks()

    if data:
        user_id = input('Enter a ID: ')

        if user_id in data:
            new_status = input('Set a status\n1. Todo\n2. In progress\n 3. Done\nEnter: ')
            statuses = {'1': 'todo', '2': 'in_progress', '3': 'done'}

            if new_status not in statuses:
                print('Invalid status')
                return

            data[user_id]['status'] = statuses[new_status]

            save_json(data)
            logging.info(f'Changed status: - {data[user_id]["status"]}')
            print('Status updated!')

        else:
            print('ID not found')
            return

    else:
        logging.error('No tasks found')
        return


def filter_priority():
    data = load_tasks()

    if data:
        user_priority = input('Enter the priority to search for: ')

        for task_id, task_info in data.items():
            if task_info['priority'] == user_priority:
                print_task(task_id, task_info)

    else:
        logging.error('No tasks found')
        return


def filter_status():
    data = load_tasks()

    if data:
        user_status = input('Enter the status to filter for: ')

        for task_id, task_info in data.items():
            if task_info['status'] == user_status:
                print_task(task_id, task_info)

    else:
        logging.error('No tasks found')
        return


menu_options = {'1': add_task, '2': read_task, '3': delete_task, '4': search_task, '5': change_status,
                '6': filter_priority, '7': filter_status}

while True:
    user_choice = input(
        '1. Add task\n'
        '2. Read task\n'
        '3. Delete task\n'
        '4. Search task\n'
        '5. Change status\n'
        '6. Filter priority\n'
        '7. Filter status\n'
        '8. Exit\n'
        'Enter: ')

    if user_choice in menu_options:
        menu_options[user_choice]()

    elif user_choice == '8':
        break

    else:
        print('Invalid option')
