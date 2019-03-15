'''
Using requests_html scrape information from a wikipedia page that interests you.
( you can use: https://en.wikipedia.org/wiki/Ubud )

Collect:
* all the information recorded in the infobox on the right
* 2 links to images on the site
* an interesting fact or quote from the page
* a collection of all the resources (titles and links) related to the page

Store the information in a nicely formatted text file.

'''

from requests_html import HTMLSession
import random

url = "https://en.wikipedia.org/wiki/Paris"

session = HTMLSession()
r = session.get('https://en.wikipedia.org/wiki/Paris')

about = r.html.find("div.table", first=True)

print(about)
#about = r.html.xpath("//*[@id='mw-content-text']/div/table[1]")[0]

#print(about.text)

#img1 = r.html.xpath("//*[@id='mw-content-text']/div/div[15]/div/a/img")[0]



