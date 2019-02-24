'''
Print pi to the console using the following formula:
note that this is not the complete series to compute the true number pi.
Challenge: find another way to do this using a package you can import

4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11))

'''


operator = -1
x = 1

for i in range(3, 1000, 2):
    if operator == 1:
        x += 1/i
    else:
        x -= 1/i

operator *= -1

print(4*x)


import math
print(math.pi)