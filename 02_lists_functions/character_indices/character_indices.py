def find_all(target, symbol):
    l = []
    target = list(target)

    for i in range(len(target)):
        if target[i] == symbol:
            l.append(target.index(target[i]))
            target[i] = ' '
    return l

s = input('Enter a string: ')
char = input('Enter a character: ')

print(find_all(s, char))