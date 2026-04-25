import random

print('Welcome to the Number Guessing Game!')
game_start = input('Would you like to play? y/n: ').strip().lower()


def is_valid(number):
    if number < 1 or number > 100:
        return False
    else:
        return True


while game_start == 'y':
    random_number = random.randint(1, 100)
    attempts_count = 0

    while True:
        try:
            user_number = int(input('Enter a number: '))
        except ValueError:
            print('Please, enter a valid number')
            continue

        if not is_valid(user_number):
            print('Please, enter a number between 1 and 100')
            continue

        attempts_count += 1

        if user_number == random_number:
            print(f'You guessed the number {random_number}. Number of attempts: {attempts_count}')
            break
        elif user_number > random_number:
            print('Your number is higher than the one I picked. Try again.')
        else:
            print('Your number is lower than the one I picked. Try again.')

    game_start = input('Want to play again? y/n: ').strip().lower()

print('The game is over')
