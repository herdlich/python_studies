from pathlib import Path
import shutil

# Base folder containing unsorted files
path = Path('files')

# Dictionary of file categories and their extensions
extensions = {'Images': ['.jpg', '.jpeg', '.png'],
              'Documents': ['.docx', '.doc', '.pdf', '.txt', '.rtf', '.md'],
              'Archives': ['.zip', '.rar', '.7z'],
              'Audio': ['.mp3', '.wav', '.aac', '.flac'],
              'Videos': ['.mp4', '.avi', '.mkv', '.mov']}


def sort_files():
    # Base folder where sorted files will be placed
    sorted_path = path / 'sorted'

    # Iterate over all items in the 'files' folder
    for file in path.iterdir():
        print(file) # Debug: show current file being processed

        # Only process files, skip directories
        if file.is_file():

            # Loop through categories to find the matching extension
            for key_str, values in extensions.items():

                # Check if the file extension matches the current category
                if file.suffix.lower() in values:

                    # Folder path for the current category
                    path_mkdir = sorted_path / key_str

                    # Create the folder if it does not exist
                    path_mkdir.mkdir(exist_ok=True)

                    # Full target path for the file in the category folder
                    target_file = path_mkdir / file.name

                    # Check if a file with the same name already exists
                    i = 1
                    while target_file.exists():
                        # If it exists, append a number to the filename (_1, _2, etc.)
                        target_file = path_mkdir / f'{file.stem}_{i}{file.suffix}'
                        i += 1
                    # Move the file to the target path
                    shutil.move(file, target_file)

                    # File has been moved, stop checking other categories
                    break
            else:
                # If no category matched, place the file in 'Other'
                path_mkdir = sorted_path / 'Other'
                target_file = path_mkdir / file.name
                path_mkdir.mkdir(exist_ok=True) # Create folder if missing

                # Check for name conflicts in 'Other'
                i = 1
                while target_file.exists():
                    target_file = path_mkdir / f'{file.stem}_{i}{file.suffix}'
                    i += 1

                # Move the file to 'Other'
                shutil.move(file, target_file)

# Run the sorting function
sort_files()
