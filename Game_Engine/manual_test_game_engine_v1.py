# Manual Testing Game Engine Unit of Capstone Adventure Game Version 1 (Week 3)
# 
# 4 Places created (objects) 
# 1 user created (object)
#
# Place topology # 1:
#    ____         ____
#   |r1  |       |r2  |
#   |    |-------|    |
#   |____|       |____|
#      |           |
#      |           |
#    __|_         _|__
#   |r4  |       |r3  |
#   |    |-------|    |
#   |____|       |____|
#
#
#
# Place topology # 2: (diagonal entrances/exits)
#  ____          ____
# |r1  |        |r4  |
# |    |--------|    |
# |____|        |____|
#       \      /
#        \____/           ____
#        |r2  |          |r3  |
#        |    |----------|    |
#        |____|          |____|
#
#

import game_engine_v1
import action
from game_engine_v1 import *
from action import *

def runTopologyOne():
	
	game = Game(1,1)

	descriptions = ["place during day", "place during night"]
	
	# has doors to the east and south
	place1 = Place (game, "Place 1", descriptions, [None,  None, "Place 2", None, "Place 3", None, None, None, None, None])
	
	# has doors to the west and south
	place2 = Place(game, "Place 2", descriptions, [None, None, None, None, "Place 4",  None, "Place 1", None, None, None])

	# has doors to the north and west
	place3 = Place(game, "Place 3", descriptions, ["Place 1", None, None, None, None, None, "Place 4", None, None, None])

	# has doors to the north and east
	place4 = Place(game, "Place 4", descriptions, ["Place 2", None, "Place 3", None, None, None, None, None, None, None])

	user = User(game, "user1", "Place 1", "n", False) # starting the user facing north

	place1.setAdjacentPlaces(game)
	place2.setAdjacentPlaces(game)
	place3.setAdjacentPlaces(game)
	place4.setAdjacentPlaces(game)

	game.setUser(user)
	return game

def runTopologyTwo():
	
	game = Game(1,1)
	descriptions = ["place during day", "place during night"]
	
	# has doors to the east and south-east
	place1 = Place (game, "Place 1", descriptions, [None,  None, "Place 4", "Place 2", None, None, None, None, None, None])
	
	# has doors to the north west, north east and east
	place2 = Place(game, "Place 2", descriptions, [None, "Place 4", "Place 3", None, None, None, None, "Place 1", None, None])

	# has doors to the west
	place3 = Place(game, "Place 3", descriptions, [None, None, None, None, None, None, "Place 2", None, None, None])

	# has doors to the west and south-west
	place4 = Place(game, "Place 4", descriptions, [None, None, None, None, None, "Place 2", "Place 1", None, None, None])

	place1.setAdjacentPlaces(game)
	place2.setAdjacentPlaces(game)
	place3.setAdjacentPlaces(game)
	place4.setAdjacentPlaces(game)

	user = User(game, "user1", "Place 1", "n", False) # start in Place1 facing north
	game.setUser(user)
	return game


def main():

	# run topologyOne
	game = runTopologyOne()
	game.setIsValid()

	# testing moving
	action1 = Action()
	action1.setVerb("move_user")

	print("Topology 1\n\n")
	print("Testing valid moves: \n\n")

	# valid moves in topology # 1
	valid_moves = ["e", "s", "w", "n", "s", "e", "n", "w"]

	for m in valid_moves:
		
		game.user.printUser(game)

		action1.setDirection(m)

		# call game as though you are the parser
		game.fromParserToGame(action1)

	print("\n\n")
	print("Testing invalid moves (manually check print of 'invalid request' for each): \n\n")
	
	# invalid moves in topology # 1 (cannot do  from Place 1)
	invalid_moves = ["n", "w", "ne", "nw", "se", "sw"]

	for m in invalid_moves:
		game.user.printUser(game)

		action1.setDirection(m)

		# call game as though you are the parser
		game.fromParserToGame(action1)

	print("\n\n")
	print("Topology 2 (diagonal moves)\n\n")
	print("Testing valid moves (manually check that each move occurs): \n\n")


	# run topologyTwo
	game = runTopologyTwo()
	game.setIsValid()

	# testing moving
	action2 = Action()
	action2.setVerb("move_user")

	# valid moves in topology # 2
	valid_moves = ["e", "sw", "nw", "se", "e", "w", "nw"]

	for m in valid_moves:
		game.user.printUser(game)

		action2.setDirection(m)

		# call game as though you are the parser
		game.fromParserToGame(action2)

	print("\n\nTesting invalid moves (manually check that 'invalid request' is printed): \n\n")
	
	# invalid moves in topology # 2 (from Place 1)
	invalid_moves = ["ne", "n", "nw", "w", "sw"]

	for m in invalid_moves:
		game.user.printUser(game)

		action2.setDirection(m)

		# call game as though you are the parser
		game.fromParserToGame(action2)

# run main
main()
