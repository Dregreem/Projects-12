
from player import HumanPlayer, RandomComputerPlayer

class Tictactoe:
    def __init__(self):
        # Initialize the board as a list of 9 empty spaces
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # Print the current state of the board
        for element in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(element) + ' |')

    @staticmethod
    def print_board_nums():
        # Print the board numbers for reference
        number_board = []
        for j in range(3):
            row = []
            for i in range(j * 3 + 1, (j + 1) * 3 + 1):
                row.append(str(i))
            number_board.append(row)
        for row in number_board:
            print(' | '.join(row))

    def available_moves(self):
        # Return a list of available moves (indices of empty spaces)
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        # Return the number of empty squares on the board
        return self.board.count(' ')

    def make_move(self, square, letter):
        # Make a move on the board if the square is empty
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check if the current move leads to a win

        # Check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        # Check diagonals if the move is on an even-numbered square (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + " wins")
                return letter

        # Switch players
        letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It is a tie")

if __name__ == "__main__":
    # Initialize players and the game
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = Tictactoe()
    play(t, x_player, o_player, print_game=True)