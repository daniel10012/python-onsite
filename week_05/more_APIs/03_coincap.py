'''
Sign up for an API key with the new coinmarketcap API.

Using their documentation, fetch all listed cryptocurrencies.
From the result, create a new JSON file that includes the following:
* cmc_rank
* name
* symbol
* platform
* quote

Save that info to a file.

'''

from config import COIN_KEY

# This example uses Python 2.7+ and the python-request library
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COIN_KEY,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


with open("cryptos.json","w") as fout:
    list_coins = []

    for coin in data["data"]:
        dict_coin = {}
        dict_coin["name"] = coin["name"]
        dict_coin["cmc_rank"] = coin["cmc_rank"]
        dict_coin["platform"] = coin["platform"]
        dict_coin["symbol"] = coin["symbol"]
        dict_coin["price"] = round(coin["quote"]["USD"]["price"])
        list_coins.append(dict_coin)
    #print(list_coins)

    json.dump(list_coins,fout)