digit, message = int(input('Enter a shift number: ')), input('Enter your message: ')
total = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(message)):
    for j in range(len(alphabet)):
        if 96 < ord(message[i]) - digit < 122 and message[i] == alphabet[j]:
            total += chr(ord(message[i]) - digit)

        # If the value goes beyond the range of the English alphabet, 26 is added to bring it back within the range
        elif ord(message[i]) - digit < 97 and message[i] == alphabet[j]:
            total += chr(ord(message[i]) - digit + 26)

print(total)
