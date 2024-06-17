--script that lists all cities containeed in database
SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states ON state.id = cities.states_id
ORDER BY cities.id;
