'''
Created on August 19th 2016
@author: Thierry Souche

This modules contains few constants and functions which are useful for other 
unit test modules.
'''


from bson.objectid import ObjectId
from reference_test_data import refGames_Dict

"""
Set verbose = True enable to capture many comments during unitary testing.
Set verbose = False does not produce the comments.
"""
verbose = True

# logging functions (for tests)

def vprint(arg="\n"):
    if verbose:
        print(arg)

def vbar():
    vprint("------------------------------------------------------------------------")

def cardsList(nb):
    """
    This function return a list of 'nb' integers, from 0  to nb-1
    """
    lst = []
    if nb>1:
        for i in range(0,nb):
            lst.append(i)
    return lst
