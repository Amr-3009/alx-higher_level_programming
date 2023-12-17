#!/usr/bin/python3
"""
Query State ID by Name from the Database

This script connects to a MySQL database using SQLAlchemy and queries the ID o
a state from the "states" table based on the provided state name.

Usage:
    python script_query_state_id.py
    <username> <password> <database_name> <state_name>

Parameters:
    <username>: MySQL database username.
    <password>: Password for the specified user.
    <database_name>: Name of the MySQL database.
    <state_name>: Name of the state to query.

Dependencies:
    - SQLAlchemy: This script requires the SQLAlchemy library. You can install
      it using:
          pip install sqlalchemy
    - model_state.py: Contains the State model definition.

Example:
    python script_query_state_id.py myuser mypassword mydatabase California
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Ensure the "states" table is created in the database
    Base.metadata.create_all(engine)

    # Query the ID of the state based on the provided state name
    state = session.query(State).filter(State.name == argv[4]).first()

    # Print the state ID or a message if the state is not found
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the database session
    session.close()
