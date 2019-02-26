'''
There are many string methods available to perform all sorts of tasks.

Experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.

Python documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate
optional arguments. So sub is required, but start is optional, and if
you include start, then end is optional.

For this exercise, demonstrate the following string methods below:
- strip
- replace
- find

'''

my_string = "Bonjour Daniel comment ca va ca Daniel"

my_string = my_string.strip()

print(my_string)

print(my_string.replace("Daniel", "Bob",1))

song = 'Let it be, let it be, let it be, let it be'

'''only two occurences of 'let' is replaced'''
print(song.replace('let', "don't let", 1))

print(my_string.find("Daniel", 9 , 30))



