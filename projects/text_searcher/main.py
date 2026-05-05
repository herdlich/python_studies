from pathlib import Path

user_search = input('Enter a search term: ')
path = Path('texts')  # path to the folder with input files


def text_search(word):
    global_count = 0  # total matches across all files

    if not path.exists():  # check if folder exists before processing
        print('Folder does not exist')
        return

    with open('results.txt', 'w', encoding='utf-8') as out:
        for file in path.glob('*.txt'):  # iterate over all .txt files in folder
            try:
                count_matches = 0  # matches within current file

                with open(file, 'r', encoding='utf-8') as f:
                    # read file line by line with line numbers
                    for i, line in enumerate(f, 1):
                        # case-insensitive search
                        if word.lower() in line.lower():
                            count_matches += 1
                            global_count += 1

                            # write filename only once (on first match in file)
                            if count_matches == 1:
                                out.write(f'{file.name}:\n')
                                print(f'\n{file.name}:')  # separate files in console output

                            # write matched line (strip to control newline formatting)
                            out.write(f'{i} line: {line.strip()}\n')
                            print(f'{i} line: {line.strip()}')

                # write summary for current file if any matches were found
                if count_matches > 0:
                    out.write(f'Matches: {count_matches}\n\n')

            except Exception as e:
                # handle file read errors without crashing entire program
                print(f'Error in {file.name}: {e}')

        # final summary across all files
        out.write(f'Total number of matches: {global_count}')


text_search(user_search)
