'''
Created on August 19th 2016
@author: Thierry Souche

This modules contains few constants and functions which are useful for other 
unit test modules.
'''



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

# Initialize the reference test data

def refCardsets():
    """
    This function returns a list of 3 CardSets which are test references:
        - Cardset 0: interesting because there is no valid set of 3 cards in the
            first 12 cards of the cardset. The Table must be build with the 13th
            card in the pick, and move the 12th card at the end of the Pick.
        - Cardset 1: ***  TO BE CONFIRMED *** jointly with the 'refSet 0' series, 
            will get to a final table with only 6 cards.
        - Cardset 2: show a non-randomized cardset, usefull for testing the 
            CardSet class.
    """
    
    # loads the test data into CardSets
    Dict = refGames_Dict()
    cardsets_ref = []
    cardsets_ref.append(CardSet())  # cardset 0
    cardsets_ref.append(CardSet())  # cardset 1
    cardsets_ref.append(CardSet())  # cardset init
    # overwrite the cardsets 0 and 1 with reference data read from refGamesDict
    for i in range(0,2):
        cc = cardsets_ref[i].cards
        for code in Dict[i]['cardset']['cards']:
            k = int(code[:2])
            c = int(code[3])
            s = int(code[4])
            f = int(code[5])
            n = int(code[6])
            cc[k] = [c,s,f,n]
    # overwrite the cardset init
    Dict = {'__class__': 'SetCardset', 
        'cards': ['00-0000', '01-0001', '02-0002', '03-0010', '04-0011', '05-0012', 
                  '06-0020', '07-0021', '08-0022', '09-0100', '10-0101', '11-0102', 
                  '12-0110', '13-0111', '14-0112', '15-0120', '16-0121', '17-0122', 
                  '18-0200', '19-0201', '20-0202', '21-0210', '22-0211', '23-0212', 
                  '24-0220', '25-0221', '26-0222', '27-1000', '28-1001', '29-1002', 
                  '30-1010', '31-1011', '32-1012', '33-1020', '34-1021', '35-1022', 
                  '36-1100', '37-1101', '38-1102', '39-1110', '40-1111', '41-1112', 
                  '42-1120', '43-1121', '44-1122', '45-1200', '46-1201', '47-1202', 
                  '48-1210', '49-1211', '50-1212', '51-1220', '52-1221', '53-1222', 
                  '54-2000', '55-2001', '56-2002', '57-2010', '58-2011', '59-2012', 
                  '60-2020', '61-2021', '62-2022', '63-2100', '64-2101', '65-2102', 
                  '66-2110', '67-2111', '68-2112', '69-2120', '70-2121', '71-2122', 
                  '72-2200', '73-2201', '74-2202', '75-2210', '76-2211', '77-2212', 
                  '78-2220', '79-2221', '80-2222']
        }
    cc = cardsets_ref[2].cards
    for code in Dict['cards']:
        k = int(code[:2])
        c = int(code[3])
        s = int(code[4])
        f = int(code[5])
        n = int(code[6])
        cc[k] = [c,s,f,n]
    # returns the 3 filled cardsets.
    return cardsets_ref


