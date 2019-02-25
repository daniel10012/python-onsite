my_list =[9,4,6,2,3,7,8,1,3,9]

my_sorted_list =[]

for i in range(0, len(my_list)):
    my_sorted_list.append(min(my_list))
    my_list.remove(min(my_list))

print(my_list, my_sorted_list)


# def sorting(list):
#     my_sorted_list.append(min(list))
#     list.remove(min(mylist))

