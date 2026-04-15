# This script removes comments in a line

n = int(input('Enter the number of string lines: '))
l = []

for i in range(n):
    s = input('Enter the string: ')
    if "#" in s:
        s = s[:s.find('#')]
    s = s.rstrip()
    l.append(s)
print(*l, sep='\n')