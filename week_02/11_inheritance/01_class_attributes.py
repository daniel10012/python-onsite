
'''
Flush out the classes below with the following:

    - Add inheritance so that Class1 is inherited by Class2 and Class2 is inherited by Class3.
    - Follow the directions in each class to complete the functionality.



'''

class Class1:
    def __init__(self, x):
        self.x = x
    # define an __init__() method that sets an attribute x


class Class2(Class1):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    # define an __init__() method that sets an attribute y and calls the __init__() method of its parent


class Class3(Class2):
    def __init__(self, x, y,z):
        super().__init__(x,y)
        self.z = z

    # define an __init__() method that sets an attribute z and calls the __init__() method of its parent



# create an object of each class and print each of its attributes

obj1 = Class1(3)
obj2 = Class2(4, 5)
obj3 = Class3(7, 9, 8)

print(obj3.y)