# The script finds the “heaviest” word by summing the Unicode values of all its characters.
# It returns the “heaviest” word.

maximum = 0
s = 0

for i in range(4):
    letter = input('Enter a string: ')

    for j in letter:
        s = sum(ord(i) for i in letter)  # the sum of all characters in Unicode
        if maximum < s:  # the largest number is determined
            maximum = s
            max_letter = letter

print(max_letter)  # in the end, the longest word is printed
