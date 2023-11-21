# Import necessary modules from PyQt5 library
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

# Define the TicTacToeGame class that inherits from QWidget


class TicTacToeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # Initialize the UI elements
    def init_ui(self):
        # Set window title and geometry (position and size)
        self.setWindowTitle('Tic Tac Toe')
        self.setGeometry(100, 100, 200, 200)

        # Initialize game state variables
        self.board = [' '] * 9
        self.current_player = 'x'
        self.buttons = []

        # Create buttons for each cell in the Tic Tac Toe grid
        for i in range(9):
            # Create a QPushButton with empty label
            button = QPushButton('', self)
            button.setFont(button.font())  # Set the font for the button
            # Connect button click to make_move function
            button.clicked.connect(lambda _, i=i: self.make_move(i))
            self.buttons.append(button)  # Add the button to the list

        # Create a reset button
        self.reset_button = QPushButton('Reset', self)
        # Connect button click to reset_game function
        self.reset_button.clicked.connect(self.reset_game)

        # Create the layout for buttons
        layout = QVBoxLayout()

        # Organize buttons in a 3x3 grid using a QHBoxLayout for each row
        grid_layout = [self.buttons[i:i + 3] for i in range(0, 9, 3)]
        for row in grid_layout:
            row_layout = QHBoxLayout()
            for button in row:
                row_layout.addWidget(button)
            layout.addLayout(row_layout)

        # Add the reset button to the layout
        layout.addWidget(self.reset_button)

        # Set the layout for the main widget
        self.setLayout(layout)

        # Update the initial UI
        self.update_ui()

    # Handle the button click to make a move
    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.update_ui()
            winner = self.check_winner()
            if winner:
                self.show_winner(winner)
            else:
                self.current_player = 'o' if self.current_player == 'x' else 'x'

    # Update the UI based on the game state
    def update_ui(self):
        for i in range(9):
            self.buttons[i].setText(self.board[i])

    # Check for a winner or a tie
    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return 'Tie'
        return None

    # Display the winner or tie message
    def show_winner(self, winner):
        message = f'Winner: {winner}' if winner != 'Tie' else 'It\'s a Tie!'
        winner_label = QLabel(message, self)
        winner_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout().addWidget(winner_label)

    # Reset the game state
    def reset_game(self):
        self.board = [' '] * 9
        self.current_player = 'x'
        self.update_ui()
        winner_label = self.findChild(QLabel)
        if winner_label:
            winner_label.deleteLater()


# Run the application
if __name__ == '__main__':
    app = QApplication([])  # Create the application instance
    ex = TicTacToeGame()  # Create an instance of the TicTacToeGame class
    ex.show()  # Display the game window
    app.exec_()  # Run the application event loop
