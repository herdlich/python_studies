a_eng_lower = 'abcdefghijklmnopqrstuvwxyz'
a_eng_upper = a_eng_lower.upper()
a_rus_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
a_rus_upper = a_rus_lower.upper()

print('Hi! Here you can apply the Caesar cipher to your text')
print('The characters are shifted to the right')
print()


def check_language_text(text):
    count_e, count_r = 0, 0

    for char in text:
        if char in a_eng_lower or char in a_eng_upper:
            count_e += 1
        elif char in a_rus_lower or char in a_rus_upper:
            count_r += 1

    if count_e > 0 and count_r == 0:
        return 'En', True
    elif count_e == 0 and count_r > 0:
        return 'Ru', True
    else:
        return None, False


def caesar_cipher_right(text, key):
    lang, is_valid = check_language_text(text)
    l = []

    if lang == 'En':
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

    elif lang == 'Ru':
        for char in text:
            if char in a_rus_lower:
                if char.isalpha():
                    if 1072 <= ord(char) + key <= 1103:
                        l.append(chr(ord(char) + key))
                    elif ord(char) + key > 1103:
                        l.append(chr(ord(char) + key - 32))
            elif char in a_rus_upper:
                if char.isalpha():
                    if 1040 <= ord(char) + key <= 1071:
                        l.append(chr(ord(char) + key))
                    elif ord(char) + key > 1071:
                        l.append(chr(ord(char) + key - 32))
            else:
                l.append(char)

    else:
        print('Language not supported')
        return False, False

    return l


def caesar_cipher_left(text, key):
    lang, is_valid = check_language_text(text)
    l = []

    if lang == 'En':
        for char in text:
            if char in a_eng_lower:
                if char.isalpha():
                    if 97 <= ord(char) - key <= 122:
                        l.append(chr(ord(char) - key))
                    elif ord(char) - key < 97:
                        l.append(chr(ord(char) - key + 26))
            elif char in a_eng_upper:
                if char.isalpha():
                    if 65 <= ord(char) - key <= 90:
                        l.append(chr(ord(char) - key))
                    elif ord(char) - key < 65:
                        l.append(chr(ord(char) - key + 26))
            else:
                l.append(char)

    elif lang == 'Ru':
        for char in text:
            if char in a_rus_lower:
                if char.isalpha():
                    if 1072 <= ord(char) - key <= 1103:
                        l.append(chr(ord(char) - key))
                    elif ord(char) - key < 1072:
                        l.append(chr(ord(char) - key + 32))
            elif char in a_rus_upper:
                if char.isalpha():
                    if 1040 <= ord(char) - key <= 1071:
                        l.append(chr(ord(char) - key))
                    elif ord(char) - key < 1040:
                        l.append(chr(ord(char) - key + 32))
            else:
                l.append(char)

    else:
        print('Language not supported')
        return False, False

    return l


s = input('Enter the text you want to encrypt: ')
k = int(input('Enter the offset value: '))
offset = input('Which way should the cipher be shifted? R - Right, L - Left: ').strip().lower()
print()

if offset == 'l':
    print(*caesar_cipher_left(s, k), sep='')
elif offset == 'r':
    print(*caesar_cipher_right(s, k), sep='')
