#    The program identifies several tasks related to a given number:
# 1. The count of the digit 3 within it
# 2. The number of times its last digit appears within it
# 3. The count of even digits
# 4. The sum of its digits greater than five
# 5. The product of its digits greater than seven
# 6. The number of times the digits 0 and 5 appear within it
n = int(input())
count_three = 0
count_last = n % 10
count_l = 0
count_even = 0
total = 0
product = 1
count_zf = 0
while n > 0:
    last_digit = n % 10
    if last_digit == 3:
        count_three += 1
    if last_digit == count_last:
        count_l += 1
    if last_digit % 2 == 0:
        count_even += 1
    if last_digit > 5:
        total += last_digit
    if last_digit > 7:
        product *= last_digit
    if last_digit == 5 or last_digit == 0:
        count_zf += 1
    n //= 10
print(count_three, count_l, count_even, total, product, count_zf, sep='\n')
