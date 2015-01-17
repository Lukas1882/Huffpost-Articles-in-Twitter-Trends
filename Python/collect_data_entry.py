#!/usr/bin/env python

import sys
import json
import cgi

fs = cgi.FieldStorage()
sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")
result = {}
result['success'] = True

data = {}
for k in fs.keys():
    data[k] = fs.getvalue(k)

result['message'] = "Server: Have get the data:"+data["data"]+'. However, after trying webdriver with Friefox, headless Firefox, xvfbwrapper and PhantomJS, the webdriver cannot run with the necessary permissions. It should be caused by system setting issues. You can collect the link or scan the url manually runing Python scripts. You can find more information from READ_ME.'
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")
sys.stdout.close()
