(SELECT "yearID", "G", "R", "H", "2B", "3B", "HR", "playerID", "weight", "height", "bats", "debut")
UNION
(SELECT Batting.yearID, G, R, H, 2B, 3B, HR,
       Master.playerID, weight, height, bats, debut
FROM Batting
LEFT JOIN Master ON Master.playerID = Batting.playerID
INTO OUTFILE "test.csv"
FIELDS ENCLOSED BY '"'
TERMINATED BY ';'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n');
