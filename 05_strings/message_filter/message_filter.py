n = int(input('Enter comment: '))
for i in range(1, n + 1):
    s = input()
    if s.isspace() or s == '':
        print(f'{i}: COMMENT SHOULD BE DELETED')
    else:
        print(f'{i}: {s}')