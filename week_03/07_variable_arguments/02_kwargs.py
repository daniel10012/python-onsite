'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def fun(name, **kwargs):
    for key,value in kwargs.items():
        print(f"{key} maps to {value}.")

fun("bob", lastname="george", age=13, hair="grey")