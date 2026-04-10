# Find the maximum and minimum strings up to the stopword
maximum = None
minimum = None
s = input('Enter a string: ')
while s != 'END':
    if maximum == None or s > maximum:
        maximum = s
    if minimum == None or s < minimum:
        minimum = s
    s = input('Enter a string: ')
print(f'''Maximum string: {maximum}
Minimum string: {minimum}''')