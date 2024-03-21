#!/usr/bin/python3
"""
Script that display all values in the states table
that matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Defining the database parameters
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE states.name = %s ORDER BY states.id",
        (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
