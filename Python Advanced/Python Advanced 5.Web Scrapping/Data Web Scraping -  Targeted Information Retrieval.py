import requests # https://requests.readthedocs.io/en/master/user/quickstart/
from bs4 import BeautifulSoup
def main():
    url = 'http://www.allocine.fr/'
    r = requests.get(url)
    print(url, r.status_code)
    soup = BeautifulSoup(r.content, 'lxml')
    soup
    for p in soup.find_all('a'): # an 'a' tag refers to hyperlinks
        print(p.text)
    for elem in soup.find_all('a', attrs={"class": "meta-title meta-title-link"}):
        print(elem)
    # print href's
    for elem in soup.find_all('a', attrs={"class": "meta-title meta-title-link"}):
        print(elem.get('href'))
        # return a list
    # print titles
    for elem in soup.find_all('a', attrs={"class": "meta-title meta-title-link"}):
        print(elem.get('title'))


main()