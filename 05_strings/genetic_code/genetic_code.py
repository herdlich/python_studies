# The purpose of the exercise: A string is entered. Each of the listed characters will be counted: a, g, c, t (the nitrogenous bases of the genetic code in a molecule).
# For example, if you enter ‘aaggccttAAGGCCTT’, the result will be as follows:
# Adenine: 4
# Guanine: 4
# Cytosine: 4
# Thymine: 4

s = input('Enter string: ')
s = s.lower()
print(
    f'Adenine: {s.count('a')}{'\n'}Guanine: {s.count('g')}{'\n'}Cytosine: {s.count('c')}{'\n'}Thymine: {s.count('t')}')
