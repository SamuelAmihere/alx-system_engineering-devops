#!/usr/bin/python3
"""Script to perform sql query."""

import sys
import MySQLdb

if __name__ == "__main__":

    sqlStatement = "SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`"

    args = sys.argv
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    exe = db.cursor()
    exe.execute(sqlStatement)

    for c in exe.fetchall():
        print(c)
    exe.close()
