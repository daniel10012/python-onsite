'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''


def sed(pattern_string, replacement_string, file1,file2):
    try:
        with open(file1,"r") as fin:
            content = fin.readlines()
    except FileNotFoundError:
        print(f"{file1} doesn't exist")


    try:
        with open(file2, "w") as fout:
            for line in content:
                new_line = line.replace(pattern_string,replacement_string)
                fout.write(new_line)
    except UnboundLocalError:
        pass

sed("strings", "Notstrings", "words3.txt", "wordss3.txt")

