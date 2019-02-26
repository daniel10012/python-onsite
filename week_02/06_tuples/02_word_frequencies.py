'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency.

For example, the follow string should produce the following result.

string_ = 'hello'

Output:
l, h, e, o

For letters that are the same frequency, the order does not matter.

'''

my_string = "hello"

letters_count = []


for i in my_string :
    tup = (i, my_string.count(i))
#    print (tup)
    if tup not in letters_count:
        letters_count.append(tup)

print(letters_count)

def secondelement(list1):
    return list1[1]

letters_count.sort(key=secondelement, reverse=True)

print(letters_count)

letters =[]
for i in letters_count:
    letters.append(i[0])

result = ",".join(letters)

print(result)
