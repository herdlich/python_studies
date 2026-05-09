from pathlib import Path
import shutil

# Small utility to sort files by extension
# and also restore them back to the main folder
print('Hello. Here you can sort the files by file extension or reverse the sort order.')

# Main working directory
path = Path('files')

# File categories and their related extensions
sort_list = {'Images': ['.jpg', '.jpeg', '.png'],
             'Documents': ['.docx', '.doc', '.pdf', '.txt', '.rtf', '.md'],
             'Archives': ['.zip', '.rar', '.7z'],
             'Audio': ['.mp3', '.wav', '.aac', '.flac'],
             'Videos': ['.mp4', '.avi', '.mkv', '.mov']}

if not path.exists():
    path.mkdir(parents=True, exist_ok=True)


def file_sorter():
    # Creates target folders and moves files there
    # If a file with the same name already exists,
    # adds a number to avoid overwriting
    def paths(file, folder):
        folder_path = path / 'sorted' / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        target = folder_path / file.name

        i = 1
        while target.exists():
            target = folder_path / f'{file.stem}_{i}{file.suffix}'
            i += 1

        shutil.move(file, target)

    # Go through all files in the main folder
    for file in path.iterdir():
        try:
            if file.is_file():

                # Check which category the file belongs to
                for key_str, value in sort_list.items():
                    if file.suffix.lower() in value:
                        # Move file into its category folder
                        paths(file, key_str)

                        break

                # If extension was not found in any category
                # move file into "Other"
                else:
                    paths(file, 'Other')
        except Exception as e:
            print(f'Error in {file.name}: {e}')


def file_unsorter():
    # Create a static list of files first
    # to avoid issues while moving files during iteration
    file_to_move = [f for f in path.rglob('*') if f.is_file() and f.parent != path]
    for file in file_to_move:
        try:
            file_path = path / file.name

            # Prevent overwriting files with the same name
            i = 1
            while file_path.exists():
                file_path = path / f'{file.stem}_{i}{file.suffix}'
                i += 1

            # Move files back into the main folder
            shutil.move(file, file_path)
        except Exception as e:
            print(f'Error in {file.name}: {e}')


# User menu
user_choice = input('Select:\n1. Sort\n2. Unsort\nEnter the option number: ').strip()

if user_choice == '1':
    file_sorter()
elif user_choice == '2':
    file_unsorter()
