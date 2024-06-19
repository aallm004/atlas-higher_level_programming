#!/usr/bin/python3
"""Script that lists all states from db"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    sql_code = "SELECT * FROM `states` ORDER BY `id`"

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute(sql_code)

    # Fetch all results
    res = cursor.fetchall()

    # Print the results
    for row in res:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
