#!/usr/bin/python3
#!/usr/bin/python3
"""Script that takes name of state as arg and lists all cities"""
import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute(""""SELECT cities.name FROM cities INNER JOIN states ON \
                cities.state_id = states.id WHERE states.name = %s \
                ORDER BY cities.id ASC", (argv[4],)""")
    results = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    db.close()
