import time
from scoreboard import * 

def get_coordinates():

    while True:
        row = input("Enter row (0-9): ")
        column = input("Enter column (0-9): ")

        if row.isdigit() and column.isdigit():
            row = int(row)
            column = int(column)

            if 0 <= row <= 9 and 0<= column <= 9:
                return row, column

            print("Invalid coordinates. Please enter numbers from 0-9.")

def get_action(): 

    while True:
        action = input("Reveal [r] or Flag [f]? ").lower()

        if action == "r" or action == "f":
            return action

        print("Invalid action. Enter [r] or [f] to flag.")

def play_game():
    board = board()
    board.setup()
    board.place_mines()

    start_time = time.time()

    while True: 
        board.draw_board()

        row, column = get_coordinates()
        action = get_action()

        cell = board.board[row][column]

        if action == "r":
            cell.revealed = True

            if cell.mine:
                board.draw_board()
                print("Game Over! You hit a mine!")
                break

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
            cell.flag = not cell.flag

        else:
            print("Invalid action.")

                