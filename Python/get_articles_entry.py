#!/usr/bin/env python
import sys
import json
import cgi
from article_engin import get_articles
fs = cgi.FieldStorage()
sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")
result = {}
result['success'] = True

data = ''
for k in fs.keys():
    data+=fs.getvalue(k)

#get_articles(eval(data))
result['message'] =  get_articles(eval(data))
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")
sys.stdout.close()




