#!/usr/bin/python3
"""Update state name using SQLAlchemy."""
import sys
from model_state import Base, State  # Import model classes
from sqlalchemy import create_engine  # Import create_engine
from sqlalchemy.orm import sessionmaker  # Import sessionmaker

if __name__ == "__main__":
    # Create an SQLAlchemy engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session factory for interacting with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with ID 2
    result = session.query(State).filter_by(id=2).first()

    if result:
        # Update the name of the State object
        result.name = "New Mexico"

        # Commit the changes to the database
        session.commit()
        print("State name updated successfully.")
    else:
        print("State with ID 2 not found.")
