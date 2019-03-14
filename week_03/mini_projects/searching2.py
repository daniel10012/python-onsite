import os

start_folder = "/Users/danielwegmann/Documents"

my_dictionary = {}

# for i in os.walk(start_folder):
#     print(i)

dirs = [file[0] for file in os.walk(start_folder)]
files = [file[2] for file in os.walk(start_folder)]

for index, dir in enumerate(dirs):
    for file in files[index]:
        if file[-3:] == "jpg":
            if dir not in my_dictionary.keys():
                my_dictionary[dir] = []
            my_dictionary[dir].append(file)

print(my_dictionary)