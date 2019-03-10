'''
User python's built-in .enumerate() function to print the classes
together with their numbers from 1-4.


NOTE: a less readable, but common structure in other languages would be:

for i in range(len(courses)):
    print(f"{i}: {courses[i]} python")

'''

classes = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

a = enumerate(classes)

for i in a:
    print (i)

for index, value in enumerate(classes, start=1):
    print(index, value)

for i in range(len(classes)):
    print(f"{i}: {classes[i]} python")