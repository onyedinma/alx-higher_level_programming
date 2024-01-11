#!/usr/bin/python3
""" A module to list all cities of a state from a database

Usage: python3 2-my_filter_states.py <username> <password> <database> <state>
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    # connect to the database using the arguments
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         charset="utf8")
    # create a cursor object to execute queries
    cursor = db.cursor()
    # execute the query using a join between cities and states tables
    cursor.execute("""
        SELECT City FROM (
        SELECT cities.id AS ID, cities.name AS City,
        states.name AS State FROM cities
        JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC) as Table1
        WHERE State='{}';
        """.format(sys.argv[4]))
    # fetch all the rows from the query result
    cities = cursor.fetchall()
    # print the city names separated by commas
    print(", ".join(city[0] for city in cities))
    # close the cursor and the database
    cursor.close()
    db.close()
