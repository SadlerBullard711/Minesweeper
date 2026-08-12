import time
from gameboard import Board
from scoreboard import add_player_name 


def get_coordinates():
    """Get and validate a row and column entered by the player.

    Prompts the player to enter two numbers between 0 and 9.
    Continues asking until valid coordinates are entered.

    Returns:
        tuple: The row and column as integers.
"""

    while True:
        coordinates = input("Enter row and column: ('ex: 0 0'): ").split()

        if len(coordinates) == 2:
            row, column = coordinates

            if row.isdigit() and column.isdigit():
                row = int(row)
                column = int(column)

                if 0 <= row <= 9 and 0 <= column <= 9:
                    return row, column

        print("Invalid coordinates. Please enter numbers from 0-9.")

def get_action():
    """Get the player's requested action.

    Prompts the player to choose between revealing a cell ('r')
    or flagging a cell ('f').

    Returns:
        str: 'r' to reveal or 'f' to flag.
    """

    while True:
        action = input("Reveal [r] or Flag [f]? ").lower()

        if action == "r" or action == "f":
            return action

        print("Invalid action. Enter [r] or [f] to flag.")

def play_game():
    """Run a complete game of Minesweeper. 
    
    Creates a game board and repeatedly allows the player to
    reveal or flag cells. The game ends when the player hits
    a mine or reveals all safe cells. 

    A score is calculated based on the player's completion time
    and saved to the SQLite scoreboard when the player wins.
    """
    board = Board()
   
    start_time = time.time()

    while True: 
        board.draw_board()

        row, column = get_coordinates()
        action = get_action()

        cell = board.board[row][column]

        if action == "r":
            if cell.flagged:
                print("This cell is flagged. Unflag it before revealing.")
                continue

            coordinate = [row, column]
            cell.reveal(board)

            
            if cell.mine:
                board.draw_board()
                print("Game Over! You hit a mine!")
                break

            if cell.number == 0:
                reveal_adjacent(board, coordinate)

            if board.unrevealed == 0:
                end_time = time.time()
                elapsed_time = end_time - start_time
                player_score = max(0, 1000 -int(elapsed_time))

                board.draw_board()
                print("Congratulations! You won!")
                print(f"Your score: {player_score}")

                player_name = input("Enter your name: ")

                add_player_name(player_name, player_score)

                break
        elif action == "f":
            cell.toggle_flag()

        else:
            print("Invalid action.")


def reveal_adjacent(board: Board, coordinate): #coordinate is a list [row, column]
    """Recursively reveal safe cells adjacent to an empty cell.
    
    Checks the cells surrounding the given coordinate. Safe, 
    unrevealed cells are revealed. If an adjacent cell has no
    neighboring mines, this function calls itself recursively
    to reveal that cell's neighbors. 

    Args:
        board(Board): The current Minesweeper game board.
        coordinate (list): THe row and column of the cell being checked.
    """

    if (coordinate[0] != 0) and (coordinate[1] != 0):
        top_left = board.board[coordinate[0] - 1][coordinate[1] - 1]
        if not top_left.revealed and not top_left.mine:
            top_left.reveal(board)
            if top_left.number == 0:
                new_coordinate = [coordinate[0] - 1, coordinate[1] - 1]
                reveal_adjacent(board, new_coordinate)

    if (coordinate[0] != 0) and (coordinate[1] != board.size - 1):
        top_right = board.board[coordinate[0] - 1][coordinate[1] + 1]
        if not top_right.revealed and not top_right.mine:
            top_right.reveal(board)
            if top_right.number == 0:
                new_coordinate = [coordinate[0] - 1, coordinate[1] + 1]
                reveal_adjacent(board, new_coordinate)

    if (coordinate[0] != 0):
        top_middle = board.board[coordinate[0] - 1][coordinate[1]]
        if not top_middle.revealed and not top_middle.mine:
            top_middle.reveal(board)
            if top_middle.number == 0:
                new_coordinate = [coordinate[0] - 1, coordinate[1]]
                reveal_adjacent(board, new_coordinate)
            
    if (coordinate[0] != board.size - 1) and (coordinate[1] != 0):
        bottom_left = board.board[coordinate[0] + 1][coordinate[1] - 1]
        if not bottom_left.revealed and not bottom_left.mine:
            bottom_left.reveal(board)
            if bottom_left.number == 0:
                new_coordinate = [coordinate[0] + 1, coordinate[1] - 1]
                reveal_adjacent(board, new_coordinate)
            
    if (coordinate[0] != board.size - 1) and (coordinate[1] != board.size -1):
        bottom_right = board.board[coordinate[0] + 1][coordinate[1] + 1]
        if not bottom_right.revealed and not bottom_right.mine:
            bottom_right.reveal(board)
            if bottom_right.number == 0:
                new_coordinate = [coordinate[0] + 1, coordinate[1] + 1]
                reveal_adjacent(board, new_coordinate)

    if (coordinate[0] != board.size - 1):
        bottom_middle = board.board[coordinate[0] + 1][coordinate[1]]
        if not bottom_middle.revealed and not bottom_middle.mine:
            bottom_middle.reveal(board)
            if bottom_middle.number == 0:
                new_coordinate = [coordinate[0] + 1, coordinate[1]]
                reveal_adjacent(board, new_coordinate)

    if (coordinate[1] != 0):
        middle_left = board.board[coordinate[0]][coordinate[1] - 1]
        if not middle_left.revealed and not middle_left.mine:
            middle_left.reveal(board)
            if middle_left.number == 0:
                new_coordinate = [coordinate[0] , coordinate[1] - 1]
                reveal_adjacent(board, new_coordinate)

    if (coordinate[1] != board.size - 1):
        middle_right = board.board[coordinate[0]][coordinate[1] + 1]
        if not middle_right.revealed and not middle_right.mine:
            middle_right.reveal(board)
            if middle_right.number == 0:
                new_coordinate = [coordinate[0] , coordinate[1] +1]
                reveal_adjacent(board, new_coordinate)

                