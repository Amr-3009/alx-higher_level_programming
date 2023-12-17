#!/usr/bin/python3
"""
MySQL Database Query Script

This script connects to a MySQL database, executes a SELECT query with a JOIN
operation and a WHERE clause, and retrieves cities in a specific state. The
results are printed to the console.

Usage:
    python script.py <username> <password> <database_name> <state_name>

Parameters:
    <username>: MySQL database username.
    <password>: Password for the specified user.
    <database_name>: Name of the MySQL database.
    <state_name>: The name of the state to filter cities.

Dependencies:
    - MySQLdb module (MySQL-python): This script requires the MySQLdb module t
      be installed. You can install it using:
        pip install MySQL-python

Example:
    python script.py myuser mypassword mydatabase 'California'

Note:
    Before running the script, make sure to replace "myuser," "mypassword," an
    "mydatabase" with your MySQL username, password, and database name.

Workflow:
1. Establish a connection to the specified MySQL database using the provided
   username, password, and database name.
2. Create a cursor object to interact with the database.
3. Execute an SQL query with a JOIN operation between the "cities" and "states
   tables based on the 'state_id' foreign key, and filter results by the
   provided state name.
4. Fetch all rows returned by the query.
5. Extract city names from the results.
6. Print the city names to the console.
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

    # Execute an SQL query with a JOIN operation between the "cities" and
    # "states" tables based on the 'state_id' foreign key, and filter results
    # by the provided state name.
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s",
        [argv[4]]
    )

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Extract city names from the results
    cities_in_states = [row[1] for row in rows]

    # Print the city names to the console
    print(", ".join(cities_in_states))

    # Close the database cursor
    cur.close()

    # Close the database connection
    db.close()
