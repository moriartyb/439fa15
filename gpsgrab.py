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
    line=line.split(" ")
    print line
    data = json.loads(line[0])
    print data
    if data.get('lat',None):
        with open('latlong.csv') as f:
            wr = csv.writer(f)
            wr.writerow([data['time'],data['lat'],data['long']])
