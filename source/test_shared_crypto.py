'''
Created on Dec 27, 2016

@author: thierry
'''

import unittest

from app_reference_test_data import refPlayers, refPlayers_Dict
from app_shared_crypto import encryptPassword, checkPassword
from app_shared_db import getPlayersColl
from test_utils import vbar, vprint


class test_Shared_Crypto(unittest.TestCase):
    """
    This class unit-test the shared functions declared in the 'constants' 
    module.
    """

    def setUp(self, gameIDNone = True):
        # Connection to the MongoDB server / players collection
        playersColl = getPlayersColl()
        # populate db with test data about players
        playersColl.drop()
        for pp in refPlayers():
            if gameIDNone:
                playersColl.insert_one({'_id': pp['playerID'],
                                'nickname': pp['nickname'],
                                #'password': pp['password'],
                                'passwordHash': pp['passwordHash'],
                                'totalScore': pp['totalScore'],
                                'gameID': None})
            else:
                playersColl.insert_one({'_id': pp['playerID'],
                                'nickname': pp['nickname'],
                                #'password': pp['password'],
                                'passwordHash': pp['passwordHash'],
                                'totalScore': pp['totalScore'],
                                'gameID': pp['gameID']})
        return playersColl

    def teardown(self, players):
        players.playersColl.drop()

    def test_encryptPassword(self):
        vbar()
        print("Test shared_crypto.encryptPassword")
        vbar()
        # produce a hash for all reference players and check the verification is ok
        vprint("We create a new hash for all reference players and check the outcome:")
        for pp in refPlayers_Dict():
            new_hash = encryptPassword(pp['password'])
            self.assertTrue(checkPassword(pp['password'], new_hash))
            vprint("    > " + pp['nickname'] + "'s new hash is recognized")

    def test_checkPassword(self):
        vbar()
        print("Test shared_crypto.checkPassword")
        vbar()
        vprint("We check that all reference test player's (password + hash) is ok")
        for pp in refPlayers_Dict():
            self.assertTrue(checkPassword(pp['password'], pp['passwordHash']))
            vprint("    > " + pp['nickname'] + ": couple (password + hash) is ok")
        vprint("We now check that other couples are not ok:")
        for pp in refPlayers_Dict():
            for yy in refPlayers():
                if pp['nickname'] != yy['nickname']:
                    self.assertFalse(checkPassword(pp['password'], yy['passwordHash']))
                    vprint("    > " + pp['nickname']+ "'s password and " + yy['nickname'] + "'s hash do not correspond")

