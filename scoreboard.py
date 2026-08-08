import sqlite3
def setup_database():
    connection = sqlite3.conncet("Scoreboard.db")
    cursor = connection.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS Scoreboard (
                    player_name TEXT, 
                    player_score INTERGER
                    )               
                """)
    input_name = input("ENTER NAME: ")
    input_player_score = int(input("ENTER SCORE: "))
    insert_query = "INSERT INTO Scoreboard (player_name, player_score)"