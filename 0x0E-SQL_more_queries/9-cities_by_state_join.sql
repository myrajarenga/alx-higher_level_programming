-- script that list all cities of astate
SELECT cities.id, cities.name states.name
FROM cities
INNER JOIN states ON cities.state_id=state.id
ORDER BY cities.id ASC;
