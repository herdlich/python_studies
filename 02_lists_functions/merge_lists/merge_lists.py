def quick_merge(n):
    l = []
    # The line is split into a list and appended to the main list
    for i in range(n):
        s = input().split()
        l.extend(s)
    for j in range(len(l)):
        l[j] = int(l[j])

    l.sort()
    return l


n = int(input('Enter the number of rows: '))
print(*quick_merge(n))
