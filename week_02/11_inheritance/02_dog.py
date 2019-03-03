'''

Building on the dog class from the previous example, create a subclass of the dog class
with at least one additional attribute. Also, override the sleep() and eat() methods to act
slightly different.

Create and object of this class and demonstrate it's functionality.

'''
import time

from dog import Dog

class DEAdog(Dog):

    def __init__(self, name,color,age,is_hungry=False, percent_full=100, drug = "cocaine"):
        super().__init__(name,color,age,is_hungry=False, percent_full=100)
        self.drug = drug

    def __str__(self):
        if self.is_hungry == True:
            return (f"the dog is called {self.name}, he is {self.color} and he is {self.age} years old. He is "
                    f"{self.percent_full} percent full and hungry. He is ready to sniff {self.drug}")
        else:
            return (f"the dog is called {self.name}, he is {self.color} and he is {self.age} years old. He is "
                    f"{self.percent_full} percent full and not hungry. He is ready to sniff {self.drug}")

    def eat(self,food_item, amount):
        print(f"the dog ate {amount} of {food_item} and is ready to work")
        self.is_hungry = False
        self.percent_full = 100

    def sleep(self):
        time.sleep(3)
        self.is_hungry=True
        self.percent_full -= 30


dog_test = DEAdog("bob", "blue", 12, True, 50)

print(dog_test)

dog_test.eat("chicken", 5)

dog_test.sleep()

print(dog_test)

