'''
Using the PokéAPI https://pokeapi.co/docs/v2.html#pokemon
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''


import requests
import os

url = "https://pokeapi.co/api/v2/pokemon/"
url_img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/.png"

for i in range(1,2):
    current_url = url +str(i)+"/"
    r = requests.get(current_url).json()
    name = r["forms"][0]["name"]
    height = r["height"]
    img_link = url_img+str(i)+".png"
    img = requests.get(img_link)
    dirname = "images"
    filename = f"images/{name}.png"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as f:
        f.write(img.content)

