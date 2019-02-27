'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''

num1 = int(input('enter a first number'))
num2 = int(input("enter a second number"))

num = num1
sum_nums = 0
counter = 0

while num <= num2:
    sum_nums += num
    num += 1
    counter += 1

print (sum_nums)
print(sum_nums/counter)