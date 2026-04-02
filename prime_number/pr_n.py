n1, n2 = (int(input()) for _ in range(2))

for i in range(n1, n2 + 1):  # number range
    is_prime = True
    for j in range(2, i):  # range: is it divisible by numbers other than itself and 1?
        if i % j == 0:
            is_prime = False  # if yes - false
            break
    if is_prime and i != 1:  # if no and not equal to 1 - print
        print(i)
