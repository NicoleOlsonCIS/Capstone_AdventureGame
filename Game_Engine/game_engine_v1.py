# Game Engine Unit of Capstone Adventure Game Version 1 (Week 3)
# 
# Adjacent Rooms is a list of size 8 and has the following meaning: 
#	AdjacentRooms[0] represents north
#	AdjacentRooms[1] represents north-east
#	AdjacentRooms[2] represents east
#   (and so on clockwise)
# 
#
# define the "Game" class
class Game:
	def __init__(self):
		self.rooms = {}
		self.isValid = {}

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
	def setIsValid(self):
		newdict={} 
		user_room = self.user.getCurrentRoom()
		adjacent_rooms = user_room.getAdjacentRooms()
   
		# create a list of available move locations
		valid_moves = []
		if adjacent_rooms[0] is not None:
			valid_moves.append("n")
		if adjacent_rooms[1] is not None:
			valid_moves.append("ne")
		if adjacent_rooms[2] is not None:
			valid_moves.append("e")
		if adjacent_rooms[3] is not None:
			valid_moves.append("se")
		if adjacent_rooms[4] is not None:
			valid_moves.append("s")
		if adjacent_rooms[5] is not None:
			valid_moves.append("sw")
		if adjacent_rooms[6] is not None:
			valid_moves.append("w")
		if adjacent_rooms[7] is not None:
			valid_moves.append("nw")

		# set the dictionary with key "move" to the array of valid moves
		newdict = {"move_user": valid_moves}

		# --- other actions involving objects (future) --- #

		# set the "is valid" attribute to the current dictionary of valid game operations
		self.isValid = newdict

	def checkIsValid(self, action, object, direction):
		if action == "move_user":
			v = self.isValid.get("move_user")
			for i in v:
				if i == direction:
					return True
			print("No room in " + direction + " direction.")
			return False
		else:
			print("Move_user + direction is the only valid action in version 1")
	

	# Precondition: called after isValid()
	def executeRequest(self, action, object, direction):
		if action == "move_user":
			self.moveUser(direction)
		else:
			print("Invalid action type for version 1")


	# Precondition: room adjacency pre-validated
	def moveUser(self, direction):
		user_room = self.user.getCurrentRoom()
		adjacent_rooms = user_room.getAdjacentRooms()

		if direction == "n":
			self.user.updateRoom(adjacent_rooms[0])
			print("User moved north.")
		elif direction == "ne":
			self.user.updateRoom(adjacent_rooms[1])
			print("User moved north-east.")
		elif direction == "e":
			self.user.updateRoom(adjacent_rooms[2])
			print("User moved east.")
		elif direction == "se":
			self.user.updateRoom(adjacent_rooms[3])
			print("User moved south-east.")
		elif direction == "s":
			self.user.updateRoom(adjacent_rooms[4])
			print("User moved south.")
		elif direction == "sw":
			self.user.updateRoom(adjacent_rooms[5])
			print("User moved south-west.")
		elif direction == "w":
			self.user.updateRoom(adjacent_rooms[6])
			print("User moved west.")
		elif direction == "nw":
			self.user.updateRoom(adjacent_rooms[6])
			print("User moved north-west.")
		else:
			print("invalid direction")


# define the "Room" class
class Room:
	def __init__(self, game, name, description, adjacentRoomNames):
		self.name = name
		self.adjacentRoomNames = adjacentRoomNames
		self.description = description
		game.addRoom(self) # creates a map between name and room object in the game

	#  translates array to "adjacentRooms" array after all Rooms created
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
		print("Username: " + self.name + " Current Room: " + room_name)