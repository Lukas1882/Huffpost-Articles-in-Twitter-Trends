import tweepy
import pymongo
import json
from pymongo import MongoClient


def get_trends_place(place_id):
    auth = tweepy.OAuthHandler("QOgmguBKBSRMKIvsKSnQHKtRh", "Q1b2qx1jmqmyz1W1MQybKxVFjT2Xki4I09nIaopWRttNcUzagb")
    auth.set_access_token("830970282-3m0aLd06DIC9Yp5M3koaSbDyNFAeiAqLhqRZi7Qs", "MAKSvwoIqfnO9KIxdBVJQUdKwJYRrZWaT3aEafXpQzjoj")
    api = tweepy.API(auth)
    return api.trends_place(place_id)


trends = get_trends_place(2459115)   
#print trends


dd =json.dumps(trends)
bb= str(dd)
print bb


import cgitb
cgitb.enable()

print "Content-Type: text/plain;charset=utf-8"
print

print "Hello World!"
