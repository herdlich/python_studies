# This program creates a frame made of stars based on the specified number of rows!
n = int(input('Enter the number of lines: '))
for i in range(1, n + 1):
    if i != 1 and i != n:
        print('*', ' ' * 15, '*')
    else:
        print('*' * 19)
