#!/usr/bin/python3
"""Lists states matching user input exactly."""

import MySQLdb
import sys


if _name_ == "_main_":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(sys.argv[4])
    cur.execute(query)
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
