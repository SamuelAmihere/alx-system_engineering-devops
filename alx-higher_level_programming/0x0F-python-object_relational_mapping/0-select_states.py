#!/usr/bin/python3
"""Script to perform sql query."""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    exe = db.cursor()
    exe.execute("SELECT * FROM `states`")

    for state in exe.fetchall():
        print(state)

    exe.close()
