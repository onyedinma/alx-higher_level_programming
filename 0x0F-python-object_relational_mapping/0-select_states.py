#!/usr/bin/python3

import MySQLdb
import sys

def listStates(username, password, database):
    # Connecting to MySQL server
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # creating SQL query to  retrieve all states

    query = "SELECT * FROM states ORDER BY id ASC"

    # Executing the SQL query to retrieve all states
    cursor.execute(query)

    # Fetching all the rows returned by the query
    results = cursor.fetchall()

    # Printing the results
    for row in results:
        print(row)

    # Closing the cursor and database connection
    cursor.close()
    connection.close()

# Check if the script is being run directly
if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states
    listStates(username, password, database)
