import sqlite3
def setup_database(): #sets up my database, Kat
    connection = sqlite3.conncet("Scoreboard.db")
    cursor = connection.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS Scoreboard (
                    player_name TEXT, 
                    player_score INTERGER
                    )               
                """)
    
    connection.commit()
    connection.close()
    
def add_player_name(player_name, player_score): #should allow the user to input a name to go along with their score
    connection = sqlite3.conncet("Scoreboard.db")
    cursor = connection.cursor()
    
    cursor.execute
    insert_query = "INSERT INTO Scoreboard (player_name, player_score) VALUES(?, ?)",
    (player_name, player_score)
    
    connection.commit()
    connection.close()
    
def get_top_scores(): #should get the top ten scores and show them from the database, Kat
    connection = sqlite3.conncet("Scoreboard.db")
    cursor = connection.cursor()
    
    cursor.execute(""" 
                   SELECT player_name, player_score
                   FROM scores
                   ORDER BY player_score DESC
                   LIMIT 10
                   """)
    scores = cursor.fetchall()
    
    connection.close()
    return scores