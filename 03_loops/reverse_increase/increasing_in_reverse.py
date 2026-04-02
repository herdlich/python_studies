n = int(input('Enter your number: '))
l = len(str(n))
flag = True  # flag for finding a discrepancy
while n // 10 > 0:
    if n % 10 > n // 10 % 10:  # comparison of last and next last
        flag = False
    n //= 10
if flag:  # remains True if the numbers consecutive
    print('The number increases in reverse order!')
else:
    print('The number does not increase in reverse order')
