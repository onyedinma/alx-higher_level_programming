#!/usr/bin/python3
""" A module to select states """
if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    curs = conn.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_res = cur.fetchall()
    for row in query_res:
        if row[1][0] == "N":
            print(row)
    curs.close()
    conn.close()
