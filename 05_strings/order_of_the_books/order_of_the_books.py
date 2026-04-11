# Checks whether the entered authors and books are sorted in ascending order.
# Format: <author's last name> <author's initials>, “<book title>”

n = int(input('Enter a number: '))
s1 = input('Enter a string: ')
count = 0
answer = 'YES'

while count < n - 1:
    s2 = input('Enter a string: ')

    if s2[0:s2.find(' ')] > s1[0:s1.find(' ')]:
        # If the current value is greater than the previous one, the sequence is in ascending order
        s1 = s2  # The next value of s1 is equal to the current value of s2
    elif s2[0:s2.find(' ')] == s1[0:s1.find(' ')]:  # If the author is the same, check by book title
        if s2[s2.find('«') + 1:s2.find('»')] > s1[s1.find('«') + 1:s1.find('»')]:
            s1 = s2
        elif s2[s2.find('«') + 1:s2.find('»')] < s1[s1.find('«') + 1:s1.find('»')]:
            answer = 'NO'
            break
    elif s2[0:s2.find(' ')] < s1[0:s1.find(' ')]:  # if the next one is less than the previous one, break
        answer = 'NO'
        break
    count += 1
print(answer)
