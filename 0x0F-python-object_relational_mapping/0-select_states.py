#!/usr/bin/python3
""" Module to select states """
if __name__ == "__main__":
    import MySQLdb
    import sys
    lin = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = lin.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_row_results = cur.fetchall()
    for row in query_row_results:
        print(row)
    cur.close()
    lin.close()
