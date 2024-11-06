import random

BOARD_SIZE = 10
DIRECTION = ["N", "S", "E", "W"]
SHIP_SIZES = [2, 2, 3, 4, 5]


def rules():
    # This function will explain the rules to the user,
    # and ask if the user is ready to start the game
    print("Welcome to Battleships\n")
    print("Rules:\n")
    print("1. The goal of the game is to sink all of your opponent's ships "
          "before they sink yours.")
    print("2. You are playing against the computer, and there will be two "
          "10x10 game boards.")
    print("3. There are five ships of varying sizes: two 2-length ships, "
          "one 3-length ship, one 4-length ship, and one 5-length ship.")
    print("4. Ships can be placed either vertically (N or S) or horizontally "
          "(E or W).")
    print("5. Players take turns guessing the coordinates of their opponent's "
          "ships.")
    print("6. When making a guess, if the coordinates correspond to a ship, "
          "it's considered a 'hit' (marked with 'X').")
    print("7. If the guess does not hit a ship, it's considered a 'miss' "
          "(marked with '-').")
    print("8. The game continues until one player has sunk all of their "
          "opponent's ships.\n")
    ready = input("Are you ready to start? (press any key)")


def create_board():
    # Create a 10x10 grid using lists
    return [["O"]*10 for x in range(BOARD_SIZE)]


def print_display_boards(user_board, computer_board):
    # This function has parameters user_board and computer_board,
    # each parameter is s 10x10 grid using the create_board function

    #  Titles for boards
    print(" "*9 + "Users Board" + " "*20 + "Computers Board")
    # Add speration line for readablility
    print("-"*67)
    # Add column labels
    column_label = "  " + ("  ").join(map(str, range(BOARD_SIZE)))
    print(column_label + " "*6 + column_label)
    # Iterate through each row and join the list with spaces instead of ","
    for i in range(BOARD_SIZE):
        user_board_row = str(i) + " " + ("  ").join(user_board[i])
        computer_board_row = str(i) + " " + ("  ").join(computer_board[i])
        print(f"{user_board_row}  ||  {computer_board_row}")
    print("")


def get_computer_ship(board):
    # This function will have a parameter for a board,
    # specifically the computers board that is hidden, and place the computers
    # ships

    # It will first get a randomly placed staring point (row and column),
    # then randomly choose a direction from imported random,

    # The function will loop through each ship size
    # and will place the ship on the board until a valid ship placement.

    print("Computer is placing ships... \n")
    for ship_size in SHIP_SIZES:
        placed = False
        while not placed:
            comp_row = random.randint(0, BOARD_SIZE - 1)
            comp_col = random.randint(0, BOARD_SIZE - 1)
            comp_dir = random.choice(DIRECTION)
            # Validate ship function will either return true or false depending
            # on if the ship will fit on the board and there is no overlapping
            # ships already on the board
            if validate_ship(comp_dir, comp_row, comp_col, ship_size, board):
                place(comp_row, comp_col, comp_dir, ship_size, board)
                placed = True


def get_user_ship(user_board, board):
    # This function will use parameters user_board and board,
    # each a 10x10 grid defined with the create board function

    # The function will loop through the different ship sizes asking,
    # the user to input a row, column and direction.

    # The function will keep asking the user until valid inputs or ships are,
    # able to be placed
    print("Time to place your ships! \n")
    for ship_size in SHIP_SIZES:
        placed = False
        while not placed:
            try:
                # Ask the users to input the row column and direction
                user_row = int(input(
                    f"Enter row (0-9) for ship length {ship_size}: \n"))
                user_column = int(input(
                    f"Enter column (0-9) for ship length {ship_size}: \n"))
                user_dir = input("Enter your direction (N,S,E,W): \n").upper()
                print("")
                if user_dir in DIRECTION:
                    # Make sure the ship can be placed and is valid
                    if validate_ship(
                                    user_dir, user_row, user_column,
                                    ship_size, user_board):
                        # If the ship is valid and returns true
                        # place the ship
                        place(
                            user_row, user_column,
                            user_dir, ship_size, user_board)
                        print_display_boards(user_board, board)
                        placed = True
                    else:
                        print("Oh no! Your placement is incorrect \n")
                else:
                    print("Please enter a valid direction: (N,S,E,W) \n")
            except ValueError:
                print("Invalid Input! \n")
                placed = False


def validate_ship(direction, row, column, ship_size, board):
    # This function will take parameters direction, row, column,
    # ship_size and board. The ship_size are the size of the ships defined in,
    # SHIP_SIZES

    # Make sure the row and column are within the bounds of the board,
    # also ensuring depending on direction and the shize of the ship,
    # it is also within bounds.

    # The loop in each if statement will ensure there are no overlapping ships.

    # If the ship can be placed with these conditions then return true,
    # or if not return false.
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
    # Place ships on the board according to starting row, column
    # size and direction and place the ship on the specified board,
    # depending on if the computer is placing or the user.

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
    # This function will take all the boards of 10x10 and determing if,
    # there is a hit or a miss and update the board accordingly.

    # Loop until we have a valid input
    guessing = True
    while guessing:
        try:
            u_guess_row = int(input("Guess a row (0-9): \n"))
            u_guess_col = int(input("Guess a column (0-9): \n"))
            if (u_guess_col < 0 or u_guess_col > 9 or u_guess_row < 0 or
                    u_guess_row > 9):
                print("Your guess is not within the board, try again \n")
            elif computer_display_board[u_guess_row][u_guess_col] != "O":
                print("You have already guessed this, try again")
            elif computer_board[u_guess_row][u_guess_col] == "S":
                print("You have Hit \n")
                computer_display_board[u_guess_row][u_guess_col] = "X"
                guessing = False
            elif computer_board[u_guess_row][u_guess_col] == "O":
                print("You have Missed \n")
                computer_display_board[u_guess_row][u_guess_col] = "-"
                guessing = False
        except ValueError:
            print("Invalid Input \n")


def computer_guess(computer_display_board, user_board):
    # This will have parameters of both the display boards printed to the user,
    # It will generate a random point on the board and determine,
    # a hit or a miss making sure there are no duplicate answers.

    print("Computers Turn")
    guessing = True
    while guessing:
        comp_guess_row = random.randint(0, BOARD_SIZE - 1)
        comp_guess_col = random.randint(0, BOARD_SIZE - 1)
        if user_board[comp_guess_row][comp_guess_col] == "S":
            print("Computer has Hit \n")
            user_board[comp_guess_row][comp_guess_col] = "X"
            print_display_boards(user_board, computer_display_board)
            guessing = False
        elif user_board[comp_guess_row][comp_guess_col] == "O":
            print("Computer has Missed \n")
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

    # Display the rules for the game
    rules()
    # Create the different 10x10 lists
    computer_board = create_board()
    user_board = create_board()
    computer_display_board = create_board()
    print("")
    print("Lets Start! \n")
    # Print the boards the user will need to play the game
    print_display_boards(user_board, computer_display_board)
    # Place the computer ships on the hidden computer board
    get_computer_ship(computer_board)
    # Place the users ships on the users board
    get_user_ship(user_board, computer_display_board)
    print("Time to Start Firing")
    print("Start guessing! \n")
    # Keep track of the amount of turns stating at 1
    turn = 1
    # Loop that will make sure the user and the computer are guessing until
    # check user win or check computer win is satisfied
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
