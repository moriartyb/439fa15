import sys
import ast
import csv
import json

print "Waiting for GPS data ..."
while(1):
#    print "getting new line"
    line=sys.stdin.readline()
    if not line:
        exit()
#    print "got new line"

    line=line.strip()
    line=line.split("\t")
    if line[0] == "Station":
        current_mac = line[1]
    if line[0] == "signal":
        current_signal = line[1]

    with open('latlong.csv') as f:
        wr = csv.writer(f)
        wr.writerow(current_mac,current_signal)
