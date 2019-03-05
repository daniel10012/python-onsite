'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

number1 =""
while type(number1) != int:
    try:
        number1 = int(input("please input a integer"))
    except ValueError:
        print("this is not an integer")

number2 =""
while type(number2) != int or number2 == 0:
    try:
        number2 = int(input("please input a integer"))
    except ValueError:
        print("this is not an integer")
    else:
        try:
            print(f"the result is {number1/number2}")
        except ZeroDivisionError:
            print("you can't divide by zero !")

