
import requests # https://requests.readthedocs.io/en/master/user/quickstart/
from bs4 import BeautifulSoup
import re
import pandas as pd
from threading import Thread, RLock
lock = RLock()
urls = ['https://wiki.python.org/moin/']
class urlScrape(Thread):
    def __init__(self, link_url):
        Thread.__init__(self)
        self.link_url = link_url
    def run(self):
        links =[]
        el_a =[]
        el_a_href =[]
        r = requests.get(self.link_url)
        #print(self.link_url, r.status_code)
        soup = BeautifulSoup(r.content, 'lxml')
        soup
        for elem in soup.find_all("a"):
            print(elem)
            el_a.append(elem)

            if elem.get('href') is not None:
                el_a_href.append(elem)

        print(len(el_a),len(el_a_href))
            #if elem is not None:
                #if re.match("(.)?", elem.get('href')) is not None: # this finds all a tags that have a link to other sites(url) or other parts of current site
                #if re.match("http(.)?", elem.get('href')) is not None and elem.get('href') is not None:# I choose to only get the urls and not links to other parts of the websites
                   # links.append(elem.get('href'))
        #with lock: # !!!!"with lock" is nodig anders groeiende lists die door elkaar worden afgeprint
            #print("links scrapped from ",self.link_url)
            #print(links) # list with all links

thread_1 = urlScrape(urls[0])


thread_1.start()
