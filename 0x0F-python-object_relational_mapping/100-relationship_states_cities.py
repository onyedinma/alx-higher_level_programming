#!/usr/bin/python3
"""A script to print all the states and cities """
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def print_states_and_cities():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for state in states:
        print(f"{state.name}:")
        for city in state.cities:
            print(f"\t{city.name}")
    session.close()


if __name__ == "__main__":
    print_states_and_cities()
