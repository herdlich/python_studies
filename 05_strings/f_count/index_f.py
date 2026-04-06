s = input('Enter a string: ')
f_count = s.count('f')
if f_count == 1:
    print(s.index('f'))
elif f_count > 1:
    print(s.find('f'), s.rfind('f'), sep=' ')
else:
    print('NO')