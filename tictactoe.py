import numpy as np
board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
# -----------------global variables
game_playing = True
winner = None
current_player = 'X'

def display_board():
    print(board[0, 0] + " | " + board[0, 1] + " | " + board[0, 2])
    print(board[1, 0] + " | " + board[1, 1] + " | " + board[1, 2])
    print(board[2, 0] + " | " + board[2, 1] + " | " + board[2, 2])
#     print(board[0, 0])

def handle_turns(player):
    print(player +"'s turn")
    positionx = input("Enter the row number of your selection ")
    positiony = input("Enter the column number of your selection ")
    
    valid = False
    while not valid:
        
        while positionx not in ["1", "2", "3"] and positiony not in ["1", "2", "3"]:
            positionx = input("INVALID INPUT Enter the row number of your selection from 1 to 3: ")
            positiony = input("INVALID INPUT Enter the column number of your selection from 1 to 3: ")

        positionx = int(positionx) - 1
        positiony = int(positiony) - 1

        if board[positionx, positiony] == '-':
            valid = True
        else:
            print("You can't go there, try again")
            
    board[positionx, positiony] = player
    display_board()


def check_game_over():
    check_win()
    check_tie()
    

def check_win():
    
    # set up a global variable
    global winner
    
    # check rows, columns and diagonals
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner # there was a win
    elif column_winner:
        winner = column_winner # there was a win
    elif diagonal_winner:
        winner = diagonal_winner # there was a win
    else:
        winner = None # there was no win
    return 
    
def check_rows():
    global game_playing
    row1 = board[0, 0] == board[0, 1] == board[0, 2] != '-' 
    row2 = board[1, 0] == board[1, 1] == board[1, 2] != '-'
    row3 = board[2, 0] == board[2, 1] == board[2, 2] != '-'
    if row1 or row2 or row3: # check if any row has equal values other than being empty ofc
        game_playing = False
    if row1:
        return board[0, 0]
    elif row2:
        return board[1, 0]
    elif row3:
        return board[2, 0]
    return


def check_columns():
    global game_playing
    col1 = board[0, 0] == board[1, 0] == board[2, 0] != '-' 
    col2 = board[0, 1] == board[1, 1] == board[2, 1] != '-'
    col3 = board[0, 2] == board[1, 2] == board[2, 2] != '-'
    if col1 or col2 or col3: # check if any columns has equal values other than being empty ofc
        game_playing = False
    if col1:
        return board[0, 0]
    elif col2:
        return board[0, 1]
    elif col3:
        return board[0, 2]
    return


def check_diagonals():
    global game_playing
    dia1 = board[0, 0] == board[1, 1] == board[2, 2] != '-' 
    dia2 = board[0, 2] == board[1, 1] == board[2, 0] != '-'
    if dia1 or dia2: # check if any diagonals has equal values other than being empty ofc
        game_playing = False
    if dia1:
        return board[0, 0]
    elif dia2:
        return board[0, 2]
    return


#     0 1 2
#   0 - - -
#   1 - - -
#   2 - - -

def check_tie():
    global game_playing
    if '-' not in board:
        game_playing = False
    return


def change_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return
    

def play_game():
    
    display_board()
    
    while game_playing: # True while playing the game
        
        handle_turns(current_player) # handle a turn
        
        check_game_over() # check if game is over or not
        
        change_player() # change the current player for X and O's
        
        # game ended.
    if winner == 'X' or winner == 'O':
        print(winner + " won")
    elif winner == None:
        print("Tie")
    
play_game()
