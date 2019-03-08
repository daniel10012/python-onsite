'''
Download http://thinkpython2.com/code/anagram_sets.py.
You’ll see that it creates a dictionary that maps from a sorted string
of letters to the list of words that can be spelled with those letters.
For example, 'opst' maps to the list:
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”;
read_anagrams should look up a word and return a list of its anagrams.
Solution: http://thinkpython2.com/code/anagram_db.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
#DONE

from anagram_sets import *
import random


# d = all_anagrams("words.txt")
#
# print(d)
# print(filter_length(d,6))
# print_anagram_sets(d)
# print_anagram_sets_in_order(d)


#stores anagram dictionnaries in a list
def store_anagrams(file_names):
    shelf = []
    for file in file_names:
        shelf.append(all_anagrams(file))
    return shelf

def read_anagrams(word,file_name):
    d = all_anagrams(file_name)
    s = signature(word)
    try:
        print(d[s])
    except KeyError:
        print(f"no anagrams of \"{word}\" were found in {file_name}")

read_anagrams("ospt","words.txt")

print(store_anagrams(["words.txt","words2.txt"]))


#just fun function finding all anagrams of a word way too long with random
# def anagram(word):
#     letters = list(word)
#     anag = word
#     anags = []
#     while len(anags) < 2:
#         if anag not in anags:
#             anags.append(anag)
#             random.shuffle(letters)
#             anag = ''.join(letters)
#         else:
#             continue
#     return anags
#
# print(anagram("abc"))


#anagram("rwg")
