#!/usr/bin/python3
"""
Script for Querying States from the Database

This script connects to a MySQL database using SQLAlchemy, queries and prints
information about states from the "states" table.

Usage:
    python script_query_states.py <username> <password> <database_name>

Parameters:
    <username>: MySQL database username.
    <password>: Password for the specified user.
    <database_name>: Name of the MySQL database.

Dependencies:
    - SQLAlchemy: This script requires the SQLAlchemy library. You can install
      it using:
          pip install sqlalchemy
    - model_state.py: Contains the State model definition.

Example:
    python script_query_states.py myuser mypassword mydatabase
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Ensure the "states" table is created in the database
    Base.metadata.create_all(engine)

    # Query all states from the "states" table and print information
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the database session
    session.close()
