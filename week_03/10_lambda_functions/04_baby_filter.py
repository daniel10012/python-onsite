'''
You're about to have a baby and you don't have a name yet. 😱
You and your partner agree that it should start with an 'M', but that's
about all you've got so far.

To save the day, use the filter() method and a lambda expression
to map all the baby names that begin with a 'M' to an output list.

'''

names = ['Olivia', 'Noah', 'Ava', 'Oliver', 'Isabella', 'Mason', 'Sophia', 'Logan', 'Emma', 'Liam', 'Amelia', 'Lucas', 'Mia', 'Elijah', 'Charlotte', 'Ethan', 'Harper', 'James', 'Mila', 'Aiden', 'Aria', 'Carter', 'Ella', 'Jackson', 'Evelyn', 'Alexander', 'Avery', 'Sebastian', 'Abigail', 'Michael', 'Emily', 'Benjamin', 'Luna', 'Jacob', 'Riley', 'William', 'Scarlett', 'Grayson', 'Chloe', 'Jack', 'Sofia', 'Daniel', 'Layla', 'Owen', 'Lily', 'Luke', 'Madison', 'Henry', 'Ellie', 'Wyatt', 'Zoey', 'Jayden', 'Elizabeth', 'Leo', 'Penelope', 'Gabriel', 'Victoria', 'Julian', 'Grace', 'Matthew', 'Nora', 'David', 'Aubrey', 'Jaxon', 'Camila', 'Levi', 'Hannah', 'Mateo', 'Bella', 'Asher', 'Aurora', 'Lincoln', 'Addison', 'John', 'Stella', 'Samuel', 'Skylar', 'Muhammad', 'Paisley', 'Ryan', 'Savannah', 'Adam', 'Maya', 'Isaac', 'Natalie', 'Nathan', 'Elena', 'Josiah', 'Emilia', 'Isaiah', 'Violet', 'Joseph', 'Hazel', 'Caleb', 'Nova', 'Anthony', 'Niamey', 'Hunter', 'Eva', 'Eli']


namem = lambda x: x if x[0].lower() == "m" else None
m_names = list(filter(namem , names))

names_m =lambda names: [name for name in names if name[0].lower() == "m"]
a = names_m(names)

print(m_names)
print(a)

# number_list = range(-5, 5)
# less_than_zero = list(filter(lambda x: x < 0, number_list))
# print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]