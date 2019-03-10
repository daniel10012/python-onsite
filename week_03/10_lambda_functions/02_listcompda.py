'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

print([x.startswith('D') for x in names])

print(map(lambda x: x.startswith('D'),names))

print(list(map(lambda x: x.startswith('D'),names)))

gen = map(lambda x: x.startswith('D'),names)

print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())


print(list(gen))



print(list(gen))


