#!/usr/bin/python3
"""
MySQL Database Query Script

This script connects to a MySQL database, executes a SELECT query with a JOIN
operation, and retrieves rows from the "cities" and "states" tables. The resul
are printed to the console.

Usage:
    python script.py <username> <password> <database_name>

Parameters:
    <username>: MySQL database username.
    <password>: Password for the specified user.
    <database_name>: Name of the MySQL database.

Dependencies:
    - MySQLdb module (MySQL-python): This script requires the MySQLdb module to
      be installed. You can install it using:
        pip install MySQL-python

Example:
    python script.py myuser mypassword mydatabase

Note:
    Before running the script, make sure to replace "myuser," "mypassword," and
    "mydatabase" with your MySQL username, password, and database name.

Workflow:
1. Establish a connection to the specified MySQL database using the provided
   username, password, and database name.
2. Create a cursor object to interact with the database.
3. Execute an SQL query with a JOIN operation between the "cities" and "states"
   tables based on the 'state_id' foreign key.
4. Fetch all rows returned by the query.
5. Print each row to the console.
6. Close the database cursor.
7. Close the database connection.

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

    # Execute an SQL query with a JOIN operation between the "cities" and
    # "states" tables based on the 'state_id' foreign key. Order the result by
    # the 'cities.id' column in ascending order.
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Print each row to the console
    for row in rows:
        print(row)

    # Close the database cursor
    cur.close()

    # Close the database connection
    db.close()
