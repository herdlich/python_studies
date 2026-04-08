letter = input('Enter a letter: ')
for i in range(27):
    if chr(ord(letter) + i - 1) != 'Z':
        print(chr(ord(letter) + i))
    else:
        print('There are no more letters')
        break