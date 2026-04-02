n = int(input('Enter your number: '))
maximum = 0
minimum = 9
l = len(str(n))
for i in range(1, l + 1):
    if maximum < n % 10:
        maximum = n % 10
    if minimum > n % 10:
        minimum = n % 10
    n //= 10
if maximum != minimum:
    print("NO same")
else:
    print("YES")