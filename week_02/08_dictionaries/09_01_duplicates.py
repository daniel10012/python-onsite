'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.


'''

# [a,b,d,s,w,q,a]

def has_duplicates(list_):
    dict = {}
    for i in list_:
        dict[i] = list_.count(i)

    print (dict)
    for value in dict.values():
        if value >1:
            return True
    return False

print(has_duplicates([2,3,4,2,3,2,45,4]))
print(has_duplicates([1,2,3,4,5,6,7,8,9]))

