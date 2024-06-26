#!/usr/bin/python3
"""Script that takes an arg and disp values in the states table"""

import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC;""")
    results = cur.fetchall()

    for state in results:
        print(state)
