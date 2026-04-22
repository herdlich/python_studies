# The script converts camel case to snake case
#    Conditions:
# 1. The first word begins with a capital letter
# 2. Words are written in camel case

def convert_to_python_case(text):
    new_text = ''
    count = -1  # count so that the new_text follows text

    for i in range(len(text)):
        if text[i].isupper():
            count += 1
            new_text = new_text[:i + count] + '_' + text[i:]

    new_text = new_text[1:]  # the very first one is cut off "_"
    result = new_text.lower()
    return result


txt = input("Enter a string: ")

print(convert_to_python_case(txt))
