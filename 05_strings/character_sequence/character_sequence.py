a, b = int(input('Enter first number: ')), int(input('Enter second number: '))
count = 0
for i in range(a, b + 1):
    print(chr(ord(chr(a)) + count), end=' ')
    count += 1