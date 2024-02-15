#!/usr/bin/python3
"""Script to perform sql query."""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    exe = db.cursor()
    exe.execute("SELECT * FROM `states` ORDER BY `id`")

    for state in exe.fetchall():
        if "N" == state[1][0]:
            print(state)

    exe.close()
