# This script finds the next prime number, starting from the entered number (excluding the number itself)
# Since a prime number is divisible only by 1 and itself,
# we are looking for a number with `count == 2` (2 divisors within the number's range)

def get_next_prime(num):
    for i in range(num + 1, num * 10):  # a range from num (exclusive) to num * 10
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:  # As soon as a prime number is found, the function will terminate
            return i

    return False  # if there happens to be no prime numbers


n = int(input())
print(get_next_prime(n))
