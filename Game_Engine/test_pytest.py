import game_engine_v1
from game_engine_v1 import *

### --- Unit Testing of "Place" Class Constructor --- ###

# Unit Test # 1 -- Target: Place Constructor & Attribute "name"
def test_setPlaceName():
    game = Game(1,1)
    descriptions = ["day description", "night description"]
    place1 = Place (game, "Place 1", None, [None, None, None, None, None, None, None, None, None, None])

    assert(place1.name == "Place 1")


# Unit Test # 2 -- Target: Place Constructor & Attribute "description"
def test_setPlaceDescription():
    game = Game(1,1)
    descriptions = ["day description", "night description"]
    place1 = Place (game, None, "Place 1 description", descriptions, [None, None, None, None, None, None, None, None, None, None])

    assert(place1.description.get("day") == "day description")
    assert(place1.description.get("night") == "night description")


# Unit Test # 3 -- Target: Place Constructor & Attribute "adjacentPlaceNames[]"
def test_setPlaceAdjacentNames():
    game = Game(1,1)
    # descriptions = ["day description", "night description"]
    place1 = Place(game, None, None, ["x", None, None, None, None, None, None, None, None, None])

    assert(place1.adjacentPlaceNames[0] == "x")



### --- Unit Testing of User Class constructor --- ###

# Unit Test #4 -- Target: User Constructor & Attribute "name"
def test_setUserName():
    game = Game(1,1)
    user = User(game, "name", None, None, False)

    assert(user.name == "name")

# Unit Test #5 -- Target: User Constructor & Attribute "current_Place" (at start)
def test_setStartingPlace():
    game = Game(1,1)
    user = User(game, None, "Place 1", None, False)

    assert(user.current_place == game.getPlace("Place 1"))

# Unit Test #6 Target: User Constructor & Attribute "direction" (at start)
def test_setStartingDirection():
    game = Game(1,1)
    user = User(game, None, "Place 1", "n", False)
    game.setUser(user)

    assert(user.direction == game.user.getUserDirection())