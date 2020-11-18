# Tic-Tac-Toe

#
# Global variables
#

# TODO: Define your global variables here

# Game loop
is_running = False

# Players

# Game board

def initalize_game():
    pass

    # TODO: Initialize your game board. Hint: All spaces should have '#'
    
    
    # TODO: Assign players by calling your assign_players() function
    

    # TODO: Initialize player turn to player 1

def display_board(board):
    pass

    # TODO: Print the game board

def place_marker(board, player, position):
    # TODO: Place the player marker on the board at position and return the board
    pass

def check_space(board, position):
    # TODO: Check if position on the board is empty
    pass

def player_choice(player, board):
    # TODO: Ask the player to choose a space on the board,
    # Check if the player choice is valid (between 0-8)
    # Check if the player choice is empty
    pass

def assign_players():
    player1 = input("\nPlease pick a marker 'X' or 'O': ")
    while True:
        # TODO: Check if player1 chose 'X', then set player2 to 'O' and return the players 
        # Do not forget to check the other cases.
        pass

def check_board_full(board):
    # TODO: Check if the board is full by counting the number of spaces left.
    pass

def check_win(board, mark):
    # TODO: Check rows for a win
    pass

    # TODO: Check coloumns for a win
    pass

    # TODO: Check diagonals for a win
    pass

def replay():
    # TODO: Ask if the player wishes to start a new game
    pass

# DO NOT CHANGE THE LINE BELOW

if __name__ == "__main__":
    print('\nWelcome to Tic-Tac-Toe!')
    
    # TODO: Call you initialize_game() function
    
    while is_running:
        pass
        
        # TODO: Check if the board is full
        
        # TODO While the board is not full
        
        # TODO: Check if the player_turn value is odd or even, and set marker to the correct player
            
        # TODO: Call your player_choice() function to ask the user for a position

        # TODO: Call your place_marker() function to place the marker on the board

        # TODO: Display the board

        # TODO: Increment the player turn counter

        # TODO: Check if there is a winner on the board
        
        # TODO: Check if the user wishes to play again
    