'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''

number = int(input("enter a number btw 1 and 7"))

if number == 1:
    print("monday")
elif number == 2:
    print("tuesday")
elif number == 3:
    print("wednesday")
elif number == 4:
    print("thursday")
elif number == 5:
    print("friday")
elif number == 6:
    print("saturday")
elif number == 7:
    print("sunday")


