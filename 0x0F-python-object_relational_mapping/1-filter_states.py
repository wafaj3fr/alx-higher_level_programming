#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)
    cursor.close()
    db.close()
