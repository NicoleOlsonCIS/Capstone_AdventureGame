# Manual Testing Game Engine Drop Object
# 
#
# 1 - 2 places created
# 2 objects that are pickupable
# 1 user
# 
# Scenario 1: drop object when you don't have any objects --> error
#
# Scenario 2: pick up multiple objects, drop single object (in same room). 
#       --> verify that object gets back in room and user doesn't have it
#
# Scenario 3: pick up object, move rooms, drop in different room 
#       --> verify that object gets put in different room and user doens't have it
#

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

    # put things in place1
    place1.addThing(thing1)

    game.setIsValid()

    # create action object
    action = Action("drop", None, "thing1")

    # print user
    print("\nUser pre-action attempt:")
    game.user.printUser(game)

    # call game as though you are the parser
    game.fromParserToGame(action)

    # print user
    print("\nUser post-action attempt:")
    game.user.printUser(game)

def runScenario2():
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

    # create action object to pick up an object
    action = Action("take", None, "thing1")

    # print user
    print("\nUser pre-take:")
    game.user.printUser(game)

    # call game as though you are the parser
    game.fromParserToGame(action)

    # print user
    print("\nUser post-take:")
    game.user.printUser(game)

    game.setIsValid()

    # create action object
    action2 = Action("drop", None, "thing1")

    # print user
    print("\nUser pre-drop attempt:")
    game.user.printUser(game)

    # print room
    print("\nPlace pre-drop attempt:")
    things = place1.things
    for t in things:
        print(t.name)

    # call game as though you are the parser
    game.fromParserToGame(action2)

    # print user
    print("\nUser post-drop thing 1 attempt:")
    game.user.printUser(game)

    # print room to show object is in room
    print("\nPlace post-drop attempt:")
    things = place1.things
    for t in things:
        print(t.name)

def runScenario3():
    game = Game(1,1)
    descriptions = ["place during day", "place during night"]
    adjacent_rooms = ["Place 2", None, None, None, None, None, None, None, None, None]
    place1 = Place (game, "Place 1", descriptions, adjacent_rooms)
    adjacent_rooms = [None, None, None, None, "Place1 ", None, None, None, None, None]
    place2 = Place (game, "Place 2", descriptions, adjacent_rooms)

    user = User(game, "user1", "Place 1", "n", False)

    place1.setAdjacentPlaces(game)
    place2.setAdjacentPlaces(game)

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

    # create action object to pick up an object
    action = Action("take", None, "thing1")

    # print user
    print("\nUser pre-take:")
    game.user.printUser(game)

    # call game as though you are the parser
    game.fromParserToGame(action)

    # print user
    print("\nUser post-take:")
    game.user.printUser(game)

    game.setIsValid()

    # now move the user north
    # create action object
    action2 = Action("move_user", "n", None)

    # print user
    print("\nUser pre-move")
    game.user.printUser(game)

    # call game as though you are the parser
    game.fromParserToGame(action2)

    # print user
    print("\nUser post-move:")
    game.user.printUser(game)

    # print room to show now objects in Place 2
    print("\n Objects in user new room:")
    things = place2.things
    for t in things:
        print(t.name)

    game.setIsValid()

    # create action object for dropping
    action3 = Action("drop", None, "thing1")

    # print user
    print("\nUser pre-drop")
    game.user.printUser(game)

    # call game as though you are the parser
    game.fromParserToGame(action3)

    # print user
    print("\nUser post-drop:")
    game.user.printUser(game)

    # print room to show now objects in Place 2
    print("\n Objects in place 2 post drop:")
    things = place2.things
    for t in things:
        print(t.name)

def main():

    runScenario1()
    runScenario2()
    runScenario3()

main()