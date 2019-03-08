'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

try:
    with open("integerss.txt","r")as fin:
        numbers = fin.read().split()

except FileNotFoundError:
    print("this file doesn't exist")

try:
    first_number = int(numbers[0])
    print(first_number + 5)
except NameError:
    pass





