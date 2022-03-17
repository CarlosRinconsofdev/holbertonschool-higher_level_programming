-- This script show how to list all records in a second table 
-- with a score >= 10 in a  DataBase in MySQL server
SELECT score, name FROM second_table WHERE score >= 10
ORDER BY score DESC;
