'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''


sentence = "I love to work with dictionaries!"

# dict_sentence = {}
# for i in sentence:
#     if i == " ":
#         continue
#     dict_sentence[i] = sentence.count(i)


dict_sentence = {"Upper_case" : 0, "Lower_case" : 0 , "Punctuation" : 0 , "Characters" : 0 }

for i in sentence:
    if i == " ":
        continue
    if i in ["!", "?", ",", "."]:
        dict_sentence["Punctuation"] += 1
    elif i == i.upper():
        dict_sentence["Upper_case"] += 1
    elif i == i.lower():
        dict_sentence["Lower_case"] += 1

    dict_sentence["Characters"] += 1

print(dict_sentence)

for key, value in dict_sentence.items():
    print(key,": ",value)








