# integrating pygame into my previous script containing code to play and print the game in the terminal

# ============================             MODULES              ===============================

import pygame

# ============================          GLOBAL VARIABLES        ===============================
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tic Tac Toe")

# creating board (list comprehension)
board = ["-" for i in range(9)]
# setting the player, O goes first
player_curr = "O"
# keeping tabs on player scores
score_X = 0
score_O = 0

# ==================================        FUNCTIONS           ==============================
    
# create pygame display
def display_board():
    global board
    # define size of single 3 x 3 square
    square_size = 500/3

    # draw square lines
    pygame.draw.line(window, pygame.Color(255, 255, 255), (square_size, 0), (square_size, 500))
    pygame.draw.line(window, pygame.Color(255, 255, 255), (square_size * 2, 0), (square_size * 2 , 500))
    pygame.draw.line(window, pygame.Color(255, 255, 255), (0, square_size), (500, square_size))
    pygame.draw.line(window, pygame.Color(255, 255, 255), (0, square_size * 2), (500, square_size * 2))

    # draw X and O
    for squares in range(len(board)):
        if board[squares] == "O":
            draw_O(squares)
        if board[squares] == "X":
            draw_X(squares)

def draw_O(squares):
    # setting which squares to draw in
    # setting the y distance of O's from window edge
    if squares in [0, 1, 2]:
        col = 83
    elif squares in [3, 4, 5]:
        col = 250
    else:
        col = 417

    # setting the x distance of O's from window edge
    if squares in [0, 3, 6]:
        row = 83
    elif squares in [1, 4, 7]:
        row = 250
    else:
        row = 417

    # drawing the circles
    pygame.draw.circle(window, pygame.Color(0, 0, 255), (row, col), 65)
    pygame.draw.circle(window, pygame.Color(0, 0, 0), (row, col), 60)

def draw_X(squares):
    # setting which squares to draw in
    # setting the y distance of X's from window edge
    if squares in [0, 1, 2]:
        col = 83
    elif squares in [3, 4, 5]:
        col = 250
    else:
        col = 417

    # setting the x distance of X's from window edge
    if squares in [0, 3, 6]:
        row = 83
    elif squares in [1, 4, 7]:
        row = 250
    else:
        row = 417

    line_length = 60
    # drawing the X's
    pygame.draw.line(window, pygame.Color(255, 0, 0), (row - line_length, col - line_length), (row + line_length, col + line_length))
    pygame.draw.line(window, pygame.Color(255, 0, 0), (row - line_length, col + line_length), (row + line_length, col - line_length))

# alternate player turns
def alternate_turns():
    global player_curr
    if player_curr == "O":
        player_curr = "X"
    else:
        player_curr = "O"

# check if someone wins
def check_win():
    # return results from checking rows, columns and diagonals
    row_result = check_rows()
    col_result = check_cols()
    diag_result = check_diag()
    # check if any of the results returns the winner
    if row_result != False or col_result != False or diag_result != False:
        display_board()
        # declaring the winner
        for i in [row_result, col_result, diag_result]:
            if i != False:
                return i 
    # return false if no winner found
    return False
                
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
    if "-" not in board:
        return True

# read mouse input and add result to board
def mouse_input(mouse_pos):
    global player_curr, board

    # define rows and cols of squares
    squares_1 = range(0, 166)
    squares_2 = range(167, 333)
    squares_3 = range(334, 500)
    
    # enter position (square according to mouse position)
    if mouse_pos[0] in squares_1 and mouse_pos[1] in squares_1:
        position = 0
    elif mouse_pos[0] in squares_2 and mouse_pos[1] in squares_1:
        position = 1
    elif mouse_pos[0] in squares_3 and mouse_pos[1] in squares_1:
        position = 2
    elif mouse_pos[0] in squares_1 and mouse_pos[1] in squares_2:
        position = 3
    elif mouse_pos[0] in squares_2 and mouse_pos[1] in squares_2:
        position = 4
    elif mouse_pos[0] in squares_3 and mouse_pos[1] in squares_2:
        position = 5
    elif mouse_pos[0] in squares_1 and mouse_pos[1] in squares_3:
        position = 6
    elif mouse_pos[0] in squares_2 and mouse_pos[1] in squares_3:
        position = 7
    elif mouse_pos[0] in squares_3 and mouse_pos[1] in squares_3:
        position = 8
    
    # robust coding -- do not let the current player to overwrite if the square has already been filled.
    if board[position] == "-":
        board[position] = player_curr
        # alternate between players only when a new square is filled
        alternate_turns()

def restart(result=False):
    global board, score_X, score_O
    restart_game = False

    # prints the winner, scores, or check for tie
    if result == "X":
        score_X += 1
    elif result == "O":
        score_O += 1
    
    # display caption with score
    pygame.display.set_caption("Tic Tac Toe | Player O :{} Player X :{}".format(score_O, score_X))
    
    # refresh board
    board = ["-" for i in range(9)]

    # hold board until players presses R to restart game
    while not restart_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    play_game()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    
def message_display(text):
    global window

    # creating the font object/instance
    myfont = pygame.font.SysFont("Comic Sans MS", 20)
    # rendering text on the surface
    textSurface = myfont.render(text, True, (255, 255, 255))
    # blitting the surface onto the window
    window.blit(textSurface, (0, 0))

# game loop
def play_game():
    pygame.init()
    global player_curr
    game_over = False

    while not game_over: 
        # handling game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                # inserting quit method here enables quitting even after the game is restarted
                pygame.quit()
            # get mouse position when mouse is pressed in the window
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_input(mouse_pos)
            # quit if escape is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    pygame.quit()
        
        # handling game logic, checking for winner or tie
        winner = check_win()
        tie = check_tie()
        
        # handling display
        window.fill(pygame.Color(0, 0, 0))    
        display_board()

        # display player turn, or if game ends display the result
        if winner: 
            message_display("Player {} wins! Press R to restart or ESC to quit".format(winner))
        elif tie:
            message_display("Game is tied. Press R to restart or ESC to quit")
        else:
            message_display("Player {}'s turn.".format(player_curr))
 
        pygame.display.update()

        # restart the game
        if winner: restart(winner)
        if tie: restart()

play_game()
pygame.quit()

