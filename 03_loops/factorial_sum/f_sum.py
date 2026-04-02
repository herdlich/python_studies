from math import factorial

n = int(input())
sum = 0  # summation of factorials
for i in range(1, n + 1):
    fctrl = factorial(i)
    sum += fctrl
print(sum)
