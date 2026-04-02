a, b = (int(input()) for _ in range(2))
best_number = None
sum_dividers = 0
max_sum = 0

for i in range(a, b + 1):  # range of entered number
    sum_dividers = 0  # prime sum of divisors
    for j in range(1, i + 1):
        if i % j == 0:
            sum_dividers += j  # If i is divisible, the divisors are summed
    if sum_dividers >= max_sum:
        max_sum = sum_dividers  # maintain maximum results
        best_number = i  # a number whose divisors are summed

print(best_number, max_sum)
