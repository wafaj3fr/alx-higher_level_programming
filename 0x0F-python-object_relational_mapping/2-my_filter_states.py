#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    curs.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(argv[4]))
    [print(state) for state in curs.fetchall()]
