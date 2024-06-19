#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         port=3306, pw=password, db_name=database_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`")

    rows = cur.fetchall()
    
    for row in rows:
        print(row)

        cur.close()
        db.close()
