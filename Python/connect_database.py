import pymongo
from pymongo import MongoClient


def getDatabase():
    try:
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.lyl
        return db
    
    except Exception,e:
        print "LYL:Pymongo connection error:\n",str(e)
        sys.exit(0)

    
