#!/usr/bin/python3
""" Module 0-select_states """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name \
                LIKE BINARY 'N%' ORDER BY states.id ASC;")
    for i in cur.fetchall():
        print(i)
    cur.close()
    db.close()
