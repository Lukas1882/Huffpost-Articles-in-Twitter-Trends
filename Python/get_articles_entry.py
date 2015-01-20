#!/usr/bin/env python
# This entry file get the call from AJAX to collect the related articels.

import sys
import json
import cgi
from article_engin import get_articles
from connect_database import getDatabase
fs = cgi.FieldStorage()
sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")
result = {}
result['success'] = True

data = ''
for k in fs.keys():
    data += fs.getvalue(k)

# get_articles(eval(data))
titles = get_articles(eval(data))
article_data = []
client = getDatabase()
db = client.lyl
result["title"] = []
result["url"] = []
result["tags"] = []
result["section"] = []
for title in titles:
    article = db.link_content.find_one({"title": title})
    result["title"] += [article["title"]]
    result["url"] += [article["url"]]
    result["tags"] += [article["tags"]]
    result["section"] += [article["section"]]
client.close()
sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")
sys.stdout.close()