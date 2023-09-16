#!/usr/bin/python3
# Lists all sstaes from database
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <mysql name>
import sys
import MySQLdb

def list_states(username, password, database):
    # connect to db
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    c = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print
    for row in rows:
        print(row)

    # Close db
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
