from bs4 import BeautifulSoup

def main():
    file = open("/home/becode/data/AI4Belgium.html", "r")
    html_doc = file.read()
    file.close()
    print(html_doc)

    soup = BeautifulSoup(html_doc, "lxml")
    # In my file (becode.org) by looking at this html script We can see that the main title is arranged in the h1 tag
    # The h1 tag should contain your targeted keywords, ones that closely relate to the page title and are relevant to your content.
    # The h2 tag is a subheading and should contain similar keywords to your h1 tag.
    # Your h3 is then a subheading for your h2 and so on to h6

    for p in soup.find_all('h1'):
        # We only retrieve the content ==> .text
        print("h1 ", p.text)

    for p in soup.find_all('h2'):
        # We only retrieve the content ==> .text
        print("h2 ", p.text)

    for p in soup.find_all('h4'):
        # We only retrieve the content ==> .text
        print("h4 ", p.text)

    for p in soup.find_all('p'): # ptags a paragraph
        # We only retrieve the content ==> .text
        print("p tag ", p.text)

main()