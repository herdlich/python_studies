n = int(input('Enter length of list: '))
l = []
for i in range(n):
    s = input('Enter a string: ')
    l.append(s)
k = int(input())
for i in range(len(l)):
    if len(l[i]) >= k:  # if length of string is at least k
        print(l[i][k - 1], end='')  # find index k in string
    else:
        continue
