# Comparison of strings without considering non-alphabetic characters or case.
# This script uses the English alphabet.
# You can add any other alphabet by replacing in lines 8 and 11 with “or el in your_alphabet”.

s1, s2 = input('Enter a string 1: '), input('Enter a string 2: ')
f_s1 = ''
f_s2 = ''
s1, s2 = s1.lower(), s2.lower()
alphabet_e = 'abcdefghijklmnopqrstuvwxyz'

for el in s1:
    if el in alphabet_e:
        f_s1 += el
for el in s2:
    if el in alphabet_e:
        f_s2 += el

if f_s1 == f_s2 and len(f_s1) == len(f_s2):
    print('YES')
else:
    print('NO')
