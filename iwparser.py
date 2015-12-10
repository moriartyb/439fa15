#!/usr/bin/python2
import sys
import csv
import sqlite3
import os
RSSI_CSV_FILE=os.environ.get('RSSI_CSV_FILE', 'rssi.csv')

conn = sqlite3.connect('rssi.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS rssi (mac text, rssi real, timestamp real)''')

current_mac = None
current_signal = None
from time import time
count = 0
data = []
t = time()
while(1):
    line=sys.stdin.readline()
    if not line:
        break
    data.append(line)
for line in data:
    line=line.strip()
    line=line.split("\t")
    line = map(lambda s: s.strip(': '), line)
        # print line[0].split(" ")

    space_split = line[0].split(" ")
    if space_split[0] == "Station":
        current_mac = space_split[1]
    if line[0] == "signal":
        current_signal = line[1]

    if current_mac and current_signal:
        with open(RSSI_CSV_FILE, 'a') as f:
            wr = csv.writer(f)
            wr.writerow([current_mac,int(current_signal.split(' ')[0]), t])
            c.execute("INSERT INTO rssi VALUES ('{0}', '{1}', '{2}')".format(current_mac,int(current_signal.split(' ')[0]), t))
        current_mac = None
        current_signal = None
conn.commit()
conn.close()
