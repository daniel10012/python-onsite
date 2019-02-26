'''
The following functions are all intended to check whether a string
contains any lowercase letters, but at least some of them are wrong.
For each function, write its docstring to describe what the function
actually does (assuming that the parameter is a string).



'''

def any_lowercase1(s):
    """
    any_lowercase1(B) -> bool

    Return True if the first letter of string B is lowercase and there is
    at least one cased character in B, False otherwise.
    """

    for c in s:
        if c.islower():
            return True
        else:
            return False



def any_lowercase2(s):
    """
    any_lowercase2(B) -> bool

    Return True all the time
    """

    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'



def any_lowercase3(s):
    """
    any_lowercase3(B) -> bool

    Return True if the last letter of string B is lowercase and there is
    at least one cased character in B, False otherwise.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """
    any_lowercase4(B) -> bool

    Return True if at least one letter of string B is lowercase and there is
    at least one cased character in B, False otherwise.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """
    any_lowercase5(B) -> bool

    Return True if all letters of string B are lowercase and there is
    at least one cased character in B, False otherwise.
    """
    for c in s:
        if not c.islower():
            return False
    return True


a = "Ab"
print(any_lowercase1(a))
print(any_lowercase2(a))
print(any_lowercase3(a))
print(any_lowercase4(a))
print(any_lowercase5(a))

