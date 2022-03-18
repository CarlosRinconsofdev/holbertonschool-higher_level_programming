-- This script show how to list the number of records 
-- with the same score in a table in a database in a MySQL server
SELECT score, COUNT(SCORE) 
AS NUMBER FROM second_table 
GROUP BY score ORDER BY score DESC;
