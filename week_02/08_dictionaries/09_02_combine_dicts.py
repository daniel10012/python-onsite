'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''


dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}



dict_1.update(dict_2)
print(dict_1)
dict_1.update(dict_3)
print(dict_1)

for key,value in dict_1.items():
    print(key,value)



#newdict = dict(dict_1.items() + dict_2.items())



# print(newdict)