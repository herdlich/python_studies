# Checking whether every opening bracket has been closed

def is_correct_bracket(text):
    count_br = 0

    for el in text:
        if el == '(':
            count_br += 1
        elif el == ')':
            count_br -= 1
        if count_br < 0:
            return False
    if count_br == 0:
        return True
    else:
        return False


txt = input()
print(is_correct_bracket(txt))
