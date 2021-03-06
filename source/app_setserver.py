'''
Created on August 11th 2016
@author: Thierry Souche
'''

from bottle import Bottle, request, run
from bson.objectid import ObjectId

from app_shared import oidIsValid

from app_backend import Backend

"""
This script must be run in order to start the server. 
Unit test can be run with test_setserver.py, provided that the bottle server
will have been started with the command line:
    > cd /
    > python /data/code/setgame/server/setserver.py
"""

# version
setserver_version = 'v1.0.0'

# address of the web server (exposing the Setgame API)
setserver_address = 'localhost'
setserver_port = 8080

# routes which are declared in the web server

setserver_routes_list = {
        'default':                  '/',
        'hello':                    '/hello',
        'version':                  '/about',

        'nickname_available':       '/player/register/available/',
        'register_player':          '/player/register/nickname/',
        'get_player_details':       '/player/details/',

        'enlist_player':            '/player/enlist/',
        'enlist_team':              '/player/enlist_team',
        'deregister_player':        '/player/deregister/',
        'get_gameid':               '/player/gameid/',

        'get_turn':                 '/game/turncounter/',
        'get_game_finished':        '/game/gamefinished/',
        'get_nicknames':            '/game/nicknames/',
        'soft_stop':                '/game/stop/',
        'hard_stop':                '/game/hardstop/',
        'get_game_details':         '/game/details/',
        'get_step':                 '/game/step/',
        'get_history':              '/game/history/',
        'propose_set':              '/game/set/',

        'test_reset':               '/test/reset',
        'test_reg_ref_players':     '/test/register_ref_players',
        'test_enlist_ref_players':  '/test/enlist_ref_players',
        'test_delist_players':      '/test/delist_all_players',
        'test_load_ref_game':       '/test/load_ref_game',
        'test_back_to_turn':        '/test/back_to_turn/'
        }

# web server's related functions

def setserver_routes(verb, full=True):
    """
    This function returns the path 
    """
    if full:
        prefix = "http://" + setserver_address + ":" + str(setserver_port)
    else:
        prefix = ""
    result = prefix + '/' + setserver_routes_list[verb]
    return result

def server_banner():
    print()
    print("  #######################################################")
    print("  #                                                     #")
    print("  #                   Set Server                        #")
    print("  #                                                     #")
    print("  #######################################################")
    print("  #                                                     #")
    print("  #   Set game server - version {:<8}                #".format(setserver_version))
    print("  #                                                     #")
    print("  #   URL: {:<20}                         #".format(setserver_address))
    print("  #   Listening on port {:<6}                          #".format(setserver_port))
    print("  #                                                     #")
    print("  #######################################################")
    print()



if __name__ == "__main__":

    # initiate the server class
    backend = Backend()
    # initiate the web server
    webserver = Bottle()


    #
    # Generic routes
    #


    # this route is used for checking that the server is up
    @webserver.route(setserver_routes('default', False))
    @webserver.route(setserver_routes('hello', False))
    def hello():
        return "<p>Hello. The Set game server is active.</p>"

    # this route is used to get the server version
    @webserver.route(setserver_routes('version', False))
    def version():
        return "<p>Set server version "+server_version+"</p>"

    #
    # Routes related to managing users (= players)
    #


    # this route enable to check if a nickname is still available to register a 
    # new player to the server
    @webserver.route(setserver_routes('nickname_available', False) + "<nickname>")
    def isNicknameAvailable(nickname):
        return backend.isNicknameAvailable(nickname)

    # this route enable to register players to the Set game server
    @webserver.route(setserver_routes('register_player', False) + "<nickname>")
    def registerPlayer(nickname):
        passwordHash = request.query.get('passwordHash')
        return backend.registerPlayer(nickname, passwordHash)

    # this route enable to return the login details of a player from its nickname
    @webserver.route(setserver_routes('get_player_details', False) + "<nickname>")
    def getPlayerLoginDetails(nickname):
        return backend.getPlayerLoginDetails(nickname)


    #
    # Routes related to the enrolment of players to a game
    #


    # this route enable enlist one single player to a yet-to-start game
    @webserver.route(setserver_routes('enlist_player', False) + "<playerid_str>")
    def enlistPlayer(playerid_str):
        # check that the string passed is a valid ObjectId, and if so
        # call the backend.
        if oidIsValid(playerid_str):
            result = backend.enlistPlayer(ObjectId(playerid_str))
            if result['status'] == "ok":
                gameid_str = str(result['gameID'])
                result = {'status': "ok", 'gameID': gameid_str}
        else:
            result = {'status': "ko"}
        return result

    # this route enable to register a constituted team and start a game
    @webserver.route(setserver_routes('enlist_team', False))
    def enlistTeam():
        pid_list = []
        result = request.query.getall('playerIDlist')
        # check that the strings passed are valid ObjectId, and if so
        # add them into the list of players to be enlisted.
        for playerid_str in result:
            if oidIsValid(playerid_str):
                    pid_list.append({'playerID': ObjectId(playerid_str)})
        result2 = backend.enlistTeam(pid_list)
        if result2['status'] == "ok":
            gameid_str = str(result2['gameID'])
            result2 = {'status': "ok", 'gameID': gameid_str}
        return result2

    # this route enable to de-register a single player to a yet-to-start game
    @webserver.route(setserver_routes('deregister_player', False) + "<playerid_str>")
    def deRegisterPlayer(playerid_str):
        if oidIsValid(playerid_str):
            result = backend.deRegisterPlayer(ObjectId(playerid_str))
        else:
            result = {'status': "ko", 'reason': "invalid playerID"}
        return result

    # this route enable to return the gameID of a player from its playerID
    @webserver.route(setserver_routes('get_gameid', False) + "<playerid_str>")
    def getGameID(playerid_str):
            if oidIsValid(playerid_str):
                result = backend.getGameID(ObjectId(playerid_str))
                if result['status'] == "ok":
                    result['gameID'] = str(result['gameID'])
            else:
                result = {'status': "ko", 'reason': "invalid playerID"}
            return result

    #
    # Routes related to playing a game (once properly registered)
    #


    # this route enable to collect the turnCounter
    @webserver.route(setserver_routes('get_turn', False) + "<gameid_str>")
    def getTurnCounter(gameid_str):
        # check that the string passed is a valid ObjectId, and if so
        # call the backend.
        if oidIsValid(gameid_str):
            gameID = ObjectId(gameid_str)
            answer = backend.getTurnCounter(gameID)
            if answer['status'] == "ok":
                result = {
                    'status': "ok", 
                    'turnCounter': str(answer['turnCounter'])
                    }
            else:
                result = answer
        else:
            result = {'status': "ko", 'reason': "invalid gameID"}
        return result

    # this route enable to check if the game is finished
    @webserver.route(setserver_routes('get_game_finished', False) + "<gameid_str>")
    def getGameFinished(gameid_str):
        # check that the string passed is a valid ObjectId, and if so
        # call the backend.
        if oidIsValid(gameid_str):
            gameID = ObjectId(gameid_str)
            answer = backend.getGameFinished(gameID)
            if answer['status'] == "ok":
                result = {
                    'status': "ok", 
                    'gameFinished': str(answer['gameFinished'])
                    }
            else:
                result = answer
        else:
            result = {'status': "ko", 'reason': "invalid gameID"}
        return result

    # this route enable to collect the nicknames of the team-mates
    @webserver.route(setserver_routes('get_nicknames', False) + "<playerid_str>")
    def getNicknames(playerid_str):
        # check that the string passed is a valid ObjectId, and if so
        # call the backend.
        if oidIsValid(playerid_str):
            playerID = ObjectId(playerid_str)
            result = {'status': "ok", 'nicknames': backend.getNicknames(playerID)}
        else:
            result = {'status': "ko"}
        return result

    # this route enable to soft-stop a game
    @webserver.route(setserver_routes('soft_stop', False) + "<gameid_str>")
    def stopGame(gameid_str):
        # it needs (amongst other things) to read the 'hard' flag.
        if oidIsValid(gameid_str):
            gameID = ObjectId(gameid_str)
            result = backend.stopGame(gameID)
        else:
            result = {'status': "ko", 'reason': "invalid gameID"}
        return result

    # this route enable to hard-stop a game
    @webserver.route(setserver_routes('hard_stop', False) + "<gameid_str>")
    def stopGame(gameid_str):
        # it needs (amongst other things) to read the 'hard' flag.
        if oidIsValid(gameid_str):
            result = backend.stopGame(ObjectId(gameid_str), True)
        else:
            result = {'status': "ko", 'reason': "invalid gameID"}
        return result

    # this route enable to collect the generic details of a game 
    @webserver.route(setserver_routes('get_game_details', False) + "<gameid_str>")
    def getGameDetails(gameid_str):
        if oidIsValid(gameid_str):
            result = backend.getDetails(ObjectId(gameid_str))
        else:
            result = {'status': "ko", 'reason': "invalid gameID"}
        return result

    # this route enable to collect the current step
    @webserver.route(setserver_routes('get_step', False) + "<gameid_str>")
    def getStep(gameid_str):
        if oidIsValid(gameid_str):
            result = backend.getStep(ObjectId(gameid_str))
        else:
            result = {'status': "ko", 'reason': "invalid gameID"}
        return result

    # this route enable to collect the full history of the game
    @webserver.route(setserver_routes('get_history', False) + "<gameid_str>")
    def getHistory(gameid_str):
        if oidIsValid(gameid_str):
            result = backend.getHistory(ObjectId(gameid_str))
        else:
            result = {'status': "ko", 'reason': "invalid gameID"}
        return result

    # this route enable a client to propose a set of 3 cards to the server
    @webserver.route(setserver_routes('propose_set', False) + "<playerid_str>")
    def proposeSet(playerid_str):
        if oidIsValid(playerid_str):
            playerID = ObjectId(playerid_str)
            set_dict = request.query.getall('set')
            set_list = []
            for s in set_dict:
                try:
                    set_list.append(int(s))
                except:
                    result = {'status': "ko", 'reason': "invalid set"}
            result = backend.proposeSet(playerID, set_list)
        else:
            result = {'status': "ko", 'reason': "invalid playerID"}
        return result


    #
    # Test related routes
    #

    # this route is used to reset the server and run automated tests with a clean
    # starting status.
    @webserver.route(setserver_routes('test_reset', False))
    def reset():
        return backend.reset()
    
    # this route enable test cases (register reference test players)
    @webserver.route(setserver_routes('test_reg_ref_players', False))
    def ForTestOnly_RegisterRefPlayers():
        # registers the 6 reference test players.
        return backend.ForTestOnly_RegisterRefPlayers()

    # this route enable test cases (enlist reference test players)
    @webserver.route(setserver_routes('test_enlist_ref_players', False))
    def ForTestOnly_EnlistRefPlayers():
        # registers the 6 reference test players.
        result = backend.ForTestOnly_EnlistRefPlayers()
        if result['status'] == "ok":
            result['gameID'] = str(result['gameID'])
        return result
    
    # this route enable test cases (delist all players)
    @webserver.route(setserver_routes('test_delist_players', False))
    def ForTestOnly_DelistAllPlayers():
        # registers the 6 reference test players.
        result = backend.ForTestOnly_DelistAllPlayers()
        return {'status': "ok", 'number_delisted': result}

    # this route enable to load and play to its end a reference test game
    @webserver.route(setserver_routes('test_load_ref_game', False))
    def ForTestOnly_LoadRefGame():
        # load the reference test game indicated by 'test_data_index'
        index = request.query.get('test_data_index')
        try:
            test_data_index = int(index)
            if test_data_index in (0,1):
                result = backend.ForTestOnly_LoadRefGame(test_data_index)
                if result['status'] == "ok":
                    gid_str = str(result['gameID'])
                    result = {'status': "ok", 'gameID': gid_str}
            else:
                result = {'status': "ko", 'reason': "wrong index value"}
        except:
            result = {'status': "ko", 'reason': "invalid index"}
        return result

    # this route enable to roll back a reference test game
    @webserver.route(setserver_routes('test_back_to_turn', False) + "<index>/<turn>")
    def ForTestOnly_BackToTurn(index, turn):
        # assuming a reference game was properly loaded, it enable to roll back 
        # the finished game and get back to a given turn.
        try:
            index = int(index)
        except:
            return {'status': "ko", 'reason': "invalid index arguments"} 
        try:
            turn = int(turn)
        except:
            return {'status': "ko", 'reason': "invalid turn arguments"}
        return backend.ForTestOnly_GetBackToTurn(int(index), int(turn))





    # Now that all routes where mapped to a function, start the server
    
    server_banner()
    run(webserver, host=setserver_address, port=setserver_port, 
        reloader=True, debug=True)
