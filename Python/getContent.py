# This file is the core file to collect article information by Webdriver. 
# You can find more information on my Git README.
# You must run this file to collect article into database.
# "index" means the begining index in link table, from the index, you can use webdriver to scan the pages.
# "block" means after how many page scan, connect to the database to save the article information.


from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from connect_database import getDatabase


# retur 
def connect_links():
    client = getDatabase()
    db = client.lyl
    links = db.section_links.find()
    client.close()
    link_list = []
    for link in links:
        link_list += [link["link"]]
    client.close()
    return link_list


def save_content(titles, sections, tags, urls):
    if len(titles) == 0:
        print "no content, continue"
        return True
    print "Saving begins."
    # the index of the begining
    i = 0
    client = getDatabase()
    try:
        db = client.lyl
        while i < len(titles):
            if db.link_content.find_one({"title": titles[i]}):
                i = i + 1
                print "one article already in database"
                continue
            db.link_content.insert(
                {"title": titles[i], "section": sections[i], "tags": tags[i], "url": urls[i]})
            i = i + 1
    except:
        print "get one error when saving page information"
    client.close()
    print "Saving ends."
    return True


def getDetail(link_list, begin_index):
    i = begin_index
    num = 0
    # after get how many links, then save them into database
    block = 10
    print "Begin scaning files, good luck!"
    #display = Display(visible=0, size=(800, 600))
    # display.start()
    driver = webdriver.Firefox()
    sections = []
    titles = []
    tags = []
    links = []

    while i < len(link_list):
        if i % block == 0:
            save_content(titles, sections, tags, links)
            sections = []
            titles = []
            tags = []
            links = []

        # check if this link saved already
        client = getDatabase()
        db = client.lyl
        if db.link_content.find_one({"url": link_list[i]}):
            print "saved this article already. Jump."
            i = i + 1
            client.close()
            continue
        else:
            client.close()

        try:
            driver.set_page_load_timeout(20)
            driver.get(link_list[i])
        except:
            print "Loading timeout at", link_list[i]
            i = i + 1
            continue
        try:
            pattern3 = re.compile(
                r"http:\/\/insidemovies\.ew\.com\/\d{4}\/\d{2}\/\d{2}\/")
            match3 = pattern3.match(str(link_list[i]))
            # for different pattern, check info bt different rules.
            if match3:
                section = "Entertainment Weekly"
                title = driver.find_element_by_tag_name('h1').text
                tag = driver.find_element_by_xpath(
                    "//div[@class='meta-bottom']//div").text
            else:
                section = driver.find_element_by_class_name('title').text
                title = driver.find_element_by_tag_name('h1').text
                tag = driver.find_element_by_xpath(
                    "//div[@class='follow bottom-tags']/span").text
            sections += [section]
            titles += [title]
            tags += [tag]
            links += [link_list[i]]
        except Exception, e:
            print "Page not available:", str(e)
            i = i + 1
            continue
        num = num + 1
        print num, "pages find.", (len(link_list) - i), "links left waiting for scan. Index:", i
        i = i + 1

    save_content(titles, sections, tags, links)
    driver.quit()
    # display.stop()


# begin with the link index
index = 850
links = connect_links()
getDetail(links, index)
