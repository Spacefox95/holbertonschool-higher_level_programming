#!/usr/bin/python3
"""
Script that display all cities in the state
passed as an argument
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
    cmd = "SELECT cities.id, cities.name FROM cities \
           JOIN states ON cities.state_id = states.id \
           WHERE states.name = %s \
           ORDER BY states.id ASC"
    cursor.execute(cmd, (sys.argv[4],))
    rows = cursor.fetchall()
    american_state = [row[1] for row in rows]
    output = ", ".join(american_state)
    print(output)
    db.close()
