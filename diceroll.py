import random


# Function to roll a specified number of dice and return the individual rolls and their sum
def roll_dice(amount: int = 2) -> (list[int], int):
    if amount <= 0:
        raise ValueError  # Raise an error if the specified amount is not positive

    rolls: list[int] = []  # List to store individual dice rolls
    rolls_sum = 0  # Variable to store the sum of dice rolls

    # Loop to roll the dice and calculate the sum
    for i in range(amount):
        random_roll: int = random.randint(1, 6)  # Generate a random number between 1 and 6
        rolls.append(random_roll)  # Add the individual roll to the list
        rolls_sum += random_roll  # Update the total sum

    return rolls, rolls_sum  # Return a tuple containing the list of rolls and their sum


# Main function to interact with the user
def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? ')
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break

            # Roll the dice and unpack the result
            rolls, rolls_sum = roll_dice(int(user_input))

            # Print the individual rolls separated by commas and display the total sum
            print(', '.join(map(str, rolls)), f'Total Sum: {rolls_sum}')
        except ValueError:
            print('Please enter a valid number')


# Run the main function when the script is executed
if __name__ == '__main__':
    main()