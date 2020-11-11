import requests # https://requests.readthedocs.io/en/master/user/quickstart/
from bs4 import BeautifulSoup
import re
import pandas as pd

def main():
    url = 'http://www.allocine.fr/'
    r = requests.get(url)
    print(url, r.status_code)
    soup = BeautifulSoup(r.content, 'lxml')
    soup

    #for p in soup.find_all('a'): # an 'a' tag refers to hyperlinks, but here we print the respective 'p' tag text
        #print(p.text)
    #for elem in soup.find_all('a'): # here we really print all the 'a' elements or hyperlinks !!!
        #print(elem)

     # select only hyperlinks to films, not series or other links, so look for this 'form' : href="/film/fichefilm-267615/vod-dvd/">#Jesuislà Blu-Ray</a>
    links =[]
    links_movies = []
    for elem in soup.find_all('a'):
        if re.match("(.)?film/fichefilm_gen(.)?", elem.get('href')) is not None:
            #print(elem)
            links.append(elem.get('href'))
    links_movies = ['http://www.allocine.fr' + elem for elem in links if 'film' in elem] # add rest of url in list to get url list
    print(links_movies)
    # now for every movie collect title and synopsis on the url page
    titles_movies=[]
    synopsis_movies = []
    for items in links_movies: #iterate through url's and make soup for every url to get title and synopsis on page
        url = items
        r = requests.get(url)
        #print(url, r.status_code)
        soup = BeautifulSoup(r.content, 'lxml')
        soup
        for elem in soup.find_all('div', attrs={"class": "titlebar-title titlebar-title-lg"}): # title
            #print(elem.text)
            titles_movies.append(elem.text)
        for elem in soup.find_all('div', attrs={"class": "content-txt"}): # synopsis, but I also get reviews so need extra code regex
            #print(elem.get("class")) this shows 2 item in list, 2nd one only when it refers to review so for synopsis take those elem out
            if (re.match("content-txt", (elem.get("class"))[0]) is not None) and (len(elem.get("class")) == 1) : #only the synopsis elements
                synopsis_movies.append(elem.text)
    #print(len(synopsis_movies), len(titles_movies), len(links_movies)) see all same lenght, same number of items in list

    # create dataframe with pandas and export as .csv !!!
    df = pd.DataFrame({'Title': titles_movies}) # 3 columns
    df['synopsis'] = synopsis_movies
    df['links'] = links_movies
    df.to_csv("/home/becode/data/allo_cine.csv", index=False)
    print(df)

main()