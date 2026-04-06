s = input('Enter string: ')
count = 0
digits = '1234567890'
for i in s:
    if i in digits:
        count += 1  # counting the number of digits in string
print(count)
