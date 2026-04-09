# The script converts a Unicode number into characters.
# ONLY in the format: [u-“number”]

s = input('Enter a string of Unicode numbers: ')
c = s.count('[')  # number of character calls

for i in range(c):
    prnth_1 = s.find('[u-')
    prnth_2 = s.index(']')
    cress = s[prnth_1 + 3:prnth_2]  # from the start of the first ‘[’ to the start of the first ']'
    s = s.replace('[u-' + cress + ']', chr(int(cress)), 1)
    # Replace a string containing a Unicode number with characters

print(s)
