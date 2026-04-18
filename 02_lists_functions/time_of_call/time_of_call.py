def print_time_call(time, difference):
    time = time.split(':')
    hh = int(time[0])
    mm = int(time[1])

    if hh < 24 and mm < 60:
        h = hh + difference
        if h > 23:
            h -= 24
        if h < 10:
            h = '0' + str(h)
        if 0 < mm < 10:
            mm = '0' + str(mm)
        if mm == 0:
            mm = '00'

        print(f'Time of call: {h}:{mm}')

    else:
        print('Incorrect time, try again')


try:
    print_time_call(input('Enter the time: '), int(input('Enter the time difference: ')))
except Exception as e:
    print(f'Error: {e}')
