'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of all of
all .jpg files (with the complete path of the files).

If you are feeling bold, create a list for each kind of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then sub out the
folder name with a bigger folder. This program should work for any specified folder on your computer.


'''
import os

#find all files in a directory and subdirectories
def afil(directory):
    allfiles = []
    for root, dirs, files in os.walk(directory, topdown=False):
       for name in files:
          allfiles.append(os.path.join(root, name))
       for name in dirs:
          allfiles.append(os.path.join(root, name))
    return allfiles


def findjpg(directory):
    jpgfiles = []
    for file in afil("/Users/danielwegmann/Documents/CodingNomads"):
        if file[-4:] == ".jpg":
            jpgfiles.append(file)
    return jpgfiles

directory = "/Users/danielwegmann/Documents/CodingNomads"
#print (afil(directory))
#print (findjpg(directory))

filetypes = []
for file in afil(directory):
    if "." in file[-3]:
        filetypes.append(file[-3:])
    elif "." in file[-4]:
        filetypes.append(file[-4:])
unique_types = list(set(filetypes))

#print(unique_types)

dict_files_bytype = {}
for type in unique_types:
    for file in afil(directory):
        if type[-3:] == file[-3:]:
            if type not in dict_files_bytype:
                dict_files_bytype[type] = [file]
            else:
                dict_files_bytype[type].append(file)

#print(dict_files_bytype)

print(dict_files_bytype[".md"])
