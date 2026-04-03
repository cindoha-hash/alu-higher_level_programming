#!/usr/bin/python3
"""Filter states starting with N."""
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
