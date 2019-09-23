class board:
    
    def __init__(self):#inialize board
        self.board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    def show_board(self):#function to display board
        for i in range(3):
            for j in range(3):
                print("   " + str(self.board[i][j]), end = "")
            print()
        print("\n")

    def play(self, x, y, Piece):#place tha piece in the spot the player chooses
        self.board[x][y] = Piece
        self.eval_board()
        self.show_board()

    def eval_board(self):#refresh board
        board = self.board


winnerX = False
winnerO = False

#winnerX = (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X")

#winnerO = (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O")

#check if theres a winner
if winnerX:
    print("X is the winner!")
    quit()
elif winnerO:
    print("O is the winner!")
    quit()
else :
    print("Continue")

board = board()
board.show_board()
board.play(0, 0, "X")
board.play(1, 2, "O")
board.play(0, 1, "X")
board.play(1, 1, "O")
board.play(0, 2, "X")
print()
board.show_board