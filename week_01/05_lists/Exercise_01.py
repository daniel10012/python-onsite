'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''

my_list = [2,5,3,2,7,23]

sum_numbers = 0

for i in my_list:
    sum_numbers += i

print(sum_numbers)

average = sum_numbers/len(my_list)

print(average)