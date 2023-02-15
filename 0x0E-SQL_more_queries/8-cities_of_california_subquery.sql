-- script that list all cities of astate
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = state.id AND states.name = 'California'
ORDER BY cities.id ASC;
