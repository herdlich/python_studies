# Removes the maximum and minimum numbers from the list

n = int(input('Enter a number of digits: '))
l = []
maximum = 0
minimum = 9999

for i in range(n):
    digit = int(input('Enter a number: '))
    l.append(digit)
    if digit < minimum:
        minimum = digit
    if digit > maximum:
        maximum = digit
l_2 = []
for i in l:
    if i == minimum or i == maximum:
        continue
    l_2.append(i)

print(*l_2, sep='\n')
