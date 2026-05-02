from datetime import datetime


def visit_log(us_name):
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")

    with open('traffic.txt', 'a', encoding='UTF-8') as tf:
        tf.write(f'Name: <{us_name}>; Visit time: <{time_str}>\n')


link = input('Click the link test.com? Y / N: ').strip().lower()

while link not in ['y', 'n']:
    print('PLS, enter Y or N')
    link = input('Click the link test.com? Y / N: ').strip().lower()

if link == 'y':
    us_name = input('Enter your nickname: ').strip()

    while not us_name: us_name = input('Enter your nickname: ').strip()

    visit_log(us_name)
    print('THX!')
else:
    print('Closed')
