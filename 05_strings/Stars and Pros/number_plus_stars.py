# This program counts the number of "+" and "*" characters in a string
s = input('Any set of characters: ')
count_p = 0
count_s = 0
for i in s:
    if '+' in i:
        count_p += 1
    if '*' in i:
        count_s += 1
print(f'The "+" symbol appears {count_p} times', f'The "*" symbol appears {count_s} times', sep='\n')
