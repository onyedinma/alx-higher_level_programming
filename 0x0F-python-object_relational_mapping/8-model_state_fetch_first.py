#!/usr/bin/python3
"""Prints the first State object from the database\
        hbtn_0e_6_usa via  sqlalchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_first_state(engine):
    """Prints the first state in the states table"""
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).first()
    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")


if __name__ == "__main__":
    # Usage: python3 script.py <db_username> <db_password> <db_name>
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    print_first_state(engine)
