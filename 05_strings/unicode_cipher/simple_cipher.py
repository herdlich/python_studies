s = input('Enter a string: ')
l = len(s)
for i in s:
    print(ord(chr(ord(i))), end=' ')