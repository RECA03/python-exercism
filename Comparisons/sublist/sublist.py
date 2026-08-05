"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
from ast import Eq
from operator import is_


SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

#THE LIST ELEMENTS HAVE TO BE IN THE SAME ORDER, current solution doesnt account for that.

def is_contiguous_subsequence(sublist, superlist):
    """True if needle appears as one contiguous block inside haystack."""
    if not sublist:
        return True
    size = len(sublist)
    for i in range(len(superlist) - size + 1): 
        if superlist[i : i + size] == sublist:
            return True
    return False

def sublist(list_one, list_two):
    
    if list_one == list_two:
        return EQUAL
    if not list_one:
        return SUBLIST
    if not list_two:
        return SUPERLIST

    if len(list_one) < len(list_two) and is_contiguous_subsequence(list_one, list_two):
        return SUBLIST
    elif len(list_one) > len(list_two) and is_contiguous_subsequence(list_two, list_one):
        return SUPERLIST
    
    return UNEQUAL
        
            
