
from random import randrange

words = [
    "hello",
    "yass",
    "okay",
    "Notice",
    "sasquatch",
    "alien",
    "two",
    'marvelous',
    'wonderful',
    "sheep",
    "sleep",
    'whatever'
]


while True:
    secret = words[randrange(0, len(words))]
    attempts = 5
    current_index = 0


    print('-- new word! --')

    while True:
        print('You have ' + str(attempts) + ' attempts left')

        if attempts <= 0:
            print('You lose')
            break
        guess = input("Guess a letter: ")

        if guess == secret[current_index]:
            print('You got the ' + str(current_index) + 'th letter right')
            current_index += 1
        else:
            print('No, try again')
            attempts -=1

        if current_index == len(secret):
            print('You have won the game!') 
            break



    print('Your word was ' + secret)
