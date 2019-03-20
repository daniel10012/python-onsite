'''
Using python's request library, retrieve the HTML of the website you created
that now lives online at <your-gh-username>.github.io/<your-repo-name>

BONUS: extend your python program so that it reads your original HTML file
       and returns True if the HTML from the response is the same as the
       the contents of the original HTML file.

'''


import requests

url = "https://daniel10012.github.io/staticpage/"

r = requests.get(url).text

with open("copymysite.html", "w") as fout:
    fout.write(r)

with open("copymysite.html", "r") as fin:
    content_copy = fin.read()
    if r == content_copy:
        print("the 2 files are identical")

with open("original.html", "r") as fin:
    content_original = fin.read()
    if r == content_original:
        print("site = original")