# The script splits the numbers and outputs the number of “+” symbols corresponding to the number

s = input('Enter a string of number: ')
sl = s.split()
for i in range(len(sl)):
    sl[i] = '+' * int(sl[i])
print(*sl, sep='\n')
