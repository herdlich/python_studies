# The program searches for the desired word in files
# Main drawback: the entire string is converted to lowercase


def file_search(word):
    results = []

    f_1 = open('texts/note1.txt', 'r')
    f_2 = open('texts/note2.txt', 'r')
    f_3 = open('texts/note3.txt', 'r')

    files = {f_1: 'note1.txt', f_2: 'note2.txt', f_3: 'note3.txt'}

    for file in files:
        for line_number, line in enumerate(file, start=1):
            if word.lower() in line.lower():  # match search
                # highlighting the desired word:
                changed_line = line.lower().replace(word.lower(), '<' + word.upper() + '>')
                results.append(f'file: {files[file]}, line: {line_number}: {changed_line.strip()}')

    f_1.close()
    f_2.close()
    f_3.close()

    return results


user_word = input("Enter your word for search: ").strip()

if not user_word:
    print('Search word cannot be empty')
else:
    results = file_search(user_word)

    if results:
        with open('result.txt', 'w') as result_file:
            result_file.write('\n'.join(results))  # saving the results to a separate file
        print(*results, sep='\n')
    else:
        print('No results found')
