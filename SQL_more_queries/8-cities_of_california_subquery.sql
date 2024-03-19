-- List the cities that can be find in the database
SELECT cities.id, cities.name FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;