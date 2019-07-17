# Manual Testing Game Engine Pick Up Object
# 
#
# 1 place created
# 2 objects that are pickupable, 1 object that is not
# 1 user
# 
# Scenario 1: pick up objects --> check that user has that object
# Scenario 2: pick up objects that are not in room --> error
# Scenario 3: pick up object you already have --> error
# Scenario 4: pick up object that is not pickupable --> error
import game_engine_v1
import action
from game_engine_v1 import *
from action import *

def runScenario1():

    game = Game(1,1)
    descriptions = ["place during day", "place during night"]
    adjacent_rooms = [None, None, None, None, None, None, None, None, None, None]
    place1 = Place (game, "Place 1", descriptions, adjacent_rooms)
    user = User(game, "user1", "Place 1", "n", False)
    place1.setAdjacentPlaces(game)
    game.setUser(user)

    # create thing1
    name = "thing1"
    description = name + " description"
    thing1 = Thing(name, description, place1, True)

    # create thing2
    name = "thing2"
    description = name + " description"
    thing2 = Thing(name, description, place1, True)

    # create feature1
    name = "feature1"
    description = name + " description"
    feature1 = Thing(name, description, place1, True)

    # put things in place1
    place1.addThing(thing1)
    place1.addThing(thing2)
    place1.addThing(feature1)

    game.setIsValid()

    # create action object
    action = Action("take", None, "thing1")

    # print user
    game.user.printUser(game)

    # call game as though you are the parser
    game.fromParserToGame(action)

    # print user
    game.user.printUser(game)


def main():

    runScenario1()

main()