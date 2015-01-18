
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import pymongo
from pymongo import MongoClient
 

def save_link_to_db(browser,page):
    # database connection
    try:
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.lyl
    except Exception,e:
        print "LYL:Pymongo connection error:\n",str(e)


     
    # get all the links in page
    links = browser.find_elements_by_xpath('//a')
    try:
        
        for link in links:
            post = {"link":link.get_attribute('href'),"date": datetime.datetime.utcnow()}
            db.links.insert(post)
        print "LYL:",len(links),"links from page\"",page,"\" added into database.\n"
    except Exception,e:
          print "LYL:Pymongo inseration error:\n",str(e)


browser = webdriver.Firefox()
page= "http://www.google.com/"
browser.get(page)
save_link_to_db(browser,page)

browser.quit()
