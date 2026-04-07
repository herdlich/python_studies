# 3 requirements:
# the username must begin with the “@” symbol,
# contain between 5 and 15 characters,
# and consist solely of lowercase letters and/or numbers

nickname = input('Nickname: ')
if nickname[0] == '@' and 5 <= len(nickname) <= 15 and nickname[1:].isalnum() and nickname == nickname.lower():
    print('Correct')
else:
    print('Incorrect')
