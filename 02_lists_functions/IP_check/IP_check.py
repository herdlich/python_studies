# The script checks whether the entered IP address is valid.
# Condition: the number must be between 0 and 255.

s = input('Enter the IP address: ')
sl = s.split('.')
flag = 'YES'
for i in sl:
    if not (0 <= int(i) <= 255):
        flag = 'NO'
        break
print(flag)
