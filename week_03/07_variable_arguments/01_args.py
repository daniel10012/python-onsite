'''
Write a script with a function that demonstrates the use of *args.

'''

def my_funct(name,*args):
    print(name)
    print(args[-1])
    for item in args:
        print(item)


print(my_funct("bob", "michel",3,"jim",9,True))





