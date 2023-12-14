#!/usr/bin/python3
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)

    states = session.query(State).order_by(State.id).first()
    if states:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
