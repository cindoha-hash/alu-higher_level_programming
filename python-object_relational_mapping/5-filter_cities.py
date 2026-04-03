#!/usr/bin/python3
"""List cities by state (safe)."""
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
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([r[0] for r in rows]))
    cur.close()
    db.close()
