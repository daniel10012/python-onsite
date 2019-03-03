'''
Building on the dog exercise in the previous section:

1. Create a dog class and make the functions from the last class methods of the dog class.

2. Add an __init__() method that sets the following attributes:

    - name
    - color
    - age
    - is_hungry (should be a boolean)
    - percent_full

    Note: is_hungry should default to False, and percent_full should default to 100.

3. Change the sleep() method so that when the method is called, the attribute is_hungry is set to True
    and the attribute percent_full is decremented by 20 percent.

4. Change the eat() method so that when the method is called, the attribute is_hungry is set to False
    and the attribute percent full is incremented to 100.

5. Add a __str__() method to print out all the information about the dog.

6. Create at least two objects of the dog class to demonstrate the functionality.




'''

import time

class Dog:

    def __init__(self, name,color,age,is_hungry=False, percent_full=100):
        self.name = name
        self.color = color
        self.age = age
        self.is_hungry = is_hungry
        self.percent_full = percent_full

    def __str__(self):
        if self.is_hungry == True:
            return(f"the dog is called {self.name}, he is {self.color} and he is {self.age} years old. He is "
                      f"{self.percent_full} percent full and hungry")
        else:
            return(f"the dog is called {self.name}, he is {self.color} and he is {self.age} years old. He is "
              f"{self.percent_full} percent full and not hungry")


    def bark(self):
        print("bark bark")

    def eat(self,food_item, amount):
        print(f"the dog ate {amount} of {food_item}")
        self.is_hungry = False
        self.percent_full = 100

    def sleep(self):
        time.sleep(5)
        self.is_hungry=True
        self.percent_full -= 20



if __name__ == '__main__':
    dog1 = Dog("bob", "black", 12)
    dog2 = Dog("roger", "white",43, True, 0)

    print(dog1)
    print(dog2)

    dog1.sleep()
    print(dog1)
    dog1.eat("chicken",4)
    print(dog1)