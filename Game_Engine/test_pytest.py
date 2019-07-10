import game_engine_v1
from game_engine_v1 import *

### --- Unit Testing of "Room" Class Constructor --- ###

# Unit Test # 1 -- Target: Room Constructor & Attribute "name"
def test_setRoomName():
    game = Game()
    room1 = Room (game, "Room 1", None, [None, None, None, None, None, None, None, None])

    assert(room1.name == "Room 1")


# Unit Test # 2 -- Target: Room Constructor & Attribute "description"
def test_setRoomDescription():
    game = Game()
    room1 = Room (game, None, "Room 1 description", [None, None, None, None, None, None, None, None])

    assert(room1.description == "Room 1 description")


# Unit Test # 3 -- Target: Room Constructor & Attribute "adjacentRoomNames[]"
def test_setRoomAdjacentNames():
    game = Game()
    room1 = Room(game, None, None, ["x", None, None, None, None, None, None, None])

    assert(room1.adjacentRoomNames[0] == "x")



### --- Unit Testing of User Class constructor --- ###

# Unit Test #4 -- Target: User Constructor & Attribute "name"
def test_setUserName():
    game = Game()
    user = User(game, "name", None, False)

    assert(user.name == "name")

# Unit Test #5 -- Target: User Constructor & Attribute "current_room" (at start)
def test_setStartingRoom():
    game = Game()
    user = User(game, None, "Room 1", False)

    assert(user.current_room == game.getRoom("Room 1"))

# Unit Test # 6
