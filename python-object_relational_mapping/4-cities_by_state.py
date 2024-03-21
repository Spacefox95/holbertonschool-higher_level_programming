#!/usr/bin/python3
"""
Script that lists all the cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Defining the database parameters
    """
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    cursor = db.cursor()
    cmd = "SELECT cities.id, cities.name, states.name FROM cities \
           JOIN states ON cities.state_id = states.id \
           ORDER BY cities.id"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
