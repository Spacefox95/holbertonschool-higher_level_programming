-- List record with a score >= 10
-- Lists all records of the "second" table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;