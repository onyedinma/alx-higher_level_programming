#!/usr/bin/python3
"""Script to print states via sqlalchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_state(engine, state_name):
    """Adds a state with the given name to the states table"""
    Session = sessionmaker(bind=engine)
    session = Session()
    louis = State(name=state_name)
    session.add(louis)
    session.commit()
    result = session.query(State)\
        .filter_by(name=state_name).first()
    if result:
        print(result.id)
    else:
        print("Not found")


if __name__ == "__main__":
    """ Usage: python3 script.py
    <db_username> <db_password> <db_name> <state_name> """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    state_name = sys.argv[4]
    add_state(engine, state_name)
