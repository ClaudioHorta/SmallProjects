from random import choice

def run_game():
    # Select a random word from the list
    word: str = choice(['apple', 'secret', 'banana'])

    # Get the username from the user
    username: str = input('What is your username? >> ')
    print(f'Welcome to Hangman, {username}!')

    # Setup initial variables
    guessed: str = ''
    tries: int = 10

    # Main game loop
    while tries > 0:
        blanks: int = 0
        print('Word: ', end='')

        # Display the word with blanks for unguessed letters
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()  # adds a blank line

        # Check if all letters have been guessed
        if blanks == 0:
            print('You got it!')
            break

        # Get user input for a letter
        guess: str = input('Enter a letter: ')

        # Check if the full word is guessed
        if guess == 'apple' or guess == 'secret' or guess == 'banana':
            print('You guessed the full word! GG!!')
            break

        # Check if the input is a single letter
        if len(guess) != 1:
            print('Please enter only one letter at a time.')
            continue

        # Check if the letter has already been guessed
        if guess in guessed:
            print(f'You already used "{guess}". Please try another letter!')
            continue

        # Add the guessed letter to the list of guessed letters
        guessed += guess

        # Check if the guessed letter is not in the word
        if guess not in word:
            tries -= 1
            print(f'Sorry... \'{guess}\' is not in the word... Letters already used {list(guessed)} ({tries} tries remaining)')

            # Check if no more tries are remaining
            if tries == 0:
                print('No more tries remaining. You lose.')
                break

if __name__ == '__main__':
    run_game()
