# The script uses the Caesar cipher, shifting the characters of each word by the length of that word

a_eng_lower = 'abcdefghijklmnopqrstuvwxyz'
a_eng_upper = a_eng_lower.upper()


def caesar_cipher(text, key):  # encryption function
    l = []

    for char in text:
        if char in a_eng_lower:
            if char.isalpha():
                if 97 <= ord(char) + key <= 122:
                    l.append(chr(ord(char) + key))
                elif ord(char) + key > 122:
                    l.append(chr(ord(char) + key - 26))
        elif char in a_eng_upper:
            if char.isalpha():
                if 65 <= ord(char) + key <= 90:
                    l.append(chr(ord(char) + key))
                elif ord(char) + key > 90:
                    l.append(chr(ord(char) + key - 26))
        else:
            l.append(char)

    return l


s = input('Enter text: ').split()
new_s = []

for el in s:
    k = sum(1 for char in el if char.isalpha())
    func_ret = caesar_cipher(el, k)  # gets its own word
    word = ''.join(func_ret)  # a word is combined into a string
    new_s.append(word)  # the collected word is added to the list

print(*new_s)
