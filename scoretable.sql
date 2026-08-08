-- scoreboard database for minesweeper project, Kat

CREATE TABLE IF NOT EXISTS Scoreboard (player_name VARCHAR(25) UNIQUE, player_score INT);

INSERT or IGNORE INTO Scoreboard(player_name, player_score)
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
--SELECT player_name as 'PLAYER', player_score as 'HIGH SCORE'
SELECT * 
FROM Scoreboard
ORDER BY player_score
DESC;