'''
Created on August 10th 2016
@author: Thierry Souche

This modules contains few constants and functions which are used (and shared) across
several modules in the backend application.

'''

from bson.objectid import ObjectId
from app_shared_db import getPlayersColl


# parameters indicating the number of cards for the game
cardsMax = 81
tableMax = 12
playersMin = 4
playersMax = 6
pointsPerStep = 3

# useful function for ObjectIds shared by multiple modules

def oidIsValid(oid):
    """
    This function checks that the argument is a valid ObjectID (i.e.
    either a valid ObjectID, or a string representing a valid 
    ObjectId).
    """
    try:
        ObjectId(oid)
        return True
    except:
        return False


# useful function checking that a playerID is valid

def isPlayerIDValid(playerID):
    """
    This method checks that the playerID is valid (ie. it is a valid 
    ObjectId and the corresponding player exists in the DB).
    It return 'True' in this case, or 'False' in any other case.
    """
    playersColl = getPlayersColl()
    result = False
    if oidIsValid(playerID):
        pp = playersColl.find_one({'_id': playerID})
        result = (pp != None)
    return result




