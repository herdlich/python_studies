import json
from pathlib import Path

path = Path('note.json')


def load_json():
    with open(path, 'r', encoding='utf-8') as f:
        notes = json.load(f)
        return notes


def user_note():
    note = {}
    note['id'] = int(input('Enter your note ID: '))
    note['title'] = input('Enter your note title: ')
    note['content'] = input('Enter your note content: ')
    return note


def save_json(n):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(n, f, ensure_ascii=False, indent=4)


def add_note():
    note = user_note()

    if path.exists():

        if path.stat().st_size != 0:
            notes = load_json()
            notes.append(note)
            save_json(notes)
        else:
            notes = [note]
            save_json(notes)

    else:
        notes = [note]
        path.touch()

        save_json(notes)


def read_json():
    if path.exists():
        if path.stat().st_size != 0:
            notes = load_json()
            for note in notes:
                print(f"{note['id']}\n{note['title']}\n{note['content']}")
                print('-' * 20)
        else:
            print('File empty.')
    else:
        print('No note found.')


def search_note():
    print()
    if path.exists():
        if path.stat().st_size != 0:
            user_search = input('Enter your note search: ').lower()
            notes = load_json()
            for note in notes:
                if user_search in note['title'].lower():
                    print(f"{user_search} in title, ID {note['id']}.\n{note}")
                if user_search in note['content'].lower():
                    print(f"{user_search} in content, ID {note['id']}.\n{note}")
                print('-' * 20)
        else:
            print('File empty.')
    else:
        print('No note found.')


def delete_note():
    print()
    if path.exists():
        if path.stat().st_size != 0:
            notes = load_json()
            user_del = int(input('Enter your ID to delete: '))
            for note in notes:
                if user_del == note['id']:
                    notes.remove(note)
                    print('The post has been deleted.')
                    break

            save_json(notes)
        else:
            print('File empty.')
    else:
        print('No note found.')


while True:
    user_menu = input('1. Create a record.\n2. Read a record. \n3. Search.\n4. Delete a record\nEnter the number: ')

    if user_menu == '1':
        add_note()
    elif user_menu == '2':
        read_json()
    elif user_menu == '3':
        search_note()
    elif user_menu == '4':
        delete_note()

    print()
    user_next = input('Would you like to make any other changes to the file?\nEnter y/n: ').strip().lower()
    print()
    if user_next == 'n':
        break
