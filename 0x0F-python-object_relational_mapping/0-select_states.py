#!/usr/bin/python3
""" Module to select from a database"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    con = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = connect.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_results = cursor.fetchall()
    for row in query_results:
        print(row)
    cur.close()
    con.close()
