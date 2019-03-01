'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''
import math

class Point:
    """Represents a point.

    attributes: abscisse, ordinate.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return(f"this point had an abscisse of {self.x} and an ordinate of {self.y}")


    def distance(self, other_point):
        a = abs(self.x - other_point.x)
        b = abs(self.y - other_point.y)
        distance = math.sqrt(a**2+b**2)
        return distance

# my_point1 = Point(2,3)
#
# my_point2 = Point(-3,7)
#
# print(my_point2)
#
# print(my_point1.distance(my_point2))


'''As an exercise, write a function named move_rectangle that takes a Rectangle and two numbers named dx and dy.
 It should change the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y 
 coordinate of corner.'''

