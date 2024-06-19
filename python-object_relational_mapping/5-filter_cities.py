#!/usr/bin/python3
"""Script that takes name of state as arg and lists all cities"""
import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("""SELECT cities.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name = '{}'
                ORDER BY states.id ASC;""".format(
                sys.argv[4].replace("'", ""))
                )
    results = cur.fetchall()

    cities_results = []

    for result in results:
        cities_results.append(result[0])

    print(", ".join(cities_results))

    cur.close()
    db.close()

