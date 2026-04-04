n = int(input('Enter number: '))
while n > 9:
    sum = 0
    while n > 0:
        last_digit = n % 10
        sum += last_digit
        n //= 10
    n = sum
print(n)