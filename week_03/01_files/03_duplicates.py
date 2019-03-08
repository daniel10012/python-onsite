'''
In a large collection of MP3 files, there may be more than one copy of
the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a
given suffix (like .mp3). Hint: os.path provides several useful
functions for manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for
each file. If two files have the same checksum, they probably have the
same contents. To double-check, you can use the Unix command diff.
Solution: http://thinkpython2.com/code/find_duplicates.py.

Go and tackle your duplicate files! :)

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''

import os
import hashlib

#returns a hexadigest hashing of a portion of a file
def hashing(file):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

#find all files in current directory and subdirectories
allfiles = []
for root, dirs, files in os.walk("files", topdown=False):
   for name in files:
      allfiles.append(os.path.join(root, name))
   for name in dirs:
      allfiles.append(os.path.join(root, name))

#keeping only .jpg files
jpgfiles = allfiles.copy()
for file in jpgfiles:
    if file[-4:] != ".jpg":
        jpgfiles.remove(file)

#making dictionary of hashes: key = hash value = list of same files
dictjpg = {}
for file in jpgfiles:
    h = hashing(file)
    if h not in dictjpg.keys():
        dictjpg[h] = [file]
    else:
        dictjpg[h].append(file)


#telling the user which files are the same
for key, value in dictjpg.items():
    if len(dictjpg[key]) > 1:
        print(f"the files {value} are the same")













