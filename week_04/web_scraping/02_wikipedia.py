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

text_infobox = r.html.find("#mw-content-text > div > table.infobox.geography.vcard", first = True)
#or
#text_infobox = r.html.xpath("//*[@id='mw-content-text']/div/table[1]", first = True).text

#print(text_infobox)

# for tr in text_infobox.find('tr'):
#     print(tr.text)

# images = r.html.find("img")
#
# for image in images:
#     link = "https:" + image.attrs["src"]
#     print(link)

# facts = r.html.find("p")
#
# rand_fact = random.choice(facts)
#
# print(rand_fact.text)

title = "h1"
titles = r.html.find(title)

for title in titles:
    t.append(title.text.replace("[edit]",""))


links = list(r.html.absolute_links)

resources = t + links

print(resources)

