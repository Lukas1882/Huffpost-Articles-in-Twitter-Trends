 #HuffingtonPost Articles in Twitter Trends
 
## Synopsis and Preview
This web application is built in ***Ubuntu 14.04***. The server side is ***Apache*** with ***Common Gateway Interface*** (CGI). ***Python*** is in the back end hooked up with font end with ***AJAX***.

***Twitter API*** is used to find the trends in Twitter and ***Selenium WebDriver*** in Python is used to find the articles in *HuffingtonPost* pages. Users can find the articles related to the selected trends or key-words.

![](https://raw.githubusercontent.com/leaot/Huffpost-Articles-in-Twitter-Trends/master/IMG/web.png)

## Details

#### Twintter  API
***[Tweepy](http://docs.tweepy.org/en/v3.1.0/)*** is used to link Twitter and Python. A Twitter application is needed to get the authentication for the API. You can learn more from the Tweepy documentation and ***[Twitter REST API](https://dev.twitter.com/rest/public)***.

For security issues, Twitter limits the API call number every hour. If call exceeds the biggest number allowed each hour, the API will shut down.

#### Apache with CGI
To run Apache with, you should install Apache first then install CGI. A lot of information can be found on internet about how to configure CGI with Apache. I am sure this [link](https://bdhacker.wordpress.com/2011/05/21/running-your-first-cgi-program-with-apache2/) will help a lot. You should configure CGI in the configuration file in Apache folder, including the path of the projects, the script category will be used. 

**Important**: If run into a "500 internal server error",check the error log in "/var/log/apache2/error-log". If it is a permission limited, cd to the folder of the scripts( in my case they are Python scripts), then "chmod 755 yourfile.py". More advices can be found on web.


#### AJAX Call to Apache CGI
Using AJAX with Javascrip, POST and GET call are successful in this projects. To get the call in Python scripts, "*import cgitb*" , "*cgitb.enable()*" are needed. You can find more usefull information from the [official site](https://docs.python.org/2/library/cgi.html). In my file, I use two different ways to get the POST and the GET calls respectively.

For expansibility and future reiteration，each AJAX call to Python scripts has an  Python ***entry file ***, connecting the AJAX and the other normal Python scripts and functions. In the entry files, importing CGI and other codes for CGI configuration are created there. In this way, the other Python files can be used somewhere else with minimum change.

#### Selenium WebDriver
WebDriver is used to find the elements on target page. To work with Python, ***[WebDriver API](http://selenium-python.readthedocs.org/en/latest/api.html)*** are implemented. However, in order to call WebDriver in server side from client, headless browser are needed. In this project, just a normal Firefox is used, since Headless Firefox, PyVirtualDisplay and PhantomJS are failed without enough permission in server side. The details can be checked in Apache error log.


When ussing WebDriver to get the contents of target pages, hundreds or thounds pages will be scaned and the process period can go for more than hours. Thus, some issues should be taken care of.

***1. When to make a connect to MongoDB*** 

Since this project is just a demo, for debug reason, every 10 page scan a block of pages' information will go into the database. For real work, the block size can set to 50 or bigger. You can go to the function in "/Python/getContent.py//def getDetail" to change the block size. 

In this function,for every page waiting for scan, Python will connect to MongoDB to check whether the URL has been in the database table. Developers can delete this check since I have made a url duplicat check for the url link table. However, I keep it for my own historic debug issue. If there is something wrong with the URL table, Python can check the URL before usin ``````g Webdriver to load it, which can save a lot ot time when there are 1000 page URLs.

***2 Choose which browser for WebDriver***

As discuss above, Headless Firefox, PyVirtualDisplay and PhantomJS are failed without enough server side permissions. When use PyVirtualDisplay and headless for local side multi-page scan, they are not as stable as normal Firefox. If any one find the solution please feel free to contact with me.    
Anyway, a normal Firefox is better for debug. Develpers can watch the browser to check the process. 

***Tip 1***  ***: If the firefox keep loading on one page, you just need to open a new tab besides the page, then the browser will reload the page in the new tab***. (I spent hours on the loading issue, it is caused by the real time network status, make sure your roommates or colleagues don't eat up the internet data.)

***Tip 2*** ***: To speed of scan speed in Firefox***. You need your browser block loading JS and images. You can use some Firefox Add-ons to this job. In my project, I use QuickJava 2.0.6. You cannot install it with opening a normal firefox since Webdriver will open another sub-version in you machine. To install it, you should run Webdriver first, then get the Firefox window opend by Webdriver. Stop your running scripts, and install the Add-on in this Firefox window. To configure it, you should to the Add-ons manager. Then you can use your Webdriver again. To check whether it is installed in your browser is easy, you can find the logo in the left side of the navbar. At the very begining, I only can scan round 100 pages without this Add-on. After the 100 pages, the browser will shut down. :(     
However, this Add-on fix it.

![](https://raw.githubusercontent.com/leaot/Huffpost-Articles-in-Twitter-Trends/master/IMG/addon.png)![](https://raw.githubusercontent.com/leaot/Huffpost-Articles-in-Twitter-Trends/master/IMG/addon-setting.png)

***3. If something wrong in your page scan, Don't Worry!.***

It is possible your machine runs down after one hour's Webdriver scan, you don't need to run it again (I did it many times : ( ) In this project, you can run the webdriver from the link index which has not been saved yet.

![](https://raw.githubusercontent.com/leaot/Huffpost-Articles-in-Twitter-Trends/master/IMG/scan.png)

For example, if your Python or machine get something wrong when the code go to 368 - 377, in this case, you have saved the Index up to 1069, thus, you can savely configure the index variable in "getContent.py" to 1070. Thus, when you run the scrip again, the webdriver will scan from Index 1070. In this example, I set block as 10, page information saved every 10 page scans.

#### MongoDB
Most of information is saved into database. The newest top 10 trends, the link URLs in HuffPost sections, in details of articles are all saved in defferent tables.

***1.Filter Rules to pick the URLs in pages to SAVE TIME***

For the articles in Huffpost, they have a format for normal ones as "http://www.huffingtonpost.com/****/**/**/", or "http://live.huffingtonpost.com/r/highlight/*********" for video articles. A another rule  "http://insidemovies.ew.com/****/**/**" also added here. Developer can add more rules to scan more page in different sections. However, after adding the new rules, scan rules for collecting page details also need to configure in "getContent.py". Developer should go into the page source code to figure out which elements are needed.
 
*** 2.Get Avoid of Duplicated Links.***
Webdriver always get duplicated links in a single page. What is worse, "www.good.com/dddd" and "www.good.com/dddd?********" may lead to the same page. Thus, for every URL saved into database, we need to check whether it has been saved before. When go to article detail savement, we check the whether the title has been saved before. In this project, only new links will be saved in to link table, and only new title can be saved into article detail table. Before using Webdriver to scen, we can use database to check the whether the URL has been saved. Compared with connecting to databse, loading a page from internet is longer and more "risky" ( multi-page scan is not so stable as a single page).

![](https://raw.githubusercontent.com/leaot/Huffpost-Articles-in-Twitter-Trends/master/IMG/getlink.png)

From this picture, only a few link URLs saved into database, because it is a update operation, only the new links saved.

## Run It
To run this project is very simple. Go to the folder "Python", run the file "getlink.py". You can configure the subpages or change to other URL in this file. After get the URLs, run the file "getContent.py" to scan the pages by WebDriver. You can find more information in the above disscuss.

During these process, only new links and articles updated into database, the previous records will be kept still. Then you can go to the web page to begin your article search. The more records in database, the more results, enjoy it.

***Result1:***
![](https://raw.githubusercontent.com/leaot/Huffpost-Articles-in-Twitter-Trends/master/IMG/result2.png)

***Result2:***
![](https://raw.githubusercontent.com/leaot/Huffpost-Articles-in-Twitter-Trends/master/IMG/result1.png)

## The MIT License (MIT)

