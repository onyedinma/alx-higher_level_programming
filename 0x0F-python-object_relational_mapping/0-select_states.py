#!/usr/bin/python3
""" Module to select states """
if __name__ == "__main__":
    import MySQLdb
    import sys
    conne = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    curs = conne.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    query_row_results = curs.fetchall()
    for row in query_row_results:
        print(row)
    curs.close()
    conne.close()
