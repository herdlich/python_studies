def user_list(n):
    us_list = []
    with open('source.txt', 'w', encoding='UTF-8') as f:
        for i in range(n):
            us_line = input(f'{i + 1}. Enter your text: ')
            f.write(f'{us_line}\n')
            us_list.append(us_line)

    return us_list


def mirror_list(us_list):
    mirrored_list = []

    with open('mirror.txt', 'w', encoding='UTF-8') as fm:
        for i in range(len(us_list), 0, -1):
            fm.write(f'{us_list[i - 1]}\n')
            mirrored_list.append(us_list[i - 1])

        return mirrored_list


try:
    n = int(input('Enter the number of strings: '))

    while n < 1:
        print('Please enter a positive integer')
        n = int(input('Enter the number of strings: '))
    else:
        print(*mirror_list(user_list(n)), sep='\n')
except:
    print('PLS enter valid integer')
