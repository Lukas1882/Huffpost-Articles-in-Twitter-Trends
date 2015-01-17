#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tweepy
import re
from connect_database import getDatabase

# save the links to database.
def update_to_db(browser,page):
    db = getDatabase()
   
    # get all the links in page
    links = browser.find_elements_by_xpath('//a')
    try:
        num=0
        for link in links:
            if (checkURL(link.get_attribute('href'))):
                post = {"link":link.get_attribute('href')}
                db.section_links.insert(post)
                num = num + 1
        print "LYL:",num,"links from page \"",page,"\" added into database.\n"
    except Exception,e:
          print "LYL:Pymongo inseration error:\n",str(e)

# collect link from the certain section.
def collect_section(section):
    homepage='http://www.huffingtonpost.com/'
    page = homepage + section +'/'
    browser.get(page)
    update_to_db(browser,page)

# check if this url is a link to a article (a normal article or a live show).
def checkURL(url):
    pattern1 = re.compile(r"http:\/\/live\.huffingtonpost\.com\/r\/highlight\/")
    pattern2 = re.compile(r"http:\/\/www\.huffingtonpost\.com\/\d{4}\/\d{2}\/\d{2}\/")
    match1 = pattern1.match(str(url))
    match2 = pattern2.match(str(url))
    if match1:
        return True
    if match2:
        return True
    return False

browser = webdriver.Firefox()
collect_section('politics')
collect_section('business')
collect_section('tech')
collect_section('sports')
collect_section('theworldpost')
collect_section('')
browser.quit()
