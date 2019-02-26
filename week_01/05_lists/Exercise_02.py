'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]

common_list = []
dif_list = []

for i in list_two:
    if i in list_one:
        common_list.append(i)
    else:
        dif_list.append(i)

print(common_list)
print(dif_list)