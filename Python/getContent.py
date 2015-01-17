#!/usr/bin/env python
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tweepy
from connect_database import getDatabase

def connect_links():
    db = getDatabase()
    links = db.section_links.find()
    return links
    

def save_content(title,section,tags,url):
    db = getDatabase()
    db.link_content.insert({"title":title,"section":section,"tags":tags,"url":url})
       

def getDetail(links):
    driver = webdriver.Firefox()
    i=0
    num=0
    print "Begin scaning files, good luck!"  
    display = Display(visible=0, size=(800, 600))
    for link in links:
        i=i+1
        driver.get(link["link"])
        #driver.get("http://www.huffingtonpost.com/simon-mccormack/if-the-nypd-is-on-strike-maybe-they-should-stay-that-way_b_6404916.html?utm_hp_ref=crime")
        try:
            section = driver.find_element_by_class_name('title').text
            title = driver.find_element_by_tag_name('h1').text
            tags = driver.find_element_by_xpath("//div[@class='follow bottom-tags']/span").text
            save_content(title,section,tags,link["link"])
        except:
            print i
            continue 
        num=num+1
        print num,"saved into db.",(links.count()-i),"links left waiting for scan."

    driver.quit()
    display.stop()



links = connect_links()
getDetail(links) 


