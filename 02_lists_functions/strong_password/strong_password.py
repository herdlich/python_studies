# The script checks the strength of the password

# A password is considered secure if:
# 1. it is at least 8 characters long;
# 2. it contains at least one uppercase letter;
# 3. it contains at least one lowercase letter;
# 4. it contains at least one number.

def is_password_strong(password):
    condition_1, condition_2, condition_3, condition_4 = False, False, False, False
    count_upper, count_lower, count_digit = 0, 0, 0

    if len(password) > 7:
        condition_1 = True
    for i in password:
        if i.isupper():
            count_upper += 1
    if count_upper > 0:
        condition_2 = True
    for j in password:
        if j.islower():
            count_lower += 1
    if count_lower > 0:
        condition_3 = True
    for k in password:
        if k.isdigit():
            count_digit += 1
    if count_digit > 0:
        condition_4 = True

    if condition_1 and condition_2 and condition_3 and condition_4:
        return True
    else:
        return False

passw = input("Enter password: ")
print(is_password_strong(passw))