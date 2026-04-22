def is_prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


n = int(input())
print(is_prime(n))
