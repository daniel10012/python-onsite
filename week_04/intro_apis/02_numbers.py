'''
Write a script that connects to the http://numbersapi.com/ and fetches trivia on all
numbers from 0 through 100.

Store the responses in a new JSON file called numbers.json

BONUS:
* fetch information of all the prime numbers from 1-1000
* cycle through the different endpoints the API provides (trivia, math, date, year)
  in a way that they change in binary chunks, e.g.:
  - the info on the first 2 numbers are of type trivia
  - info on the next 4 numbers are of type math
  - the next 8 are on dates
  - etc. (cycle back to the trivia after year)

'''

import requests
import json

def is_prime(i):
    flag = True
    for j in range(2,i):
        if i % j == 0:
            flag = False
            break
    return(flag)

base_url = "http://numbersapi.com/"
extension = "/year?json"

dict_numbers = {}

#Trivia on all numbers between 0 and 100 in numbers.json

# with open("numbers.json", "w") as fout:
#     for i in range(0,101):
#         current_url = base_url + str(i) + extension
#         r = requests.get(current_url).json()
#         dict_numbers[i] = r["text"]
#     json.dump(dict_numbers,fout)

#Trivia on all prime numbers between 0 and 1000

with open("prime_numbers.json","w") as fout:
    prime_dict = {}
    for i in range(2,1000):
        if is_prime(i):
            current_url = base_url + str(i) + extension
            r = requests.get(current_url).json()
            prime_dict[i] = r["text"]
    json.dump(prime_dict,fout)










