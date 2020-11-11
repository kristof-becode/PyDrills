"""
Exercise 2 - ap all the web pages in the urls list and display the links. 1 thread per link.
urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',  => this site errors, any other I put in place works so..who knows why
]
"""
import requests # https://requests.readthedocs.io/en/master/user/quickstart/
from bs4 import BeautifulSoup
import re
import pandas as pd
from threading import Thread, RLock
lock = RLock()
urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]
class urlScrape(Thread):
    def __init__(self, link_url):
        Thread.__init__(self)
        self.link_url = link_url
    def run(self):
        links =[]
        r = requests.get(self.link_url)
        #print(self.link_url, r.status_code)
        soup = BeautifulSoup(r.content, 'lxml')
        soup
        for elem in soup.find_all("a"):
            # important to check if elem.get('href') is not None is(besides the re.match), otherwise errors, one website didn't work without this
            #if elem.get('href') is not None and if re.match("(.)?", elem.get('href')) is not None: # this finds all a tags that have a link to other sites(url) or other parts of current site
             if elem.get('href') is not None and re.match("http(.)?", elem.get('href')) is not None:# I choose to only get the urls
                links.append(elem.get('href'))
        with lock: # !!!!"with lock" is nodig anders groeiende lists die door elkaar worden afgeprint
            print("links scrapped from ",self.link_url)
            print(links) # list with all links

thread_1 = urlScrape(urls[0])
thread_2 = urlScrape(urls[1])
thread_3 = urlScrape(urls[2])
thread_4 = urlScrape(urls[3])
thread_5 = urlScrape(urls[4])
thread_6 = urlScrape(urls[5])
thread_7 = urlScrape(urls[6])
thread_8 = urlScrape(urls[7])

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()
thread_6.start()
thread_7.start()
thread_8.start()
