n = int(input('Enter a number of strings: '))
l = []
for i in range(n):
    s = input('Enter a string: ')
    if s not in l:
        l.append(s)
print(*l, sep='\n')