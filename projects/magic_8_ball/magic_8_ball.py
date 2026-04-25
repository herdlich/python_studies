import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Definitely yes",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Signs point to yes",
    "Yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]
print("Hi, I'm a magic ball, and I know the answer to any question you have")
user_name = input('What is your name? ')
print(f'Great! Welcome, {user_name}')

while True:
    question = input("I'm waiting for your question: ")
    print(random.choice(answers))
    any_q = input('Any other question? Yes or No: ').strip().lower()
    if any_q == 'No':
        print('See you later')
        break
