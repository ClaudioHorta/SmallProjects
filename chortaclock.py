import tkinter as tk
import time

# Function to update the clock display


def update_clock():
    # Get the current time and format it as HH:MM:SS
    ora_curenta = time.strftime("%H:%M:%S")

    # Update the text of the Label widget to display the current time
    chorta.config(text=ora_curenta)

    # Schedule the update_clock function to run again after 1000 milliseconds (1 second)
    chorta.after(1000, update_clock)


# Create the main application window
app = tk.Tk()
app.title("Chorta Python Clock")

# Create a Label widget to display the time, set an initial empty text, and specify the font
chorta = tk.Label(app, text="", font=("Helvetica", 48))

# Pack the Label widget to add it to the main application window
chorta.pack()

# Call the update_clock function to start displaying the time and updating it
update_clock()

# Start the Tkinter event loop to run the application
app.mainloop()
