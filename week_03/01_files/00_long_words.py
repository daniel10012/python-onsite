'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''


with open("words.txt","r") as fin:
    # print((fin.read().split()))
    word_list = (fin.read().split())
    # print((fin.read().split()))
    # print(word_list)
    # print(word_list)
    #print(fin.read())
    for word in word_list:
        if len(word)>7:
            print(word)








