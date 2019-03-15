'''
Using the JavaScript support in requests_html, parse the contents of
an Instagram page you are interested in.

Fetch and prepare all the image links - and only the image links!
* How can you exclude other links present on the page?
* BONUS: Can you find a way to download those images and save them to
         your computer using python?

'''

from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.instagram.com/martin.breuss/')
r.html.render()




list_img = [link for link in r.html.absolute_links if link[:28] == "https://www.instagram.com/p/"]


print(list_img)


























