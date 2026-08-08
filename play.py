import time

from database import add_player_score

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

                add_player_score(player_name, player_score)
                break
        elif action == "f":
            cell.flag = not cell.flag

        else:
            print("Invalid action.")

                