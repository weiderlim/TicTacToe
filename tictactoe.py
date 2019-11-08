# creating my own personal tic tac toe game, with some reference from Youtube Tutorial videos.
# creating a robust program is one of the main aspects that we want to focus on, with focus on the robust_input function.
# also try to make the program as short and concise as possible

# GLOBAL VARIABLES - If you do not want to keep passing global variables, use Class instead.

# creating board
board = []
for i in range(9):
    board.append("-")

game_over = False
player_curr = "O"

# display board
def display_board():
    print ("{} {} {}".format(board[0], board[1], board[2]))
    print ("{} {} {}".format(board[3], board[4], board[5]))
    print ("{} {} {}".format(board[6], board[7], board[8]))

# alternate turns
def alternate_turns():
    global player_curr
    if player_curr == "O":
        player_curr = "X"
    else:
        player_curr = "O"


# check if someone wins
def check_win():
    global game_over
    row_result = check_rows()
    col_result = check_cols()
    diag_result = check_diag()
    # check if any of the results returns the winner
    if row_result != False or col_result != False or diag_result != False:
        game_over = True
        display_board()
        # declaring the winner
        for i in [row_result, col_result, diag_result]:
            if i != False:
                print ("Player {} wins!".format(i))
                
# checking rows
def check_rows():
    if board[0] ==  board[1] == board[2] != "-":
        return board[0]
    if board[3] ==  board[4] == board[5] != "-":
        return board[3]
    if board[6] ==  board[7] == board[8] != "-":
        return board[6]
    return False

# checking columns
def check_cols():
    if board[0] ==  board[3] == board[6] != "-":
        return board[0]
    if board[1] ==  board[4] == board[7] != "-":
        return board[1]
    if board[2] ==  board[5] == board[8] != "-":
        return board[2]
    return False

# checking diagonals
def check_diag():
    if board[0] ==  board[4] == board[8] != "-":
        return board[0]
    if board[2] ==  board[4] == board[6] != "-":
        return board[2]
    return False

# check if game ends in tie
def check_tie():
    global game_over
    if "-" not in board:
        game_over = True
        print ("Game ends in Tie")

# packaging the input into one function to only allow the input to be accepted if all the input criterias are fulfilled
def robust_input():
    global player_curr
    valid = False

    # this seems like a good way to keep returning to the start question; need to really ensure that all the possible inputs are considered in the if statements.
    while not valid:
        position = input("Player {}'s turn to go: ".format(player_curr))

        # use the try to prevent the crash from initial input, ensuring only whole numbers are accepted. All other criterias are be placed within it. Needed because you wanted to convert the input to int immediately.
        try:
            # allows the user to enter number between 1-9, while board reads between 0-8
            position = int(position) - 1

            # checking for int within the acceptable range.
            if position not in list(range(0,9)):
                print ("Input invalid. Please enter a number between 1-9.")
        
            # checking if the position has already been filled.
            elif board[position] != "-":
                print ("That square has already been filled. Please choose another square.")
            else:
                valid = True
        except:
            print ("Please enter a whole number")
    
    # accepted input
    board[position] = player_curr

# play game - main
def play_game():
    global player_curr

    while not game_over: 
        display_board()
        robust_input()
        check_win()
        check_tie()
        alternate_turns()

play_game()