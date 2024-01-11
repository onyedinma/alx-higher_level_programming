#!/usr/bin/python3
"""Script to print states via sqlalchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_states(engine):
    """Prints the states that contain the letter 'a'"""
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State)\
        .order_by(State.id)\
        .filter(State.name.ilike('%a%'))
    for result in results:
        print("{}: {}".format(result.id, result.name))


if __name__ == "__main__":
    # Usage: python3 script.py <db_username> <db_password> <db_name>
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    print_states(engine)
