-- List all records of the database
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;