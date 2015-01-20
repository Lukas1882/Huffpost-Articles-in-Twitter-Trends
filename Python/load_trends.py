# Connect to the database and return the list of trends.


import tweepy
import pymongo
import json
from pymongo import MongoClient


def load_trends_db():
    # database connection
    try:
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.lyl
        client.close()
        return db.trends.find()[0]

    except Exception, e:
        print "LYL:Pymongo connection error:\n", str(e)

dic_data = load_trends_db()
json_data = json.dumps(dic_data.get("trends"))
print json_data
