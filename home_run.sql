<<<<<<< Updated upstream
(SELECT "yearID", "G", "R", "H", "2B", "3B", "HR", "RBI", "salary", "playerID", "weight", "height", "bats", "debut", "AB", "SO", "BB", "IBB", "SH", "SF", "GIDP", "birthYear")
=======
(SELECT "yearID", "G", "R", "H", "2B", "3B", "HR", "salary", "playerID", "weight", "height", "bats", "debut", "AB", "SO", "BB", "IBB", "SH", "SF", "GIDP", "birthYear")
>>>>>>> Stashed changes
UNION
(SELECT Batting.yearID, G, R, H, 2B, 3B, HR, RBI,
       salary,
       Master.playerID, weight, height, bats, debut, 
       AB, SO, BB, IBB, SH, SF, GIDP, birthYear
FROM Batting
JOIN Salaries USING(yearID, playerID, lgID)
LEFT JOIN Master USING(playerID)
INTO OUTFILE "/Users/peterchu/test.csv"
FIELDS ENCLOSED BY '"'
TERMINATED BY ';'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n');

