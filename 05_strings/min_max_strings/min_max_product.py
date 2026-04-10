# Formula: Multiply the maximum and minimum values in the row, then square the result
minimum = '█'
maximum = ''
product = ''
for i in range(4):
    s = input('Enter a string: ')
    # find the maximum and minimum:
    if s > maximum:
        maximum = s
    elif s < minimum:
        minimum = s
product = ord(maximum[-1]) * ord(minimum[-1])
print(product ** 2)
