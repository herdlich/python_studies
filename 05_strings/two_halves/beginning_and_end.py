# The program writes the second half of the line first, and then the first half
s = input('Enter string: ')
l = len(s) // 2
print(s[-l:] + s[0:-l])