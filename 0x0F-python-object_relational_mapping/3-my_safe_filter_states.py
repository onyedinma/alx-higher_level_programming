#!/usr/bin/python3
""" A module to filter states by name using a safe query """
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
    # execute the query using a placeholder for the name argument
    cursor.execute("SELECT * FROM states WHERE name=%s \
            ORDER BY id ASC", (sys.argv[4],))
    # fetch all the rows from the query result
    states = cursor.fetchall()
    # print each row that matches the name argument
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    # close the cursor and the database
    cursor.close()
    database.close()
