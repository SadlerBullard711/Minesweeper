from play import play_game
from scoreboard import get_top_scores, setup_database


def main():

    setup_database()

    #Give the player the choice to play, view scoreboad, or quit.
    print("Welcome to Minesweeper!")

    while True:
        print("Please choose to [Play] the game, view the [Scoreboard], or [Quit]")

        action = input("> ")
        action = action.lower()

        actions = ["play", "scoreboard", "quit"]

        #check for bad inputs.
        while action not in actions:
            print("Invalid action!")
            action = input("> ")

        #if the player chooses to Play, run the game.
        if action == actions[0]:
            play_game()

        #else if the player chooses to view the scoreboad, view the scoreboard.
        elif action == actions[1]:
            get_top_scores()

        #else quite the game.
        elif action == actions[2]:
            print("Thank you for playing!")
            return

if __name__ == "__main__":
    main()