# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI and copy and paste
the commands and results below.

- Navigate to your home directory
- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.
- Move into the CodingNomads folder
- Create new folder cli_testing
- Inside of folder cli_testing,
    a. print the directory path
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)
    c. list the contents of the folder
    d. rename one of the files
- Inside of folder cli_testing, create a new folder
- Copy a file from cli_testing to the new folder
- Move a different file from cli_testing to the new folder
- Demonstrate removing:
    a. A file
    b. A folder
'''
cd ~
mkdir "CodingNomads"
cd CodingNomads/
mkdir "cli_testing"
cd cli_testing/
pwd
touch "file1.txt"
touch "file2.txt"
touch "file3.txt"
ls -al
mv "file3.txt" "file4.txt"  
mkdir "new_folder"
cp text1.txt new_folder/
mv file2.txt new_folder/
rm file1.txt
rm -r new_folder/
'''

## vim

- Use `$ vim` to write some text inside a file
- Use `$ cat` print contents of file
- Use `$ grep` to search for a word inside file

vim hello.txt 
i
"hello"
:wq

cat hello.txt
grep "o" hello.txt



## explore advanced CLI

- What is the difference between the two commands > and >>?
- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt
- Overwrite the content of my_file.txt with "tell me"

overwrite , append
echo "tell me" > my_file.txt




