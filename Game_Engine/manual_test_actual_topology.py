# Manual Testing Game Engine with Actual 3D Topology (Week 3)

import game_engine_v1
import action
from game_engine_v1 import *
from action import *

def runActualTopology():

    game = Game(1,1)

    descriptions = ["place during day", "place during night"]

    # connections to the northeast and west 
    place1 = Place(game, "Train Platform", descriptions, [None, "Fields", None, None, None, None, "Station-House", None, None, None])

    # connection to the east
    place2 = Place(game, "Station-House", descriptions, [None, None, "Train Platform", None, None, None, None, None, None, None])

    # connections to the north and southwest
    place3 = Place(game, "Fields", descriptions, ["Front Manor Grounds", None, None, None, None, "Train Platform", None, None, None, None])

    # connections to the north, south, and northwest 
    place4 = Place(game, "Front Manor Grounds", descriptions, ["Foyer", None, None, None, "Fields", None, None, "Ash Grove", None, None])

    # connections to the north, south, west, and up 
    place5 = Place(game, "Foyer", descriptions, ["Downstairs Hallway 1", None, None, None, "Front Manor Grounds", None, "Cloakroom", None, "Upstairs Hallway 1", None])

    # connections to the north, west, and down 
    place6 = Place(game, "Upstairs Hallway 1", descriptions, ["Upstairs Hallway 2", None, None, None, None, None, "Spare Room", None, None, "Foyer"])

    # connections to the north, east, south, and west 
    place7 = Place(game, "Upstairs Hallway 2", descriptions, ["Upstairs Hallway 3", None, "Small Lavatory", None, "Upstairs Hallway 1", None, "Bedroom", None, None, None])

    # connections to the north, east, and south
    place8 = Place(game, "Upstairs Hallway 3", descriptions, ["Upstairs Hallway 4", None, "Library", None, "Upstairs Hallway 2", None, None, None, None, None])

    # connections to the north, east, south, and west
    place9 = Place(game, "Upstairs Hallway 4", descriptions, ["Upstairs Hallway 5", None, "Study", None, "Upstairs Hallway 3", None, "Large Bedroom", None, None, None])

    # connections to the north and south
    place10 = Place(game, "Upstairs Hallway 5", descriptions, ["Servants\' Stair Top", None, None, None, "Upstairs Hallway 4", None, None, None, None, None])

    # connection to the east
    place11 = Place(game, "Spare Room", descriptions, [None, None, "Upstairs Hallway 1", None, None, None, None, None, None, None])  

    # connection to the west
    place12 = Place(game, "Small Lavatory", descriptions, [None, None, None, None, None, None, "Upstairs Hallway 2", None, None, None])

    # connection to the east
    place13 = Place(game, "Bedroom", descriptions, [None, None, "Upstairs Hallway 2", None, None, None, None, None, None, None]) 

    # connection to the west
    place14 = Place(game, "Library", descriptions, [None, None, None, None, None, None, "Upstairs Hallway 3", None, None, None])

    # connection to the west
    place15 = Place(game, "Study", descriptions, [None, None, None, None, None, None, "Upstairs Hallway 4", None, None, None])

    # connection to the east
    place16 = Place(game, "Large Bedroom", descriptions, [None, None, "Upstairs Hallway 4", None, None, None, None, None, None, None])

    # connections to the south and down
    place17 = Place(game, "Servants\' Stair Top", descriptions, [None, None, None, None, "Upstairs Hallway 5", None, None, None, None, "Servants\' Stair Bottom"])

    # connections to the south and up
    place18 = Place(game, "Servants\' Stair Bottom", descriptions, [None, None, None, None, "Downstairs Hallway 3", None, None, None, "Servants\' Stair Top", None])    

    # connections to the north and south
    place19 = Place(game, "Downstairs Hallway 3", descriptions, ["Servants\' Stair Bottom", None, None, None, "Downstairs Hallway 2", None, None, None, None, None])

    # connections to the north, east, south, and west
    place20 = Place(game, "Downstairs Hallway 2", descriptions, ["Downstairs Hallway 3", None, "Kitchen", None, "Downstairs Hallway 1", None, "Servants\' Quarters", None, None, None])

    # connections to the north, east, south, and west
    place21 = Place(game, "Downstairs Hallway 1", descriptions, ["Downstairs Hallway 2", None, "Dining Room", None, "Foyer", None, "Drawing Room", None, None, None])

    # connection to the west
    place22 = Place(game, "Kitchen", descriptions, [None, None, None, None, None, None, "Downstairs Hallway 2", None, None, None])

    # connection to the east
    place23 = Place(game, "Servants\' Quarters", descriptions, [None, None, "Downstairs Hallway 2", None, None, None, None, None, None, None])

    # connection to the east
    place24 = Place(game, "Drawing Room", descriptions, [None, None, "Downstairs Hallway 1", None, None, None, None, None, None, None])

    # connection to the west
    place25 = Place(game, "Dining Room", descriptions, [None, None, None, None, None, None, "Downstairs Hallway 1", None, None, None])

    # connection to the east
    place26 = Place(game, "Cloakroom", descriptions, [None, None, "Foyer", None, None, None, None, None, None, None])

    # connections to the north and southeast 
    place27 = Place(game, "Ash Grove", descriptions, ["Rear Manor Grounds", None, None, "Front Manor Grounds", None, None, None, None, None, None]) 

    # connections to the south and east
    place28 = Place(game, "Rear Manor Grounds", descriptions, [None, None, "Root Cellar", None, "Ash Grove", None, None, None, None, None]) 

    # connection to the west
    place29 = Place(game, "Root Cellar", descriptions, [None, None, None, None, None, None, "Rear Manor Grounds", None, None, None])

    user = User(game, "user1", "Train Platform", "n", False) # starting the user facing north

    place1.setAdjacentPlaces(game)
    place2.setAdjacentPlaces(game)
    place3.setAdjacentPlaces(game)
    place4.setAdjacentPlaces(game)
    place5.setAdjacentPlaces(game)
    place6.setAdjacentPlaces(game)
    place7.setAdjacentPlaces(game)
    place8.setAdjacentPlaces(game)
    place9.setAdjacentPlaces(game)
    place10.setAdjacentPlaces(game)
    place11.setAdjacentPlaces(game)
    place12.setAdjacentPlaces(game)
    place13.setAdjacentPlaces(game)
    place14.setAdjacentPlaces(game)
    place15.setAdjacentPlaces(game)
    place16.setAdjacentPlaces(game)
    place17.setAdjacentPlaces(game)
    place18.setAdjacentPlaces(game)
    place19.setAdjacentPlaces(game) 
    place20.setAdjacentPlaces(game)
    place21.setAdjacentPlaces(game)
    place22.setAdjacentPlaces(game)
    place23.setAdjacentPlaces(game)
    place24.setAdjacentPlaces(game)
    place25.setAdjacentPlaces(game)
    place26.setAdjacentPlaces(game)
    place27.setAdjacentPlaces(game)
    place28.setAdjacentPlaces(game)
    place29.setAdjacentPlaces(game)

    game.setUser(user)
    return game


def main():

    game = runActualTopology()
    game.setIsValid()

    action1 = Action()
    action1.setVerb("move_user")

    print("Actual Topology\n")
    print("Testing valid moves...\n")

    # test valid moves (not taking locked doors into account yet) 
    # start at place1 Train Platform and encounter all places, ending back at place1 
    validPath1 = ["w", "e", "ne", "n", "n", "up", "w", "e", "n", "w", "e", "e", "w", "n", "e", "w", "n", "e", "w", "w", "e", "n", "n", "down", "s", "s", "e", "w", "w", "e", "s", "e", "w", "w", "e", "s", "w", "e", "s", "nw", "n", "e", "w", "s", "se", "s", "sw", "ne", "n", "n", "n", "e", "w", "w", "e", "n", "e", "w", "w", "e", "n", "n", "up", "s", "s", "w", "e", "e", "w", "s", "e", "w", "s", "e", "w", "w", "e", "s", "w", "e", "down", "s", "s", "sw"]
       
    for m in validPath1:
        game.user.printUser(game)
        action1.setDirection(m)
        print()
        game.fromParserToGame(action1)


    print("\n")
    print("Testing invalid moves...\n")

    # test invalid moves

    # illegal moves from place1
    invalid1 = ["e", "s", "n", "sw", "se", "nw", "up", "down"]

    # testing bad moves from place1 
    for m in invalid1:
        game.user.printUser(game)
        action1.setDirection(m)
        print()
        game.fromParserToGame(action1)


main() 
