#!/usr/bin/python3
"""
Script that lists all states
with name starting with 'N' from database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Filter and print states starting with 'N' from the database.
    Arguments:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' "
                "ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        filter_states(username, password, database)
    else:
        print("Usage: ./1-filter_states.py <mysql username> "
              "<mysql password> <database name>")
