import random

BOARD_SIZE = 10
SHIP_SIZES = [5,4,3,3,2]
DIRECTION = ["N","S","E","W"]

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

#def computers_ship_placement():
#loop through different ship sizes
#for ship_size in SHIP_SIZES:
#placed = False
#loop until all ships are placed correclty
#while not placed:
#computer_row_place = random.randint(0,BOARD_SIZE- 1)
#computer_col_place = random.randint(0,BOARD_SIZE -1)
#computer_direction = random.choice(DIRECTION)
#Going to need to check see if this can be used - another function required
#Will next then need to place the ship on the computers board - another function required
#If checks are good then placed = True 




def play_game():
    computer_board = create_board()
    user_board = create_board()
    print_display_boards(user_board, computer_board)


play_game()