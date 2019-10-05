'''
Created on August 10th 2016
@author: Thierry Souche

This modules contains few generic functions which are useful to interact with the MongoDB server.

'''

from pymongo import MongoClient


# server parameters: address and mode (test/production)

production = False
mongoserver_prod_address = '127.0.0.1'
mongoserver_prod_port = 27017
mongoserver_test_address = '127.0.0.1'
mongoserver_test_port = 27017


# generic methods to access the relevant collections in the Mongo database

def getSetDB():
    if production:
        return MongoClient(mongoserver_prod_address, mongoserver_prod_port).set_game
    else:
        return MongoClient(mongoserver_test_address, mongoserver_test_port).test_set_game

def getPlayersColl():
    setDB = getSetDB()
    return setDB.players

def getGamesColl():
    setDB = getSetDB()
    return setDB.gamesColl
    


