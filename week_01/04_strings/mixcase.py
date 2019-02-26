'''
Write a script that takes a user inputted string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''

from first_vowel import is_vowel


my_string = "aerobAREiouUppP"

cap = my_string.upper()
minim = my_string.lower()


print(cap)
print(minim)

wave_word = ""

for i in my_string:
    if is_vowel(i):
        wave_word += i.lower()
    else:
        wave_word += i.upper()


print(wave_word)
