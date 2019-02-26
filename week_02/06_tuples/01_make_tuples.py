'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''

my_list = [5,3,32,1,3,9,5,3,2,2,5]

my_list.sort()

if len(my_list) % 2 != 0:
    my_list.append(0)
#
print(my_list)

pairs = [(my_list[i], my_list[i+1]) for i in range(0,len(my_list),2)]

print(pairs)

for i in pairs:
    print(i)









