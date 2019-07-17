# Manual Testing Game Engine Pick Up Object
# 
#
# 1 or 2 places created
# 2 objects that are pickupable, 1 object that is not
# 1 user
# 
# Scenario 1: pick up objects --> check that user has that object, and that room doesn't
# Scenario 2: pick up objects that are not in room --> error
# Scenario 3: pick up object you already have --> error
# Scenario 4: pick up object that is not pickupable --> error

import game_engine_v1
import action
from game_engine_v1 import *
from action import *

# Scenario 1: pick up objects --> check that user has that object
def runScenario1():

    print("\n Scenario 1: ")

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

    # put things in place1
    place1.addThing(thing1)
    place1.addThing(thing2)

    game.setIsValid()

    # create action object
    action = Action("take", None, "thing1")

    # print user
    print("\nUser pre-action attempt:")
    game.user.printUser(game)

    # print place
    print("Things in room pre-action: ")
    things = place1.things
    for t in things:
        print(t.name)

    # call game as though you are the parser
    game.fromParserToGame(action)

    # print user
    print("\nUser post-action attempt:")
    game.user.printUser(game)

    # check that room doesn't have object
    print("Things in room post-action: ")
    things = place1.things
    for t in things:
        print(t.name)

# Scenario 2: pick up objects that are not in room --> error
def runScenario2():

    print("\n Scenario 2: ")

    game = Game(1,1)
    descriptions = ["place during day", "place during night"]
    adjacent_rooms = [None, None, None, None, None, None, None, None, None, None]
    place1 = Place (game, "Place 1", descriptions, adjacent_rooms)
    place2 = Place (game, "Place 2", descriptions, adjacent_rooms)
    user = User(game, "user1", "Place 1", "n", False)
    place1.setAdjacentPlaces(game)
    place2.setAdjacentPlaces(game)
    game.setUser(user)

    # create thing1
    name = "thing1"
    description = name + " description"
    thing1 = Thing(name, description, place1, True)

    # create thing2, put in place2
    name = "thing2"
    description = name + " description"
    thing2 = Thing(name, description, place2, True)

    # put things in places
    place1.addThing(thing1)
    place2.addThing(thing2)

    game.setIsValid()

    # create action object
    action = Action("take", None, "thing2")

    # print user
    print("\nUser pre-action attempt:")
    game.user.printUser(game)

    # call game as though you are the parser, try to pick up thing2, which is in another room
    game.fromParserToGame(action)

    # print user
    print("\nUser post-action attempt:")
    game.user.printUser(game)

# Scenario 3: pick up object you already have --> error
def runScenario3():

    print("\n Scenario 3: ")

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

    # put things in place1
    place1.addThing(thing1)
    place1.addThing(thing2)

    game.setIsValid()

    # create action object
    action = Action("take", None, "thing1")

    # print user
    print("\nUser pre-action attempt:")
    game.user.printUser(game)

    # call game as though you are the parser
    game.fromParserToGame(action)
    # call game as though you are the parser # try to pick up object you already have
    game.fromParserToGame(action)

    # print user
    print("\nUser post-action attempt:")
    game.user.printUser(game)

# Scenario 4: pick up object that is not pickupable --> error
def runScenario4():

    print("\n Scenario 4: ")

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
    feature1 = Thing(name, description, place1, False)

    # put things in place1
    place1.addThing(thing1)
    place1.addThing(thing2)
    place1.addThing(feature1)

    game.setIsValid()

    # create action object
    action = Action("take", None, "feature1")

    # print user
    print("\nUser pre-action attempt:")
    game.user.printUser(game)

    # call game as though you are the parser
    game.fromParserToGame(action)

    # print user
    print("\nUser post-action attempt:")
    game.user.printUser(game)

def main():

    runScenario1()
    runScenario2()
    runScenario3()
    runScenario4()

main()