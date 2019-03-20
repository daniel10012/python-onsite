'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''

import requests

url1 = "https://restcountries.eu/rest/v2/name/france?fullText=true"
url2 ="https://restcountries.eu/rest/v2/name/germany?fullText=true"

r1 = requests.get(url1).json()
r2 = requests.get(url2).json()


country1 = r1[0]["name"]
country2 = r2[0]["name"]
population1 = r1[0]["population"]
population2 = r2[0]["population"]
area1 = r1[0]["area"]
area2 = r2[0]["area"]

if population1 > population2:
    print(f"{country1} is more populous than {country2}")
else:
    print(f"{country2} is more populous than {country1}")

print(f"the difference in area is {abs(population2-population1)} sq km")

print(f"{r1[0]['nativeName']} has for capital {r1[0]['capital']}")
print(f"{r2[0]['nativeName']} has for capital {r2[0]['capital']}")