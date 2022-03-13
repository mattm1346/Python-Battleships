from random import randint

# Player Board (hidden)
PLAYER_BOARD = [[' '] * 8 for x in range(8)]
COMPUTER_BOARD = [[' '] * 8 for i in range(8)]
    

# Convert letters to numbers
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}
# Print board
def print_board(board):
    print("  A B C D E F G H")
    print("  _______________")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

# Computer create ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = locate_ships()
        board[ship_row][ship_column] = "X"

# Guess ship location
def locate_ships():
    # Player guesses ship location
    row = input("Enter the row of the ship (1-8): \n")
    while row not in "12345678":
        print('Error, please select a valid row')
        row = input("Enter the row of the ship (1-8): \n")
    column = input("Enter the column of the ship (A-H): \n").upper()
    while column not in "ABCDEFGH":
        print('Error, please select a valid column')
        column = input("Enter the column of the ship (A-H): \n").upper()
    return int(row) - 1, letters_to_numbers[column]

# Check if all ships are hit
def count_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

# Run Game function
create_ships(PLAYER_BOARD)
turns = 10
while turns > 0:
    print('Welcome to Battleships')
    # Print computer board so player has idea of where to guess
    print_board(COMPUTER_BOARD)
    row, column = locate_ships()
    # Check if player guesses in same place
    if COMPUTER_BOARD[row][column] == "-":
        print("Error, You guessed that one already.")
    elif PLAYER_BOARD[row][column] == "X":
        print("Hit")
        COMPUTER_BOARD[row][column] = "X" 
        turns -= 1
    else:
        print("MISS!")
        PLAYER_BOARD[row][column] = "-"   
        turns -= 1
    if count_hits(COMPUTER_BOARD) == 5:
        print("You win!")
        break
        print("You have " + str(turns) + " turns left")
    if turns == 0:
        print("You ran out of turns")