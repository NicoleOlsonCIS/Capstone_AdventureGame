# Manual Testing Game Engine Unit of Capstone Adventure Game Version 1 (Week 3)
# 
# 4 Rooms created (objects) 
# 1 user created (object)
#
# Room topology # 1:
#    ____	 	  ____	
#   |r1  |       |r2  |
#   |    |-------|    |    
#   |____|       |____|
#      |	 	   |
#      |		   |
#    __|_		  _|__
#   |r4  |       |r3  |
#   |    |-------|    | 
#   |____|       |____|
#
#
#
# Room topology # 2: (diagonal entrances/exits)
#
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
from game_engine_v1 import *

def runTopologyOne():
	
	game = Game()
	
	# has doors to the east and south
	room1 = Room (game, "Room 1", "Room 1 description", [None,  None, "Room 2", None, "Room 3", None, None, None])
	
	# has doors to the west and south
	room2 = Room(game, "Room 2", "Room 2 description", [None, None, None, None, "Room 4",  None, "Room 1", None])

	# has doors to the north and west
	room3 = Room(game, "Room 3", "Room 3 description", ["Room 1", None, None, None, None, None, "Room 4", None])

	# has doors to the north and east
	room4 = Room(game, "Room 4", "Room 4 description", ["Room 2", None, "Room 3", None, None, None, None, None])

	user = User(game, "user1", "Room 1", False)

	room1.setAdjacentRooms(game)

	room2.setAdjacentRooms(game)
	room3.setAdjacentRooms(game)
	room4.setAdjacentRooms(game)

	game.setUser(user)
	return game

def runTopologyTwo():
	
	game = Game()
	
	# has doors to the east and south-east
	room1 = Room 
	(
		game, 
		"Room 1", 
		"Room 1 description", 
		[None,  None, "Room 4", "Room 2", None, None, None, None]
	)
	
	# has doors to the north west, north east and east
	room2 = Room
	(
		game, 
		"Room 2", 
		"Room 2 description", 
		[None, "Room 4", "Room 3", None, None, None, None, "Room 1"]
	)

	# has doors to the west
	room3 = Room
	(
		game, 
		"Room 3",
		"Room 3 description", 
		[None, None, None, None, None, None, "Room 2", None]
	)

	# has doors to the west and south-west
	room4 = Room
	(
		game, 
		"Room 4", 
		"Room 4 description", 
		[None, None, None, None, None, "Room 2", "Room 1", None]
	)

	room1.setAdjacentRooms(game)
	room2.setAdjacentRooms(game)
	room3.setAdjacentRooms(game)
	room4.setAdjacentRooms(game)

	user = User(game, "user1", "Room 1", False) # start in room1
	game.setUser(user)
	return game


def main():

	# run topologyOne
	game = runTopologyOne()
	# valid moves in topology # 1
	valid_moves = ["e", "s", "w", "n", "s", "e", "n", "w"]

	for m in valid_moves:
		game.user.printUser(game)
		game.setIsValid()
		direction = m
		isValidRequest = game.checkIsValid("move_user", None, direction)
		if(isValidRequest):
			game.executeRequest("move_user", None, direction)
		else:
			print("Invalid request")

	# invalid moves in topology # 1 (cannot do  from Room 1)
	invalid_moves = ["n", "w", "ne", "nw", "se", "sw"]

	for m in invalid_moves:
		game.user.printUser(game)
		game.setIsValid()
		direction = m
		isValidRequest = game.checkIsValid("move_user", None, direction)
		if(isValidRequest):
			game.executeRequest("move_user", None, direction)
		else:
			print("Invalid request")

# run main
main()