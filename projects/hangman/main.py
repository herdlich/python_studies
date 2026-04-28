import random

word_list = ['apple', 'banana', 'computer', 'elephant', 'football', 'guitar', 'hospital', 'island', 'jacket',
             'kangaroo', 'lemon', 'mountain', 'notebook', 'orange', 'penguin', 'question', 'rabbit', 'sunshine',
             'tiger', 'umbrella', 'vacation', 'waterfall', 'xylophone', 'yellow', 'zebra', 'adventure', 'butterfly',
             'diamond', 'energy', 'flower', 'galaxy', 'hammer', 'iceberg', 'journey', 'kingdom', 'lantern', 'mystery',
             'nature', 'ocean', 'pyramid', 'rhythm', 'sapphire', 'telescope', 'universe', 'volcano', 'weather', 'yacht',
             'zenith', 'blizzard', 'crystal']


def get_words():
    word = random.choice(word_list)
    return word


def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]

    return stages[tries]


def play(word):
    word_completion = ['_'] * len(word)
    guessed_letters = []
    tries = 6

    print('Welcome to Hangman!')
    while True:
        print(display_hangman(tries))
        print(*word_completion)

        if '_' not in word_completion:
            print()
            print('🎉 You guessed the word: ✅ {}'.format(word.upper()))
            play_again = input('Would you like to play again? (y/n): ').strip().lower()
            if play_again == 'y':
                word = get_words()
                word_completion = ['_'] * len(word)
                guessed_letters = []
                tries = 6
                continue
            else:
                print('Game over')
                break


        user_word = input('Guess a letter: ').strip().lower()

        if user_word.isalpha() and len(user_word) == 1:
            if user_word in guessed_letters:
                print('You already guessed this letter')
            elif user_word in word:
                guessed_letters.append(user_word)

                for i in range(len(word)):
                    if word[i] == user_word:
                        word_completion[i] = user_word.upper()

            else:
                guessed_letters.append(user_word)
                tries -= 1
                if tries == 0:
                    print(display_hangman(tries))
                    print('❌ You lose. The correct word: ✅ {}'.format(word.upper()))
                    play_again = input('Would you like to play again? (y/n): ').strip().lower()
                    if play_again == 'y':
                        word = get_words()
                        word_completion = ['_'] * len(word)
                        guessed_letters = []
                        tries = 6
                        continue
                    else:
                        print('Game over')
                        break

        else:
            print('Please enter one letter')

play(get_words())