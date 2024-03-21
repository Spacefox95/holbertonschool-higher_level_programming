#!/usr/bin/python3
"""
Script that list all the states from the database
hbtn_0e_0_usa starting with N
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
    cmd = "SELECT * FROM states WHERE states.name LIKE BINARY 'N%' ORDER BY states.id"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
