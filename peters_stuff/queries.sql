DROP TABLE AllStarBatters;
CREATE TABLE AllStarBatters AS select * FROM Batting LEFT OUTER JOIN AllstarFull USING (playerID, teamID, lgID, yearID) LEFT OUTER JOIN Master USING (playerID);
