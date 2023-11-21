#Guess a number

from random import randint

# Start the program with basic setup
lower_num, upper_num = 1, 10
random_number: int = randint(lower_num, upper_num)
print(f'Guess the number in the range from {lower_num} to {upper_num}.')

# Set the maximum number of tries
max_tries = 3
tries = 0

# Run a loop for the game with a limited number of tries
while tries < max_tries:
    # Increment the tries counter
    tries += 1

    # Get the user guess
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue

    # Check the user guess
    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print('You guessed it!')
        break
else:
    print(f'Sorry, you have reached the maximum number of tries. The correct number was {random_number}.')