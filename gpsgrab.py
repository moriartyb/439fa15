import sys
import ast
import csv
import json
import sqlite3

print "Waiting for GPS data ..."
conn = sqlite3.connect('439.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS gps (lat real, long real, timestamp real)''')

while(1):
    line=sys.stdin.readline()
    if not line:
        exit()

    data = json.loads(line)
    print data
    if data.get('lat',None):
        with open('latlong.csv') as f:
            wr = csv.writer(f)
            wr.writerow([data['lat'], data['long'], data['time']])
            c.execute("INSERT INTO gps VALUES ('{0}', '{1}', '{2}')".format(data['lat'],data['long'], data['time']))
conn.commit()
conn.close()
