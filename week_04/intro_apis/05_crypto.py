'''
http://docs.nomics.com/
Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- request an API key first and remember to include it in your queries
- the /prices endpoint of the nomics API can be used for achieving this task
- remember to use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the logging package for easier tracking

'''

import os
import requests
from secrets import NOMICS_KEY
from pprint import pprint
import time
import json


url = "https://api.nomics.com/v1/prices?key=" + NOMICS_KEY

currencies = requests.get(url).json()

print(currencies)

for index, currency in enumerate(currencies):
    if currency["currency"] == "BTC":
        index_BTC = index

s=0
quotes={}
while s<=360:
    currencies = requests.get(url).json()
    price = currencies[index_BTC]["price"]
    quotes[time.asctime()] = price
    s+=1
    time.sleep(10)



with open("quotes.json", "w") as fout:
    json.dump(quotes, fout)


#quotes = {'Fri Mar 29 05:13:29 2019': '4035.61034', 'Fri Mar 29 05:13:32 2019': '4095.60034', 'Fri Mar 29 05:13:36 2019': '4005.1034', 'Fri Mar 29 05:13:39 2019': '4045.61034'}

date_max = max(quotes.keys(), key=lambda x: quotes[x])
price_max = quotes[date_max]
date_min = min(quotes.keys(), key=lambda x: quotes[x])
price_min = quotes[date_min]

print(date_max, price_max)
print(date_min, price_min)