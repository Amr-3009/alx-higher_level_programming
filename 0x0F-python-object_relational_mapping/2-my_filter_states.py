#!/usr/bin/python3
"""
MySQL Database Query Script

This script connects to a MySQL database, executes a SELECT query with a WHERE
clause, and retrieves rows from the "states" table based on a provided name
filter. The results are printed to the console.

Usage:
    python script.py <username> <password> <database_name> <name_filter>

Parameters:
    <username>: MySQL database username.
    <password>: Password for the specified user.
    <database_name>: Name of the MySQL database.
    <name_filter>: A filter to select rows from the "states" table based on the
                  'name' column.

Dependencies:
    - MySQLdb module (MySQL-python): This script requires the MySQLdb module to
      be installed. You can install it using:
        pip install MySQL-python

Example:
    python script.py myuser mypassword mydatabase 'N%'

Note:
    Before running the script, make sure to replace "myuser," "mypassword," and
    "mydatabase" with your MySQL username, password, and database name.

Workflow:
1. Establish a connection to the specified MySQL database using the provided
   username, password, and database name.
2. Create a cursor object to interact with the database.
3. Build an SQL query with a WHERE clause based on the provided name filter.
4. Execute the SQL query.
5. Fetch all rows returned by the query.
6. Print each row to the console.
7. Close the database cursor.
8. Close the database connection.

"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Build an SQL query with a WHERE clause based on the provided name filter
    name_filter = argv[4]
    sql_query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(
        name_filter
    )
    cur.execute(sql_query)

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Print each row to the console
    for row in rows:
        print(row)

    # Close the database cursor
    cur.close()

    # Close the database connection
    db.close()
