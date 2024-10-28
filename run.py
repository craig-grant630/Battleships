BOARD_SIZE = 10

def create_board():
    #create a list of 
    #list with a borard size of 10
    return [["O"]*10 for x in range(BOARD_SIZE)]

def print_display_boards(user_board, computer_board):
    #Print the boards the user will see and update
    #Iterate through each row and join the list with spaces
    for i in range(BOARD_SIZE):
        user_board_row = (" ").join(user_board[i])
        computer_board_row = (" ").join(computer_board[i])
        print(f"{user_board_row}    {computer_board_row}")

def play_game():
    computer_board = create_board()
    user_board = create_board()
    print_display_boards(user_board, computer_board)

play_game()