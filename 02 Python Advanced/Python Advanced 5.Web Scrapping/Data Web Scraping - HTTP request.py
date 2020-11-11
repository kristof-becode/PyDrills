import requests
from bs4 import BeautifulSoup

def main():

    # Url of website
    url = 'https://www.ai4belgium.be/nl/'
    # I send my HTTP request with a "GET" to the site server to identify in the url
    r = requests.get(url)
    # I display the requested url and the return of the server
    print(url, r.status_code)
    # I ask beautifulSoup to keep in a soup variable the web page to scrape (url) an html script
    soup = BeautifulSoup(r.content, 'lxml')

    # soup
    for p in soup.find_all('h1'):
        # We only retrieve the content ==> .text
        print("h1 ", p.text)

    for p in soup.find_all('h2'):
        # We only retrieve the content ==> .text
        print("h2 ", p.text)

    for p in soup.find_all('h3'):
        # We only retrieve the content ==> .text
        print("h3 ", p.text)

    for p in soup.find_all('h4'):
        # We only retrieve the content ==> .text
        print("h4 ", p.text)

    for p in soup.find_all('p'):  # p tags a paragraph
        # We only retrieve the content ==> .text
        print("p tag ", p.text)

main()