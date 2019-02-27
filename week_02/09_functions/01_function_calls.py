'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''



def square(number):
    return number**2

def circumference(r):
    return 3.14 * square(r)

def third_power(number):
    return square(number)*number

print(square(2))
print(circumference(4))
print(third_power(3))