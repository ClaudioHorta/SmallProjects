import random
import string
import tkinter as tk

# Function to generate a random password of the given length


def generate_password(length):
    # Define characters for the password (letters, digits, and punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Function to handle the password generation based on user input


def generate_password_interface():
    # Retrieve the desired password length from the entry widget
    length_password = int(entry_length.get())

    # Check if the desired password length is at least 6 characters
    if length_password < 6:
        label_result.config(
            text="Length password should have at least 6 characters.")
    else:
        # Generate the password and display it
        password_generator = generate_password(length_password)
        label_result.config(text="Password generated: " + password_generator)


# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create a label to instruct the user to input the desired password length
label_length = tk.Label(root, text="Introduce the desired password length: ")
label_length.pack()

# Create an entry widget for the user to input the desired password length
entry_length = tk.Entry(root)
entry_length.pack()

# Create a button to trigger password generation
generate_button = tk.Button(
    root, text="Generate Password", command=generate_password_interface)
generate_button.pack()

# Create a label to display the generated password or an error message
label_result = tk.Label(root, text="")
label_result.pack()

# Start the Tkinter event loop to run the application
root.mainloop()
