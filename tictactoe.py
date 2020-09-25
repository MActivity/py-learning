## Ask players for names
## Explain game to players

gameBoard = [[' ', ' ',' '],
             [' ', ' ',' '],
             [' ', ' ',' ']]

Player1 = "Player 1"
Player2 = "Player 2"
Player_1_choice = []
Player_2_choice = []
turn = 1
game_over = False


def print_gb():
    for i in range(0,3):
        print(gameBoard[i])

def start():    
    print(f'{Player1} will go first, {Player2} will go second')
    print(" ")
    print("To play, enter in a number that indicates a \nhorizontal row, followed by a vertical column")
    print(" ")
    print("The rows and columns are numbered 0, 1, and 2\nthey move top-down and left-right")
    print(" ")
    print("Let's get started!")
    
def check_winner():
    # check rows
    global game_over
    for i in range(0,3):
        if gameBoard[i] == ['O','O','O']:
            print(f"Player 1 wins with row {i}")
            game_over = True
        elif gameBoard[i] == ['X','X','X']:
            print(f"Player 2 wins with row {i}")
            game_over = True
        else:
            pass
    # check columns
    row_sums = list(zip(gameBoard[0], gameBoard[1], gameBoard[2]))
    for i in range(0,3):
        if row_sums[i] == ('O','O','O'):
            print(f"Player 1 wins with column {i}")
            game_over = True
        elif row_sums[i] == ('X','X','X'):
            print(f"Player 2 wins with column {i}")
            game_over = True
        else:
            pass
    # check diagonals
    diag_one = []
    diag_two = []
    x = 0
    for i in range(0,3):
        diag_one.append(gameBoard[i][x])
        x += 1
    if diag_one == ['O','O','O']:
        print("player one was won diagonally")
        game_over = True
    elif diag_one == ['X','X','X']:
        print("player two has won diagonally")
        game_over = True
    else:
        x = 0
        pass
    for i in range(2,-1,-1):
        diag_two.append(gameBoard[i][x])
        x += 1
    if diag_two == ['O','O','O']:
        print("player one was won diagonally")
        game_over = True
    elif diag_two == ['X','X','X']:
        print("player two has won diagonally")
        game_over = True
    else:
        x = 0
        pass

        

def choice():
    global turn
    global gameBoard
    choiceRow = 3
    choiceCol = 3
    current_player = "Player 1"
    # determine who is playing
    if turn % 2 == 0:
        piece  = "X"
        current_player = "Player 2"
    else:
        piece = "O"
    # ask for a placement
    while choiceRow > 2 or choiceCol > 2:
        choiceRow = int(input(f'{current_player} what is your row choice? (0, 1, or 2) '))
        choiceCol = int(input(f'{current_player} what is your column choice? (0, 1, or 2) '))
        # check if it is already taken
        if gameBoard[choiceRow][choiceCol] == ' ':
            # place piece
            gameBoard[choiceRow][choiceCol] = piece
        else:
            # ask again
            print("Sorry, that place is taken")
            choiceRow = input(f'{current_player} what is your row choice? (0, 1, or 2) ')
            choiceCol = input(f'{current_player} what is your column choice? (0, 1, or 2) ')
    #check game
    check_winner()
    # show board
    print_gb()
    turn += 1
    
def reset():
    global gameBoard 
    
    gameBoard = [[' ', ' ',' '],
                 [' ', ' ',' '],
                 [' ', ' ',' ']]
    
        
        
def play():        
    start()
    while game_over == False:
        choice()
    reset()
    
play()
