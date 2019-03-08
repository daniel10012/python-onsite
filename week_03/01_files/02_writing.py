'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

#DONE

#reverse the whole text
with open("words.txt", "r") as fin:
    text = fin.read()
    reversed_text = text[::-1]
    print(reversed_text)

#reverse words
# with open("words.txt","r") as fin:
#     words = fin.read().split()
#     reversed_words = words[::-1]
#reverse lines
# with open("words.txt","r") as fin:
#     lines = [i for i in fin]
#     rev_lines = lines[::-1]
#     print(rev_lines)

    # with open("words_reverse.txt","w") as fout:
    #     fout.write(reversed_text)




