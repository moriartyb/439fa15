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
	os.system("iwlist wlp1s0 scan | sed -ne \'s#^[[:space:]]*\\(Quality=\\|Encryption key:\\|ESSID:\\)#\\1#p\' -e \'s#^[[:space:]]*\\(Mode:.*\\)$#\\1\\n#p\' | grep -B 2 hoc | grep -vE \'hoc|Encryption\' > data.txt")
	a = open("data.txt", "r")
        while a.readline() == '':
                a.seek(0)
        a.seek(0)
        print a.readline()
	# post(a.readline().strip('. \t \n \r'))
	


