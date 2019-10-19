'''
Created on August 10th 2016
@author: Thierry Souche

This modules contains few generic functions which are useful to interact with the MongoDB server.

'''

from pymongo import MongoClient


# server parameters: address and mode (test/production)

production = False
mongoserver_prod_address = 'localhost'
mongoserver_prod_port = 27017
mongoserver_prod_DB = 'set_game'
mongoserver_test_address = 'localhost'
mongoserver_test_port = 27017
mongoserver_test_DB = 'set_game_test'

#mongo_username = 'db_admin_test'
#mongo_password = 'db_passwd_test'

players_collection = 'players'
games_collection = 'games'
log_collection = 'logs'

# generic methods to access the relevant collections in the Mongo database

def getSetDB():
    # The following line is used if we restrict the access to the mongo db
    # with credentials (which must appear in the mongo URI).
    #mongo_URI_prefix = "mongodb://{}:{}@".format(mongo_username, mongo_password)
    mongo_URI_prefix = "mongodb://"
    if production:
        mongo_URI = "{}{}:{}".format(mongo_URI_prefix, mongoserver_prod_address, mongoserver_prod_port)
        database = mongoserver_prod_DB
    else:
        mongo_URI = "{}{}:{}".format(mongo_URI_prefix, mongoserver_test_address, mongoserver_test_port)
        database = mongoserver_test_DB
    #print("HELLO: mongo URI = '{}'".format(mongo_URI))
    db = MongoClient(mongo_URI)[database]
    return db

def getPlayersColl():
    setDB = getSetDB()
    return setDB[players_collection]

def getGamesColl():
    setDB = getSetDB()
    return setDB[games_collection]

def getLogColl():
    setDB = getSetDB()
    return setDB[log_collection]

def writeLogToDB(log):
    logColl = getLogColl()
    id = logColl.insert_one(log).inserted_id
    #print("Log ID = ",id)
