BOARD_SIZE = 10

def create_board():
    # A function to create a list of 
    #list with a borard size of 10
    return [["O"]*10 for x in range(BOARD_SIZE)]

def play_game():
    computer_board = create_board()
    user_board = create_board()

