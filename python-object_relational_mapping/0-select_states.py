#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")

    results = cur.fetchall()

    for state in results:
        print(state)
