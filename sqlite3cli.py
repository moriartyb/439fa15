#!/usr/bin/python2
import sqlite3
import sys
db = sqlite3.connect(sys.argv[1])
while True:
    cmd = raw_input("sql> ")
    cur = db.cursor()
    try:
        db.execute(cmd.strip())
        if cmd.lstrip().upper().startswith("SELECT"):
            print cur.fetchall()
    except sqlite3.Error, e:
       print "An error occurred:", e.args[0]
