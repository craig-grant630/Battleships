import random

BOARD_SIZE = 10
DIRECTION = ["N", "S", "E", "W"]
SHIP_SIZES = [2]


def create_board():
    # create a list of
    # list with a borard size of 10
    return [["O"]*10 for x in range(BOARD_SIZE)]


def print_display_boards(user_board, computer_board):
    # Print the boards the user will see and update
    #Titles for boards
    print(" "*9 + "Users Board" + " "*20 + "Computers Board")
    # Add speration
    print("-"*67)
    #Add column labels
    column_label = "  " + ("  ").join(map(str, range(BOARD_SIZE)))
    print(column_label +" "*6 + column_label)
    # Iterate through each row and join the list with spaces
    for i in range(BOARD_SIZE):
        user_board_row = str(i) + " " + ("  ").join(user_board[i])
        computer_board_row = str(i) + " " + ("  ").join(computer_board[i])
        print(f"{user_board_row}  ||  {computer_board_row}")
    print("")

def get_computer_ship(board):
    # Get a randomly placed staring point and direction
    # check to see if it will fit on the board
    # place ship on the board

    print("Computer is placing ships... \n")
    for ship_size in SHIP_SIZES:
        placed = False
        while not placed:
            comp_row = random.randint(0, BOARD_SIZE - 1)
            comp_col = random.randint(0, BOARD_SIZE - 1)
            comp_dir = random.choice(DIRECTION)
            if validate_ship(comp_dir, comp_row, comp_col, ship_size, board):
                place(comp_row, comp_col, comp_dir, ship_size, board)
                placed = True

def get_user_ship(user_board, board):
    # intake the display boards and update the users board when 
    print("Time to place your ships!")
    for ship_size in SHIP_SIZES:
        placed = False
        try:
            while not placed:
                user_row = int(input(f"Enter row for ship length {ship_size}: "))
                user_column = int(input(f"Enter column for ship length {ship_size}: "))
                user_dir = input("Enter your direction (N,S,E,W): \n").upper()
                if user_dir in DIRECTION:
                    if validate_ship(user_dir, user_row, user_column, ship_size, user_board):
                        place(user_row, user_column, user_dir, ship_size, user_board)
                        print_display_boards(user_board, board)
                        placed = True
                    else:
                        print("Placement Invalid")
                else:
                    print("Invalid Direction")
        except:
            print("Invalid Input")

def validate_ship(direction, row, column, ship_size, board):
    # Make sure the ship is placed in the boundaries of the board
    if direction == "N":
        if row - ship_size <= -1:
            return False
        for y in range(ship_size):
            if board[row - y][column] == "S":
                return False
    elif direction == "S":
        if row + ship_size > BOARD_SIZE:
            return False
        for y in range(ship_size):
            if board[row + y][column] == "S":
                return False
    elif direction == "E":
        if column + ship_size > BOARD_SIZE:
            return False
        for x in range(ship_size):
            if board[row][column + x] == "S":
                return False
    elif direction == "W":
        if column - ship_size <= -1:
            return False
        for x in range(ship_size):
            if board[row][column - x] == "S":
                return False
    return True

def place(row, column, direction, ship_size, board):
    # Place ships on the board according to ship size and direction and starting point
    if direction == "N":
        for i in range(ship_size):
            board[row - i][column] = "S"
    elif direction == "S":
        for i in range(ship_size):
            board[row + i][column] = "S"
    elif direction == "E":
        for i in range(ship_size):
            board[row][column + i] = "S"
    elif direction == "W":
        for i in range(ship_size):
            board[row][column - i] = "S"

def user_guess(computer_board, computer_display_board, user_board):
    print("Time to Start Firing")
    print("Start guessing!")
    try:
        u_guess_row = int(input("Guess a row: "))
        u_guess_col = int(input("Guess a column: "))
        if computer_display_board[u_guess_row][u_guess_col] != "O":
            print("You have already guessed this, try again")
        elif computer_board[u_guess_row][u_guess_col] == "S":
            print("Hit")
            computer_display_board[u_guess_row][u_guess_col] = "X"
            print_display_boards(user_board, computer_display_board)
        elif computer_board[u_guess_row][u_guess_col] == "O":
            print("Miss")
            computer_display_board[u_guess_row][u_guess_col] == "-"
            print_display_boards(user_board, computer_display_board)
    except:
        print("Invalid Input")


def play_game():
    computer_board = create_board()
    user_board = create_board()
    computer_display_board = create_board()
    print("Initial Boards \n")
    print_display_boards(user_board, computer_display_board)
    get_computer_ship(computer_board)
    print(computer_board)
    get_user_ship(user_board, computer_display_board)
    user_guess(computer_board, computer_display_board, user_board)
    


play_game()
