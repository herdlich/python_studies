def is_palindrome(text):
    text = text.lower()
    text_pl = ''
    for i in text:
        if i.isalpha():
            text_pl += i

    if text_pl == text_pl[::-1]:
        return True
    return False


# считываем данные
txt = input('Enter a string: ')

# вызываем функцию
print(is_palindrome(txt))