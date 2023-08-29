#!/usr/bin/python3

""" This code updates the name of the state/
with id 2 to "New Mexico" in a MySQL database."""

import sys
from sqlalchemy import create_engine, select

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]),
    pool_pre_ping=True)

# Get the first state with id 2
query = select(State).where(State.id == 2)

results = engine.execute(query)

# Update the state name to "New Mexico"
results.update({'name': 'New Mexico'})

# Commit the changes to the database
engine.commit()
