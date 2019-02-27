'''
Demonstrate the use of the "break" statement to exit a loop.

'''

n = 1000

while True:
    print(n)
    if n == 500:
        break
    n -= 1
