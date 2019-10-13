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
mongoserver_prod_DB = 'set_game'
mongoserver_test_address = '0.0.0.0'
mongoserver_test_port = 27017
mongoserver_test_DB = 'set_game_test'

mongo_username = 'db_admin_tes'
mongo_password = 'db_passwd_test'

players_collection = 'players'
games_collection = 'games'
log_collection = 'logs'

# generic methods to access the relevant collections in the Mongo database

def getSetDB():
    mongo_URI_prefix = "mongodb://{}:{}@".format(mongo_username, mongo_password)
    if production:
        mongo_URI = "{}{}:{}".format(mongo_URI_prefix, mongoserver_prod_address, mongoserver_prod_port)
        database = mongoserver_prod_DB
    else:
        mongo_URI = "{}{}:{}".format(mongo_URI_prefix, mongoserver_test_address, mongoserver_test_port)
        database = mongoserver_test_DB
    print("HELLO: mongo URI = '{}'".format(mongo_URI))
    db = MongoClient(mongo_URI)[database]
    print("HELLO: type of DB is '{}'".format(type(db)))
    return db

def getPlayersColl():
    setDB = getSetDB()
    return setDB[players_collection]

def getGamesColl():
    setDB = getSetDB()
    return setDB[games_collection]

def getLogColl():
    setDB = getSetDB()
    print("HELLO: setDB type is '{}'".format(type(setDB)))
    print("HELLO: setDB.log_collection type is '{}'".format(type(setDB[log_collection])))
    return setDB[log_collection]

def writeLogToDB(log_info):
    logColl = getLogColl()
    id = logColl.insert_one({'Info': log_info}).inserted_id
    print("Log ID = ",id)


