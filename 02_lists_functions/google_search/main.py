n = int(input('Enter the number of strings: '))
string_list = []
searching_list = []

for i in range(n):
    request = input('Enter string: ')
    string_list.append(request)

k = int(input('Enter the number of words to search for: '))
for j in range(k):
    search_s = input('Enter a word: ')
    searching_list.append(search_s)

for strings in string_list:
    flag = True  # The string will be displayed if all the words are found
    for l in range(k):
        if searching_list[l].lower() not in strings.lower():  # Checking if all words are present in a single string
            flag = False
    if flag:
        print(strings)
