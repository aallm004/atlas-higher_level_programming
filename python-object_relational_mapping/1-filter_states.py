#!/usr/bin/python3
"""Script that lists all states with name starting with N"""

import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("""SELECT * FROM states WHERE
                BINARY name LIKE 'N%' ORDER BY id""")

    results = cur.fetchall()

    for state in results:
        print(state)
