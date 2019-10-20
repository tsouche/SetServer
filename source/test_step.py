'''
Created on August 5th 2016
@author: Thierry Souche
'''

import unittest

from app_step import Step
from app_reference_test_data import refGames_Dict
from test_utils import vprint, vbar, refCardsets, refSetsAndPlayers
from test_utils import stepDict_to_Step, refSteps
from test_utils import step_equality, stepDict_equality


class test_Step(unittest.TestCase):
    """
    This class is used to unit-test the Step class.
    The setup method will load test data, and the teardown method will clean the
    database.
    """

    def refStepStarts_Dict(self):
        """
        List of reference Step dictionaries, generated by the Step.start(cardset) 
        method, with the corresponding cardsets above.
        This function will only provide with the FIRST iteration of a Step, 
         
        NB:These test data are complementary to the 'refStep_dict' and 'refSteps'
        available from 'test_utilities' and specific to the testing of the
        'Step' class.
        """
        Dict = []
        # This Step will be produced with the Cardset 1, which does NOT contain a
        # valid set amongts the 12 first cards: it forces to get and grab the 13th
        # card to put it on the table, and it pushes the 12th card at the end of 
        # the pick.
        Dict.append({'__class__': 'SetStep', 'turnCounter': '0', 
            'playerID': 'None', 'nickname': '', 
            'table': ['00-00', '01-01', '02-02', '03-03', '04-04', '05-05', 
                      '06-06', '07-07', '08-08', '09-09', '10-10', '11-12'], 
            'pick':  ['00-13', '01-14', '02-15', '03-16', '04-17', '05-18', 
                      '06-19', '07-20', '08-21', '09-22', '10-23', '11-24', 
                      '12-25', '13-26', '14-27', '15-28', '16-29', '17-30', 
                      '18-31', '19-32', '20-33', '21-34', '22-35', '23-36', 
                      '24-37', '25-38', '26-39', '27-40', '28-41', '29-42', 
                      '30-43', '31-44', '32-45', '33-46', '34-47', '35-48', 
                      '36-49', '37-50', '38-51', '39-52', '40-53', '41-54', 
                      '42-55', '43-56', '44-57', '45-58', '46-59', '47-60', 
                      '48-61', '49-62', '50-63', '51-64', '52-65', '53-66', 
                      '54-67', '55-68', '56-69', '57-70', '58-71', '59-72', 
                      '60-73', '61-74', '62-75', '63-76', '64-77', '65-78', 
                      '66-79', '67-80', '68-11'], 
            'used':  [], 
            'set': [], 
            } )
        # This is a Step initiated by the Start method, when the first 12 cards from
        # the cardset contain a valid set of 3 cards
        Dict.append( {'__class__': 'SetStep', 'turnCounter': '0',
            'playerID': 'None', 'nickname': '', 
            'table': ['00-00', '01-01', '02-02', '03-03', '04-04', '05-05', 
                      '06-06', '07-07', '08-08', '09-09', '10-10', '11-11'],
            'pick':  ['00-12', '01-13', '02-14', '03-15', '04-16', '05-17', 
                      '06-18', '07-19', '08-20', '09-21', '10-22', '11-23', 
                      '12-24', '13-25', '14-26', '15-27', '16-28', '17-29', 
                      '18-30', '19-31', '20-32', '21-33', '22-34', '23-35', 
                      '24-36', '25-37', '26-38', '27-39', '28-40', '29-41', 
                      '30-42', '31-43', '32-44', '33-45', '34-46', '35-47', 
                      '36-48', '37-49', '38-50', '39-51', '40-52', '41-53', 
                      '42-54', '43-55', '44-56', '45-57', '46-58', '47-59', 
                      '48-60', '49-61', '50-62', '51-63', '52-64', '53-65', 
                      '54-66', '55-67', '56-68', '57-69', '58-70', '59-71', 
                      '60-72', '61-73', '62-74', '63-75', '64-76', '65-77', 
                      '66-78', '67-79', '68-80'],
            'used':  [],
            'set': [],
            } )
        # The third Step is the same as the second one.
        Dict.append( {'__class__': 'SetStep', 'turnCounter': '0',
            'playerID': 'None', 'nickname': '', 
            'table': ['00-00', '01-01', '02-02', '03-03', '04-04', '05-05', 
                      '06-06', '07-07', '08-08', '09-09', '10-10', '11-11'],
            'pick':  ['00-12', '01-13', '02-14', '03-15', '04-16', '05-17', 
                      '06-18', '07-19', '08-20', '09-21', '10-22', '11-23', 
                      '12-24', '13-25', '14-26', '15-27', '16-28', '17-29', 
                      '18-30', '19-31', '20-32', '21-33', '22-34', '23-35', 
                      '24-36', '25-37', '26-38', '27-39', '28-40', '29-41', 
                      '30-42', '31-43', '32-44', '33-45', '34-46', '35-47', 
                      '36-48', '37-49', '38-50', '39-51', '40-52', '41-53', 
                      '42-54', '43-55', '44-56', '45-57', '46-58', '47-59', 
                      '48-60', '49-61', '50-62', '51-63', '52-64', '53-65', 
                      '54-66', '55-67', '56-68', '57-69', '58-70', '59-71', 
                      '60-72', '61-73', '62-74', '63-75', '64-76', '65-77', 
                      '66-78', '67-79', '68-80'],
            'used':  [],
            'set': [],
            } )
        return Dict

    def refStepStarts(self):
        Dict = self.refStepStarts_Dict()
        steps_ref = []
        steps_ref.append(Step())
        steps_ref.append(Step())
        steps_ref.append(Step())
        # populate the three Steps, knowing that :
        #    - generic details are already filled in (from the __init__)
        #    - 'used' and 'set' remain empty lists
        for code in Dict[0]['table']:
            steps_ref[0].table.append(int(code[3:]))
        for code in Dict[0]['pick']:
            steps_ref[0].pick.append(int(code[3:]))
        for code in Dict[1]['table']:
            steps_ref[1].table.append(int(code[3:]))
        for code in Dict[1]['pick']:
            steps_ref[1].pick.append(int(code[3:]))
        for code in Dict[2]['table']:
            steps_ref[2].table.append(int(code[3:]))
        for code in Dict[2]['pick']:
            steps_ref[2].pick.append(int(code[3:]))
        return steps_ref

    def refStepSecond_Dict(self):
        """
        List of 2 reference Step dictionaries, generated by the Step.fromPrevious 
        method, out of the reference stepStart:
        Cardset 1 + stepStart 1 + set proposed [ 1,  6, 11] => stepSecond 1
        CardSet 2 + stepStart 2 + set proposed [ 0,  3,  9] => stepSecond 2
        This function will only provide with the SECOND iteration of a Step, 
         
        NB:These test data are complementary to the 'refStep_dict' and 'refSteps'
        available from 'test_utilities' and specific to the testing of the
        'Step' class.
        """
        Dict_steps = []
        # This is a step generated by 'fromPrevious' on Cardset 1 and stepStart 1
        Dict_steps.append({'__class__': 'SetStep', 'turnCounter': '1',
            'playerID': 'None', 'nickname': '',
            'table': ['00-00', '01-15', '02-02', '03-03', '04-04', '05-05', 
                      '06-14', '07-07', '08-08', '09-09', '10-10', '11-13'], 
            'pick':  ['00-16', '01-17', '02-18', '03-19', '04-20', '05-21', 
                      '06-22', '07-23', '08-24', '09-25', '10-26', '11-27', 
                      '12-28', '13-29', '14-30', '15-31', '16-32', '17-33', 
                      '18-34', '19-35', '20-36', '21-37', '22-38', '23-39', 
                      '24-40', '25-41', '26-42', '27-43', '28-44', '29-45', 
                      '30-46', '31-47', '32-48', '33-49', '34-50', '35-51', 
                      '36-52', '37-53', '38-54', '39-55', '40-56', '41-57', 
                      '42-58', '43-59', '44-60', '45-61', '46-62', '47-63', 
                      '48-64', '49-65', '50-66', '51-67', '52-68', '53-69', 
                      '54-70', '55-71', '56-72', '57-73', '58-74', '59-75', 
                      '60-76', '61-77', '62-78', '63-79', '64-80', '65-11'], 
            'used':  ['00-01', '01-06', '02-12'], 
            'set':   []
            } )
        # This is a step generated by 'fromPrevious' on Cardset 2 and stepStart 2
        Dict_steps.append({'__class__': 'SetStep', 'turnCounter': '1', 
            'playerID': 'None', 'nickname': '',
            'table': ['00-14', '01-01', '02-02', '03-13', '04-04', '05-05', 
                      '06-06', '07-07', '08-08', '09-12', '10-10', '11-11'], 
            'pick':  ['00-15', '01-16', '02-17', '03-18', '04-19', '05-20', 
                      '06-21', '07-22', '08-23', '09-24', '10-25', '11-26', 
                      '12-27', '13-28', '14-29', '15-30', '16-31', '17-32', 
                      '18-33', '19-34', '20-35', '21-36', '22-37', '23-38', 
                      '24-39', '25-40', '26-41', '27-42', '28-43', '29-44', 
                      '30-45', '31-46', '32-47', '33-48', '34-49', '35-50', 
                      '36-51', '37-52', '38-53', '39-54', '40-55', '41-56', 
                      '42-57', '43-58', '44-59', '45-60', '46-61', '47-62', 
                      '48-63', '49-64', '50-65', '51-66', '52-67', '53-68', 
                      '54-69', '55-70', '56-71', '57-72', '58-73', '59-74', 
                      '60-75', '61-76', '62-77', '63-78', '64-79', '65-80'], 
            'used':  ['00-00', '01-03', '02-09'], 
            'set':   []
            } )
        return Dict_steps

    def refStepSecond(self):
        Dict_steps = self.refStepSecond_Dict()
        stepSeconds_ref = []
        stepSeconds_ref.append(Step())
        stepSeconds_ref.append(Step())
        # populate the two second Steps from teh dictionaries above.
        stepDict_to_Step(Dict_steps[0], stepSeconds_ref[0])
        stepDict_to_Step(Dict_steps[1], stepSeconds_ref[1])
        return stepSeconds_ref

    def setup(self):
        # generate reference test data with 3 couples (cardset + step)
        cardsets_ref = refCardsets()
        stepStarts_ref = self.refStepStarts()
        return [cardsets_ref, stepStarts_ref]

    def teardown(self):
        pass

    def test__init__(self):
        """
        Test Step.__init__
        """
        # setup the test data
        vbar()
        vprint("We build test data for testing the class Step")
        step_test = Step()
        # run the test
        vbar()
        print("Test Step.__init__")
        vbar()
        vprint("We build a new Step and check that all fields are empty.")
        self.assertEqual(step_test.turnCounter, 0)
        self.assertEqual(step_test.playerID, None)
        self.assertEqual(step_test.nickname, "")
        self.assertEqual(step_test.pick, [])
        self.assertEqual(step_test.table, [])
        self.assertEqual(step_test.used, [])
        self.assertEqual(step_test.set, [])

    def test_start(self):
        """
        Test Step.start
        """
        # setup the test data
        [cardsets_ref, stepStart_ref] = self.setup()
        # run the test
        vbar()
        print("Test Step.start")
        vbar()
        vprint("We build a new Step for each of the reference cardset, and we compare")
        vprint("with the reference targets which are:")
        stepStarts_test = []
        stepStarts_test.append(Step())
        stepStarts_test.append(Step())
        stepStarts_test[0].start(cardsets_ref[0])
        stepStarts_test[1].start(cardsets_ref[1])
        vprint("Cardset 0: the step should be equal to:")
        vprint(stepStart_ref[0].toString(cardsets_ref[0], "  "))
        self.assertTrue(step_equality(stepStart_ref[0], stepStarts_test[0]))
        vprint("Cardset 1: the step should be equal to:")
        vprint(stepStart_ref[1].toString(cardsets_ref[1], "  "))
        self.assertTrue(step_equality(stepStart_ref[1], stepStarts_test[1]))

    def test_validateSetFromTable(self):
        """
        Test Step.validateSetFromTable
        """
        # setup the test data
        [cardsets_ref, stepStart_ref] = self.setup()
        stepStartBis_ref = refSteps()
        # it reads the reference suite of couple (set / player) to be applied in 
        # order to use the reference data on Steps. 
        setandpl_ref = refSetsAndPlayers()
        # run the test
        vbar()
        print("Test Step.validateSetFromTable")
        vbar()
        vprint("We run the method on two reference steps, and it should return")
        vprint("known answers each time.")
        # basic test, no need for additional test data
        vprint("  > We will check few Sets on cardset 0 /step 0 to see if they are ")
        vprint("    validated or rejected, without populating the step:")
        result = stepStart_ref[0].validateSetFromTable(cardsets_ref[0], [0,1,2])
        self.assertFalse(result)
        vprint("        [ 0, 1, 2] should be False => " + str(result))
        result = stepStart_ref[0].validateSetFromTable(cardsets_ref[0], [9,10,11])
        self.assertFalse(result)
        vprint("        [ 9,10,11] should be False => " + str(result))
        result = stepStart_ref[0].validateSetFromTable(cardsets_ref[0], [1,6,11])
        self.assertTrue(result)
        vprint("        [ 1, 6,11] should be True  => " + str(result))
        # here we populate the 'reference Start' steps:
        #    => they become 'test StartBis' steps

        # First test with a invalid set of 3 cards:
        vprint("  > we will now propose valid sets with 'population' option activated,")
        vprint("    and compare the outcome (so called 'stepStartBis') with reference data")
        vprint("    - Cardset 0 / step 0 - set [0,1,2] - populating with 'Donald'")
        player = setandpl_ref[0][0]['player']
        result = stepStart_ref[1].validateSetFromTable(cardsets_ref[0], [0,1,2], True, player)
        self.assertFalse(result)
        self.assertEqual(stepStart_ref[0].playerID, None)
        self.assertEqual(stepStart_ref[0].nickname, "")
        self.assertEqual(stepStart_ref[0].set, [])
        vprint("       [ 0, 1, 2] should be False => " + str(result))
        vprint("       so we check it was not populated:")
        vprint("             playerID = " + str(stepStart_ref[0].playerID))
        vprint("             nickname = " + stepStart_ref[0].nickname)
        vprint("                  set = " + str(stepStart_ref[0].set))

        # second test with a valid set of 3 cards
        player = setandpl_ref[0][0]['player']
        good_set = setandpl_ref[0][0]['set']
        vprint("    - Cardset 0 / step 0 - set " + str(good_set)
               + " - populating with '" + str(player['nickname']) + "'")
        result = stepStart_ref[0].validateSetFromTable(cardsets_ref[0], good_set, True, player)
        self.assertTrue(result)
        self.assertTrue(step_equality(stepStart_ref[0], stepStartBis_ref[0][0]))
        vprint("        "+str(good_set)+" should be True  => " + str(result))
        vprint("        so we check it was populated")
        vprint("              playerID = " + str(stepStart_ref[0].playerID))
        vprint("              nickname = " + stepStart_ref[0].nickname)
        vprint("                   set = " + str(stepStart_ref[0].set))

        # test with the second set of reference test data
        player   = setandpl_ref[1][0]['player']
        good_set = setandpl_ref[1][0]['set']
        vprint("    - Cardset 1 / step 1 - set " + str(good_set)
               + " - populating with '" + str(player['nickname']) + "'")
        result = stepStart_ref[1].validateSetFromTable(cardsets_ref[1], good_set, True, player)
        self.assertTrue(result)
        self.assertTrue(step_equality(stepStart_ref[1], stepStartBis_ref[1][0]))
        vprint("        [ 0, 3, 9] should be True  => " + str(result))
        vprint("        so we check it was populated")
        vprint("              playerID = " + str(stepStart_ref[1].playerID))
        vprint("              nickname = " + stepStart_ref[1].nickname)
        vprint("                   set = " + str(stepStart_ref[1].set))

    def test_fromPrevious(self):
        """
        Test Step.fromPrevious
        """
        # setup the test data
        # BEWARE:
        # - there are 3 examples in the 'Starts' series, indexed 0, 1 and 2
        # - there are only two in the 'Seconds' series, indexed 0 and 1
        # => index 0 in the 'Starts' disappears in the 'Seconds'
        # => index 1 in the 'Starts' correspond to index 0 in the 'Seconds'
        # => index 2 in the 'Starts' correspond to index 1 in the 'Seconds'
        [cardsets_ref, stepStarts_ref] = self.setup()
        stepStartBis_ref = refSteps()
        stepSeconds_ref = self.refStepSecond()
        stepSeconds_test = []
        stepSeconds_test.append(Step())
        stepSeconds_test.append(Step())
        # run the test
        vbar()
        print("Test Step.fromPrevious")
        vbar()
        vprint("We run the 'fromPrevious' method on two test steps, using the 'startBis'")
        vprint("reference steps as a stable starting point, and we compare the result")
        vprint("with the reference 'stepSecond'.")
        vprint()
        vprint("    stepStart -> propose Set [1, 6,11] -> stepStartBis")
        vprint("    apply 'from previous' on stepStartBis  =  stepSecond")
        vprint()
        vprint("  > Cardset 0: the result should look like")
        vprint(stepSeconds_ref[0].toString(cardsets_ref[0], "    "))
        stepSeconds_test[0].fromPrevious(stepStartBis_ref[0][0], cardsets_ref[0])        
        self.assertTrue(step_equality(stepSeconds_ref[0], stepSeconds_test[0]))

        vprint("  > Cardset 1: the result should look like")
        vprint(stepSeconds_ref[1].toString(cardsets_ref[1], "    "))
        stepSeconds_test[1].fromPrevious(stepStartBis_ref[1][0], cardsets_ref[1])
        self.assertTrue(step_equality(stepSeconds_ref[1], stepSeconds_test[1]))

    def test_serialize(self):
        """
        Test Step.serialize
        """
        # setup the test data
        dictStart_ref = self.refStepStarts_Dict()
        [cardsets_ref, stepStarts_ref] = self.setup()
        dictStartBis_ref0 = refGames_Dict()[0]['steps'][0]
        dictStartBis_ref1 = refGames_Dict()[1]['steps'][0]
        stepStartBis_ref = refSteps()
        dictSecond_ref = self.refStepSecond_Dict()
        stepSeconds_ref = self.refStepSecond()
        # run the test
        vbar()
        print("Test Step.serialize")
        vbar()
        vprint("We compare the dictionaries produced with the serialize method")
        vprint("with reference dictionaries, and check the output is correct")
        # test with the first series of Steps
        vprint()
        step_test = stepStarts_ref[0]
        dict_test = step_test.serialize()
        vprint("  > Cardets 0 - Step 0 - stepStart:")
        vprint("       Target: " + str(dictStart_ref[0]))
        vprint("       Result: " + str(dict_test))
        self.assertTrue(stepDict_equality(dict_test, dictStart_ref[0]))
        step_test = stepStartBis_ref[0][0]
        dict_test = step_test.serialize()
        vprint("  > Cardets 0 - Step 0 - stepStartBis:")
        vprint("       Target: " + str(dictStartBis_ref0))
        vprint("       Result: " + str(dict_test))
        self.assertTrue(stepDict_equality(dict_test, dictStartBis_ref0))
        step_test = stepSeconds_ref[0]
        dict_test = step_test.serialize()
        vprint("  > Cardets 0 - Step 0 - stepSecond:")
        vprint("       Target: " + str(dictSecond_ref[0]))
        vprint("       Result: " + str(dict_test))
        self.assertTrue(stepDict_equality(dict_test, dictSecond_ref[0]))
        # test with the second series of Steps
        vprint()
        step_test = stepStarts_ref[1]
        dict_test = step_test.serialize()
        vprint("  > Cardets 1 - Step 1 - stepStart:")
        vprint("       Target: " + str(dictStart_ref[1]))
        vprint("       Result: " + str(dict_test))
        self.assertTrue(stepDict_equality(dict_test, dictStart_ref[1]))
        step_test = stepStartBis_ref[1][0]
        dict_test = step_test.serialize()
        vprint("  > Cardets 1 - Step 1 - stepStartBis:")
        vprint("       Target: " + str(dictStartBis_ref1))
        vprint("       Result: " + str(dict_test))
        self.assertTrue(stepDict_equality(dict_test, dictStartBis_ref1))
        step_test = stepSeconds_ref[1]
        dict_test = step_test.serialize()
        vprint("  > Cardets 1 - Step 1 - stepSecond:")
        vprint("       Target: " + str(dictSecond_ref[1]))
        vprint("       Result: " + str(dict_test))
        self.assertTrue(stepDict_equality(dict_test, dictSecond_ref[1]))

    def test_deserialize(self):
        """
        Test Step.deserialize
        """
        # setup the test data
        dictStart_ref = self.refStepStarts_Dict()
        [cardsets_ref, stepStarts_ref] = self.setup()
        dictStartBis_ref0 = refGames_Dict()[0]['steps'][0]
        dictStartBis_ref1 = refGames_Dict()[1]['steps'][0]
        stepStartBis_ref = refSteps()
        step_test = Step()
        # run the test
        vbar()
        print("Test Step.deserialize")
        vbar()
        vprint("We compare the steps produced with the deserialize method with")
        vprint("reference steps, and check the output is correct")
        # test with the first series of Steps
        vprint()
        step_test.deserialize(dictStart_ref[0])
        vprint("  > Cardets 0 - Step 0 - stepStart:")
        vprint("       Target: " + stepStarts_ref[0].toString(cardsets_ref[0], "     "))
        vprint("       Result: " + step_test.toString(cardsets_ref[0], "     "))
        self.assertTrue(step_equality(step_test, stepStarts_ref[0]))
        vprint()
        step_test.deserialize(dictStartBis_ref0)
        vprint("  > Cardets 0 - Step 0 - stepStartBis:")
        vprint("       Target: " + stepStartBis_ref[0][0].toString(cardsets_ref[0], "     "))
        vprint("       Result: " + step_test.toString(cardsets_ref[0], "     "))
        self.assertTrue(step_equality(step_test, stepStartBis_ref[0][0]))


if __name__ == '__main__':

    unittest.main()

