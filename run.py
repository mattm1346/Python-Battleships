from random import randint

# Define two boards
# HIDDEN_BOARD that computer has placed
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
# SHOWN_BOARD that shows player guess
SHOWN_BOARD = [[' '] * 8 for i in range(8)]
    

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
    while True:
        try: 
            row = input("Enter the row guess between 1 and 8: \n")
            if row in '12345678':
                row = int(row) - 1
                break
        except ValueError:
            print('Error, please enter a valid number between 1 and 8')
    while True:
        try: 
            column = input("Enter the column guess between A and H: \n").upper()
            if column in 'ABCDEFGH':
                column = letters_to_numbers[column]
                break
        except ValueError:
            print('Error, please enter a valid letter between A-H')
    return row, column


# Check if all ships are hit
def count_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


# Run Game function
if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print('Welcome to Battleships')
        # Print computer board so player has idea of where to guess
        print_board(SHOWN_BOARD)
        row, column = locate_ships()
        # Check if player guesses in same place
        if SHOWN_BOARD[row][column] == "-":
            print("Error, You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("HIT")
            SHOWN_BOARD[row][column] = "X" 
            turns -= 1
        else:
            print("MISS!")
            SHOWN_BOARD[row][column] = "-"   
            turns -= 1
        if count_hits(SHOWN_BOARD) == 5:
            print("CONGRATULATIONS, YOU WIN!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")
            print_board(HIDDEN_BOARD)