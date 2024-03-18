-- List number of data with same value
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;