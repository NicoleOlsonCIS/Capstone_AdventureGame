# Game Engine Unit of Capstone Adventure Game Version 1 (Week 3)
# 
# 4 Rooms created (objects) 
# 1 user created (object)
# 
# User location in room changes based on inputs "move n, move e, move s, move w"
# 
# Print rooms and user location after each move
# Errors for invalid moves
# Unit tests: test user has been moved correctly or that correct error message displayed
# 
#
# Room topology:
#    ____	  ____	
#   |r1  |       |r2  |
#   |    |-------|    |    
#   |____|       |____|
#      |	   |
#      |	   |
#    __|_	  _|__
#   |r3  |       |r4  |
#   |    |-------|    | 
#   |____|       |____|
#
#

# define the "Game" class
class Game:
	def __init__(self):
		self.rooms = {}
		self.isValid = {}
	
	def run(self):
		print("Game ran")

	def addRoom(self, room):
		self.rooms[room.name] = room

	def getRoom(self, name):
		if name in self.rooms.keys():
			return self.rooms[name]
		return None

	def setUser(self, user):
		self.user = user

	def parseParserInput(self, action): 
		# parse input from Parser and call checkIsValid() with appropriate args
		return None

	# called after every change in game state in preparation for input from parser
	def setListOfValidActions(self):
		newdict={} 
		user_room = self.user.getCurrentRoom()
		adjacent_rooms = user_room.getAdjacentRooms()
   
		# create a list of available move locations
		valid_moves = []
		if adjacent_rooms[0] is not None:
			valid_moves.append("n")
		if adjacent_rooms[1] is not None:
			valid_moves.append("e")
		if adjacent_rooms[2] is not None:
			valid_moves.append("s")
		if adjacent_rooms[3] is not None:
			valid_moves.append("w")

		# set the dictionary with key "move" to the array of valid moves
		newdict = {"move": valid_moves}

		# -- other actions involving objects (future) -- #

		# set the "is valid" attribute to the current dictionary of valid game operations
		self.isValid = newdict

	def checkIsValid(self, action, object, direction):
		if action == "move_user":
			v = self.isValid.get("move")
			for i in v:
				if i == direction:
					return True
			print("No room in " + direction + " direction.")
			return False
		else:
			print("Move_user + direction(n, e, s, w) is the only valid action in version 1")
	

	# precondition: called only after it is determined to be a valid request
	def executeRequest(self, action, object, direction):
		if action == "move_user":
			self.moveUser(direction)
		else:
			print("Invalid action type for version 1")


	# move the user based on "direction" input (room adjacency pre-validated)
	def moveUser(self, direction):
		user_room = self.user.getCurrentRoom()
		adjacent_rooms = user_room.getAdjacentRooms()

		if direction == "n":
			self.user.updateRoom(adjacent_rooms[0])
			print("User moved to the north!")
		elif direction == "e":
			self.user.updateRoom(adjacent_rooms[1])
			print("User moved to the east!")
		elif direction == "s":
			self.user.updateRoom(adjacent_rooms[2])
			print("User moved to the south!")
		elif direction == "w":
			self.user.updateRoom(adjacent_rooms[3])
			print("User moved to the west!")
		else:
			print("invalid direction")


# define the "Room" class
class Room:
	def __init__(self, game, name, description, adjacentRoomNames):
		self.name = name
		self.adjacentRoomNames = adjacentRoomNames
		self.description = description
		game.addRoom(self) # creates a map between name and room object in the game

	# translates "door" array to "adjacentRooms" array after all Rooms created
	def setAdjacentRooms(self, game):
		self.adjacentRooms = list(map(game.getRoom, self.adjacentRoomNames)) # <-- expands into calls to get room for each door

	def getRoomName(self):
		return self.name

	def getAdjacentRooms(self):
		return self.adjacentRooms # an array of Room or None


# define the User class
class User:
	def __init__(self, game, name, startingRoom, saved):
		if saved == False:
			self.name = name
			self.current_room = game.getRoom(startingRoom) 
		else:
			print("Constructing user from saved game")

	def getCurrentRoom(self):
		return self.current_room

	def updateRoom(self, room):
		self.current_room = room

	def printUser(self, game):
		room = self.current_room
		room_name = room.getRoomName()
		print("Name: " + self.name)
		print("Current Room: " + room_name)


# placeholder until we start loading the game from file
def createHardcodedGame():
	game = Game()
	room1 = Room(game, "room1", "This is room 1", [None,    "room2", "room3",  None])
	room2 = Room(game, "room2", "This is room 2", [None,       None, "room4",  "room1"])
	room3 = Room(game, "room3", "This is room 3", ["room1",    None, "room4",  None])
	room4 = Room(game, "room4", "This is room 4", ["room2",    None,    None,  "room3"])

	room1.setAdjacentRooms(game)
	room2.setAdjacentRooms(game)
	room3.setAdjacentRooms(game)
	room4.setAdjacentRooms(game)

	user = User(game, "FirstUser", "room1", False) # start in room1
	game.setUser(user)
	return game

def main():
	game = createHardcodedGame()

	# sample run of game
	moves = ["e", "s", "w", "n"]

	for m in moves:
		game.user.printUser(game)
		game.setListOfValidActions()
		direction = m
		isValidRequest = game.checkIsValid("move_user", None, direction)
		if(isValidRequest):
			game.moveUser(direction)
		else:
			print("Cannot move user in direction " + direction)

# run main
main()

# say goodbye
print("\n\n\nGoodbye.")
