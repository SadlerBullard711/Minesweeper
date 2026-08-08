import sqlite3
def setup_database(): #sets up my database, Kat
    connection = sqlite3.connect("Scoreboard.db")
    cursor = connection.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS Scoreboard (
                    player_name TEXT, 
                    player_score INTEGER
                    );               
                """)
    cursor.execute("""
                    INSERT or IGNORE INTO Scoreboard (player_name, player_score)
                    VALUES('KJK', 12),
                    ('V', 277),
                    ('King of Pop', 350),
                    ('Perfect Cell', 1000),
                    ('Tarnished', 1),
                    ('The World', 999),
                    ('Marco', 500),
                    ('Mississippi', 480),
                    ('Jason', 130),
                    ('Melly', 772);  
                   """)
    cursor.execute("""
                    SELECT * 
                    FROM Scoreboard
                    ORDER BY player_score
                    DESC; 
                   """)
    
    connection.commit()
    connection.close()
    
def add_player_name(player_name, player_score): #should allow the user to input a name to go along with their score, Kat
    connection = sqlite3.connect("Scoreboard.db")
    cursor = connection.cursor()
    
    cursor.execute(
        "INSERT INTO Scoreboard (player_name, player_score) VALUES(?, ?)",
        (player_name, player_score)
    )

    connection.commit()
    connection.close()
    
def get_top_scores(): #should get the top ten scores and show them from the database, Kat
    connection = sqlite3.connect("Scoreboard.db")
    cursor = connection.cursor()
    
    cursor.execute(""" 
                   SELECT player_name, player_score
                   FROM Scoreboard
                   ORDER BY player_score DESC
                   LIMIT 10
                  """)
    scores = cursor.fetchall()
    print(scores)
    connection.close()
    