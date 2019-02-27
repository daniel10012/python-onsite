'''
Write a function that takes in a list and finds the max, min, average and sum.

'''

def list_properties(my_list):
    properties = {}
    properties["max"] = max(my_list)
    properties["min"] = min(my_list)
    properties["sum"] = sum(my_list)
    properties["average"] = sum(my_list)/len(my_list)
    return properties


list1 = [0,4,2,2,7,5,45,2,23]

print(list_properties(list1))