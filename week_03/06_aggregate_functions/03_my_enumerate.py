'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''


def my_enumerate(list_):
    enum = []
    for i in range(len(list_)):
        enum.append((list_[i] , i))
    return enum

print(my_enumerate(['Intro', 'Intermediate', 'Advanced', 'Epic Hero']))