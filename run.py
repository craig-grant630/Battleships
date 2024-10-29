import random

BOARD_SIZE = 10
DIRECTION = ["N","S","E","W"]
SHIP_SIZES = [3,2,2]

def create_board():
    #create a list of 
    #list with a borard size of 10
    return [["O"]*10 for x in range(BOARD_SIZE)]

def print_display_boards(user_board, computer_board):
    #Print the boards the user will see and update
    #Iterate through each row and join the list with spaces
    for i in range(BOARD_SIZE):
        user_board_row = ("  ").join(user_board[i])
        computer_board_row = ("  ").join(computer_board[i])
        print(f"{user_board_row}    {computer_board_row}")
    print("")


def get_computer_ship(board):
    #Get a randomly placed staring point and direction
    #check to see if it will fit on the board
    #place ship on the board

    print("Computer is placing ship \n")
    for ship_size in SHIP_SIZES:
        placed = False
        while not placed:
            computer_row_place = random.randint(0,BOARD_SIZE- 1)
            computer_col_place = random.randint(0,BOARD_SIZE -1)
            computer_direction = random.choice(DIRECTION)
            validate_ship_placement(computer_direction, computer_row_place,computer_col_place,ship_size)
            place(computer_row_place, computer_col_place, computer_direction, ship_size, board)
            placed = True

# More Validations will be needed for overlapping boats
def validate_ship_placement(direction, row, column, ship_size):
    # Make sure the ship is placed in the boundaries of the board
    if direction == "N":
        if row - ship_size <= -1:
            return False
    elif direction == "S":
        if row + ship_size > BOARD_SIZE:
            return False
    elif direction == "E":
        if column + ship_size > BOARD_SIZE:
            return False
    elif direction == "S":
        if column - ship_size <= -1:
            return False

def place(row, column, direction, ship_size, board):
    #Place ships on the board according to ship size and direction
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

def play_game():
    computer_board = create_board()
    user_board = create_board()
    print_display_boards(user_board, computer_board)
    get_computer_ship(computer_board)
    print_display_boards(user_board, computer_board)
    
play_game()