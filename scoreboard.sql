-- scoreboard database for minesweeper project, Kat
CREATE TABLE IF NOT EXISTS Scoreboard (player_name varchar(3), player_score int);

INSERT or IGNORE INTO Scoreboard(player_name, player_score)
VALUES('KJK', 12);

SELECT * FROM Scoreboard;