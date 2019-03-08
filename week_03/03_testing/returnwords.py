
def return_word(word, character):
    '''returns True if the first letter of the word is character, not case sensitive'''
    if word == "":
        return False
    if type(word)  != str or type(character) != str:
        return False
    if word[0].lower() == character.lower():
        return True
    else:
        return False


if __name__ == '__main__':

    print(return_word("Waga","w"))
    print(return_word("ours","b"))
    # print(return_word("ours", 4))
    # print(return_word("ee","w"))
