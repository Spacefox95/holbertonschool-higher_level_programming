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
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    cursor = db.cursor()
    cmd = "SELECT * FROM states WHERE name LIKE \
        BINARY '{}' ORDER BY states.id".format(sys.argv[4])
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
