'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''


num1 = int(input("input a number"))
num2 = int(input("input another number"))

for num in range(num1,num2+1):
    print(num**2)

