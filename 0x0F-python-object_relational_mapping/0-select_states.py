#!/usr/bin/python3
'''Lists all states from the databse hbtn_0e_0_usa'''

import MySQLdb
from sys import argv

if __name__ = "__main__":
    db = MySQL.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        port=3306,
        db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC;')
    for row in cur.fecthall():
        print(row)
    db.close()
