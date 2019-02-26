'''
Write a script that finds the first vowel in a a user inputted string.

'''

def is_vowel(letter):
    if letter.lower() in ("a","e","i","o","u","y"):
        return True
    else:
        return False


def first_vowel(word):
    for i in word:
        if is_vowel(i):
            return i
            break


print(first_vowel("khdgjwrgoqvkn"))