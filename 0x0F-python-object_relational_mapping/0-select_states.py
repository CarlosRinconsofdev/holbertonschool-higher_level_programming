#!/usr/bin/python3
"""Write a script that lists all
states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        rows = cursor.fetchall()

    except MySQLdb.Error as e:
        print("MYSQL Error: %s", str(e))

    for row in rows:
        print(row)
    cursor.close()
    db.close()
