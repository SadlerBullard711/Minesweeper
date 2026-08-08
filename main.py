import gameboard, play, scoreboard

def main():

    scoreboard.setup_database()

    #Give the player the choice to play, view scoreboad, or quit.
    print("Welcome to Minesweeper!")

    while True:
        print("Please choose to [Play] the game, view the [Scoreboard], or [Quit]")

        action = input("> ")

        actions = ["play", "scoreboard", "quit"]

        #check for bad inputs.
        while action.lower() not in actions:
            print("Invalid action!")
            action = input("> ")

        #if the player chooses to Play, run the game.
        if action.lower == actions[0]:
            
    


    pass

if __name__ == "__main__":
    main()