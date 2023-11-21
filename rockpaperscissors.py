import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to RPS!')

        self.moves: dict = {'rock': '✊', 'paper': '📃', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_score: int = 0
        self.ai_score: int = 0

    def play_game(self):
        user_move: str = input('What is your move? Rock, Paper, or Scissors: ').lower()
        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)
        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print('-------------')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('-------------')

    def check_moves(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print(f'It\'s a Tie! Score: User - {self.user_score} AI - {self.ai_score}')
        elif user_move == 'rock' and ai_move == 'scissors':
            self.user_score += 1
            print(f'You win! Score: User - {self.user_score} AI - {self.ai_score}')
        elif user_move == 'scissors' and ai_move == 'paper':
            self.user_score += 1
            print(f'You win! Score: User - {self.user_score} AI - {self.ai_score}')
        elif user_move == 'paper' and ai_move == 'rock':
            self.user_score += 1
            print(f'You win! Score: User - {self.user_score} AI - {self.ai_score}')
        else:
            self.ai_score += 1
            print(f'AI win! Score: User - {self.user_score} AI - {self.ai_score}')

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()
