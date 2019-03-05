'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

try:
    with open("integers.txt","r")as fin:
        numbers = fin.read().split()

except FileNotFoundError:
            print("this file doesn't exist")


print(numbers)



