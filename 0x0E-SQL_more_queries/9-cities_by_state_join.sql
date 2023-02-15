-- script that list all cities of astate
SELECT cities.id, cities.name
FROM cities, states
INNER JOIN states on cities.state_id=state.id
ORDER BY cities.id ASC;
