def print_symbol_counts(s):
    s = s.lower().replace(' ', '')
    print(s)
    l = [] # an empty list has been created
    for i in s:
        l.append(i) # filling out the list
    l.sort() # sorting letters in lexicographical order
    l2 = [] # creating a second empty list to output one letter at a time
    for i in l:
        if i not in l2: # If the character is not in l2, it is added there
            l2.append(i)
            print(l.count(i))

print_symbol_counts(input('Enter a string: '))