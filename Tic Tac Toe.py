#Created a board using a list and then defining it as a function
board = [" ", " ", " ",
" ", " ", " ",
" ", " ", " "]

def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2] + '\n' +
          board[3] + '|' + board[4] + '|' + board[5] + '\n' +
          board[6] + '|' + board[7] + '|' + board[8])

print_board()
print()

#Created two different functions for each players move.
def player1_move():
    icon = "X"
    choice = int(input("Player 1:Where do you want to move (1-9)?"))
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("Space is not empty.")

def player2_move():
    icon = "O"
    choice = int(input("Player 2:Where do you want to move (1-9)?"))
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("Space is not empty")

#Function for a victory condition
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
            (board[3] == icon and board[4] == icon and board[5] == icon) or \
            (board[6] == icon and board[7] == icon and board[8] == icon) or \
            (board[0] == icon and board[3] == icon and board[6] == icon) or \
            (board[1] == icon and board[4] == icon and board[7] == icon) or \
            (board[2] == icon and board[5] == icon and board[8] == icon) or \
            (board[0] == icon and board[4] == icon and board[8] == icon) or \
            (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

#Function for a draw
def draw():
    if " " not in board:
        return True
    else:
        return False

#While loop with all the functions. It will keep running until a winner is decided or there's a draw
while True:
    player1_move()
    print_board()
    if is_victory("X"):
        print()
        print("Player 1 wins!")
        break
    player2_move()
    if is_victory("O"):
        print()
        print("Player 2 wins!")
        break
    print_board()
    if draw():
        print()
        print("Its a draw!")

