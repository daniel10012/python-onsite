'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


def shortest(list_):
    unique_words = set(list_)
    dict = {word: len(word) for word in unique_words}
    min_lenght = min(dict.values())
    shortest_words = []
    for key, value in dict.items():
       if value == min_lenght:
           shortest_words.append(key)
    return shortest_words

def longest(list_):
    unique_words = set(list_)
    dict = {word: len(word) for word in unique_words}
    max_lenght = max(dict.values())
    longest_words = []
    for key, value in dict.items():
       if value == max_lenght:
           longest_words.append(key)
    return longest_words




with open("words.txt", "r") as fin:
    word_list = (fin.read().split())

    print(shortest(word_list))
    print(longest(word_list))
    print(len(word_list))


