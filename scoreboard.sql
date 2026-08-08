-- scoreboard database for minesweeper project, Kat
CREATE TABLE IF NOT EXISTS Scoreboard (player_name VARCHAR(3) UNIQUE, player_score INT);

INSERT or IGNORE INTO Scoreboard(player_name, player_score)
VALUES('KJK', 12);

SELECT player_name as 'PLAYER', player_score as 'High Score'
FROM Scoreboard;