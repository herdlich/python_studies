# Only those lines in the list that contain the entered word are expanded

n = int(input('Enter the number of strings: '))
l = []
lower_list = []

for i in range(n):
    s = input('Enter a string: ')
    l.append(s)

lower_list = [s.lower() for s in l]  # a new list to track all registers

search = input('Enter a search term: ').lower()
for i in range(len(lower_list)):
    if search in lower_list[i]:  # search for matches
        print(l[i], end='\n')
