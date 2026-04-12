# Display a list of negative, zero and positive numbers

n = int(input('Enter the number of digits: '))
neg_n = []
zero_n = []
pos_n = []

for i in range(n):
    number = int(input('Enter a number: '))
    if number < 0:
        neg_n.append(number)
    elif number == 0:
        zero_n.append(number)
    else:
        pos_n.append(number)

print(*neg_n, *zero_n, *pos_n, sep='\n')