#!/usr/bin/python3
# 1-filter_states.py: a script that lists all
# states with a name starting with N
# (upper N) from the database hbtn_0e_0_usa

import MySQLdb
import sys

# get the arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# connect to the database
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database,
)

# create a cursor object
cur = db.cursor()

# execute the query
cur.execute(
    """
    SELECT *
    FROM states
    WHERE name LIKE 'N%'
    ORDER BY id ASC
    """
)

# fetch all the rows
rows = cur.fetchall()

# print each row
for row in rows:
    print(row)

# close the cursor and the database
cur.close()
db.close()
