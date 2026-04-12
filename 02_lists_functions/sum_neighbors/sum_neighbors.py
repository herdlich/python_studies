n = int(input('Enter the length of list: '))
l = []
s = int(input('Enter a number: '))
for i in range(n - 1):
    old_el = s  # keep the old number
    s = int(input('Enter a number: '))
    l.append(s + old_el)  # new amount is added to the previous one
print(l)
