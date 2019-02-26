'''
Sum up all elements from the nested list of integers below.

'''

list_ = [1, 2, [10, 11], [42, 3], 9]


sum_nums = 0
for i in list_:
    if type(i) == int:
        sum_nums += i
    if type(i) == list:
        sum_nums += sum(i)


print(sum_nums)