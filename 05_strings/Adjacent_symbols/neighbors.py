s = input('Enter a string: ')
count = 0  # to count the number of matching characters
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1  # if the symbols match, counter +1
print(count)
