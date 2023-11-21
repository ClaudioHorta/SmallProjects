
import sys
import random

first_number = int(sys.argv[1])
last_number = int(sys.argv[2])


def random_number():
    return random.choice(range(first_number, last_number))


def message():
    winner_number = random_number()

    while True:
        try:
            guess_input = int(input(f'Guess a number between {first_number} and {last_number}. Enter your guess here: '))

            if guess_input == 0:
                return 'User exited the game'
            elif guess_input < first_number or guess_input > last_number:
                print(f'{guess_input} is not valid number for this game')
            elif guess_input != winner_number:
                print(f' {guess_input} is not the right guess, keep guessing! Otherwise, to exit enter: \'0\'')
            else:
                print('Your guess is correct')
                return ''
        except ValueError:
            print('Please enter a number')

result = message()

print(result)

