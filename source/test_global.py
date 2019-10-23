'''
Created on Sep 2, 2016
@author: Thierry Souche
'''

from bson.objectid import ObjectId
import unittest

from test_shared import test_Shared
from test_shared_db import test_Shared_DB
from test_shared_crypto import test_Shared_Crypto
from test_cardset import test_CardSet
from test_step import test_Step
from test_players import test_Players
from test_game import test_Game
from test_backend import test_Backend


if __name__ == "__main__":

    test_classes_to_run = [test_Shared, test_Shared_DB, test_Shared_Crypto,
        test_CardSet, test_Step, test_Players, test_Game, test_Backend]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
