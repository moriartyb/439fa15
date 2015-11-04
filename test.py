import subprocess
import os
import httplib
import urllib
cmd="cat /proc/net/wireless | tail -n 1 | awk '{print $4}'"
def post(val):
        conn = httplib.HTTPConnection("bladeismyna.me", 5000)
        params = urllib.urlencode({'point': val})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn.request("POST", "/graph", params, headers)
        response = conn.getresponse()
        print response.status, response.reason

while True:
	os.system("cat /proc/net/wireless | tail -n 1 | awk '{print $4}' > data.txt")
	a = open("data.txt", "r")
	post(a.readline().strip('. \t \n \r'))
	a.seek(0)


