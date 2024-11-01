import random

BOARD_SIZE = 10
DIRECTION = ["N", "S", "E", "W"]
SHIP_SIZES = [2, 2, 3, 4, 5]


def create_board():
    # create a list of
    # list with a borard size of 10
    return [["O"]*10 for x in range(BOARD_SIZE)]


def print_display_boards(user_board, computer_board):
    # Print the boards the user will see and update
    # Titles for boards
    print(" "*9 + "Users Board" + " "*20 + "Computers Board")
    # Add speration
    print("-"*67)
    # Add column labels
    column_label = "  " + ("  ").join(map(str, range(BOARD_SIZE)))
    print(column_label + " "*6 + column_label)
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
    print("Time to place your ships! \n")
    for ship_size in SHIP_SIZES:
        placed = False
        try:
            while not placed:
                user_row = int(input(
                    f"Enter row for ship length {ship_size}: \n"))
                user_column = int(input(
                    f"Enter column for ship length {ship_size}: "))
                user_dir = input("Enter your direction (N,S,E,W): \n").upper()
                print("")
                if user_dir in DIRECTION:
                    if validate_ship(
                                    user_dir, user_row, user_column,
                                    ship_size, user_board):
                        place(
                            user_row, user_column,
                            user_dir, ship_size, user_board)
                        print_display_boards(user_board, board)
                        placed = True
                    else:
                        print("Placement Invalid \n")
                else:
                    print("Invalid Direction \n")
        except ValueError:
            print("Invalid Input! \n")


def validate_ship(direction, row, column, ship_size, board):
    # Make sure the ship is placed in the boundaries of the board
    if row < 0 or row > 9 or column < 0 or column > 9:
        return False
    elif direction == "N":
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
    # Place ships on the board according to ship
    # size and direction and starting point
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
    # this will take in users input to update the the boards
    guessing = True
    while guessing:
        try:
            u_guess_row = int(input("Guess a row: \n"))
            u_guess_col = int(input("Guess a column: \n"))
            if (u_guess_col < 0 or u_guess_col > 9 or u_guess_row or
                    u_guess_row > 9):
                print("Invalid guess \n")
            elif computer_display_board[u_guess_row][u_guess_col] != "O":
                print("You have already guessed this, try again")
            elif computer_board[u_guess_row][u_guess_col] == "S":
                print("You Hit \n")
                computer_display_board[u_guess_row][u_guess_col] = "X"
                guessing = False
            elif computer_board[u_guess_row][u_guess_col] == "O":
                print("You Missed \n")
                computer_display_board[u_guess_row][u_guess_col] = "-"
                guessing = False
        except ValueError:
            print("Invalid Input \n")


def computer_guess(computer_display_board, user_board):
    # this will create a guess with random numbers
    # It will update the board with either a hit or a miss
    print("Computers Turn")
    guessing = True
    while guessing:
        comp_guess_row = random.randint(0, BOARD_SIZE - 1)
        comp_guess_col = random.randint(0, BOARD_SIZE - 1)
        if user_board[comp_guess_row][comp_guess_col] == "S":
            print("Computer Hit \n")
            user_board[comp_guess_row][comp_guess_col] = "X"
            print_display_boards(user_board, computer_display_board)
            guessing = False
        elif user_board[comp_guess_row][comp_guess_col] == "O":
            print("Computer Missed \n")
            user_board[comp_guess_row][comp_guess_col] = "-"
            print_display_boards(user_board, computer_display_board)
            guessing = False
        else:
            guessing = True


def game_check(board):
    # This will check if the game ends
    # It will see how many hits there have been on the board
    # This will be retured to the main loop
    count = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == "X":
                count = count + 1
    return count


def play_game():
    # This is the main loop for the game
    computer_board = create_board()
    user_board = create_board()
    computer_display_board = create_board()
    print("")
    print("Initial Boards \n")
    print_display_boards(user_board, computer_display_board)
    get_computer_ship(computer_board)
    get_user_ship(user_board, computer_display_board)
    print("Time to Start Firing")
    print("Start guessing! \n")
    turn = 1
    while True:
        print(f"Turn: {turn}")
        user_guess(computer_board, computer_display_board, user_board)
        check_user_win = game_check(computer_display_board)
        if check_user_win == sum(SHIP_SIZES):
            print("Congratulations you have sunk all the ships, You Win")
            break
        computer_guess(computer_display_board, user_board)
        check_computer_wins = game_check(user_board)
        if check_computer_wins == sum(SHIP_SIZES):
            print("The computer has sunk all you ships, computer wins")
            break
        turn = turn + 1


play_game()
