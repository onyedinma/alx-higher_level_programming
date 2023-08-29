#!/usr/bin/python3
"""Print states and cities using SQLAlchemy."""
from relationship_state import Base, State  # Import model classes
from relationship_city import City  # Import City class
from sqlalchemy import create_engine  # Import create_engine
from sqlalchemy.orm import sessionmaker  # Import sessionmaker
from sys import argv  # Import argv from sys module

if __name__ == "__main__":
    # Create an SQLAlchemy engine to connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))  # Extract credentials from argv

    Base.metadata.create_all(engine)  # Create tables if they don't exist

    # Create a session factory for interacting with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for cities and their corresponding states
    result = session.query(City, State).filter(City.state_id == State.id).all()

    for row in result:
        # Print city information along with the corresponding state
        print("{}: ({}) {}".format(row[1].name, row[0].id, row[0].name))
