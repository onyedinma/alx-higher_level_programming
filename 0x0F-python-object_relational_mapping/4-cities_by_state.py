#!/usr/bin/python3
""" A module to list all cities from a database """
if __name__ == "__main__":
    import MySQLdb
    import sys
    # connect to the database using the arguments
    database = MySQLdb.connect(host="localhost",
                               port=3306, user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3],
                               charset="utf8")
    # create a cursor object to execute queries
    cursor = database.cursor()
    # execute the query using a join between cities and states tables
    cursor.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """)
    # fetch all the rows from the query result
    cities = cursor.fetchall()
    # print each row with the city and state names
    for city in cities:
        print(city)
    # close the cursor and the database
    cursor.close()
    database.close()
