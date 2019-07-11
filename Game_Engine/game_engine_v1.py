# Game Engine Unit of Capstone Adventure Game Version 1 (Week 3)
# 
# v1.1 --> change "Room" class to "Place" and enable 3D movement (just "up/down")
# 
#
# define the "Game" class

import action

class Game:

	# constructor expects: 
	# day(int), time(int)
	def __init__(self, day, time):
		self.places = {}
		self.isValid = {}
		self.day = day	# time component new in v1.1
		self.time = time

	def setUser(self, user):
		self.user = user

	def addPlace(self, place):
		self.places[place.name] = place

	# takes the change in hours per an event in the game
	def updateTime(self, timeChange):
		self.time += timeChange
		
		# if we've crossed into a new day
		if self.time > 23: 
			self.time -= 23
			self.day = self.day + 1
		
	def getTime(self):
		return self.time
	
	def getDay(self):
		return self.day

	def getPlace(self, name):
		if name in self.places.keys():
			return self.places[name]
		return None

	# point of entry from parser, game takes care of input from this point
	# either by updating the game or sending error messages
	def fromParserToGame(self, action): 
		valid = self.checkIsValid(action)

		if(valid):

			self.executeRequest(action)
			# update the list of valid moves in the new game state

			self.setIsValid()
			# get the current/new place of the user

			user_place = self.user.getCurrentPlace()
			# get the description of the place based on the time
			
			place_description = user_place.getDescriptionBasedOnTime(self.time)
			# send info to the print module

		else: 
			# error message for input
			print("Invalid action.")

	# called after every change in game state in preparation for next input from parser
	def setIsValid(self):
		newdict={} 
		user_place = self.user.getCurrentPlace()
		adjacent_places = user_place.getAdjacentPlaces()
   
		# create a list of available move locations
		valid_moves = []
		if adjacent_places[0] is not None:
			valid_moves.append("n")
		if adjacent_places[1] is not None:
			valid_moves.append("ne")
		if adjacent_places[2] is not None:
			valid_moves.append("e")
		if adjacent_places[3] is not None:
			valid_moves.append("se")
		if adjacent_places[4] is not None:
			valid_moves.append("s")
		if adjacent_places[5] is not None:
			valid_moves.append("sw")
		if adjacent_places[6] is not None:
			valid_moves.append("w")
		if adjacent_places[7] is not None:
			valid_moves.append("nw")

			# new in v1.1
		if adjacent_places[8] is not None:
			valid_moves.append("up")
		if adjacent_places[9] is not None:
			valid_moves.append("down")

		# set the dictionary with key "move" to the array of valid moves
		newdict = {"move_user": valid_moves}

		# --- other actions involving objects (future) --- #

		# set the "is valid" attribute to the current dictionary of valid game operations
		self.isValid = newdict

	# take action object and consult "isValid" dictionary 
	def checkIsValid(self, action): 
		if action.verb == "move_user":
			v = self.isValid.get("move_user")
			for i in v:
				if i == action.direction:
					return True
			print("No place in " + action.direction + " direction.")
			return False
		else:
			print("Move_user + direction is the only valid action in version 1")
	

	# Precondition: called after checkIsValid()
	def executeRequest(self, action):
		if action.verb == "move_user":
			self.moveUser(action.direction)

			# update the game time (just moving by 1 hour for now) 
			# idea is that other actions will take different times
			self.updateTime(1)
		else:
			print("Invalid action type for version 1")


	# Precondition: place adjacency pre-validated
	def moveUser(self, direction):
		user_place = self.user.getCurrentPlace()
		adjacent_places = user_place.getAdjacentPlaces()

		if direction == "n":
			self.user.updatePlace(adjacent_places[0])
			print("User moved north.")
		elif direction == "ne":
			self.user.updatePlace(adjacent_places[1])
			print("User moved north-east.")
		elif direction == "e":
			self.user.updatePlace(adjacent_places[2])
			print("User moved east.")
		elif direction == "se":
			self.user.updatePlace(adjacent_places[3])
			print("User moved south-east.")
		elif direction == "s":
			self.user.updatePlace(adjacent_places[4])
			print("User moved south.")
		elif direction == "sw":
			self.user.updatePlace(adjacent_places[5])
			print("User moved south-west.")
		elif direction == "w":
			self.user.updatePlace(adjacent_places[6])
			print("User moved west.")
		elif direction == "nw":
			self.user.updatePlace(adjacent_places[7])
			print("User moved north-west.")

			# new in v1.1
		elif direction == "up":
			self.user.updatePlace(adjacent_places[8])
			print("User moved up.")
		elif direction == "down":
			self.user.updatePlace(adjacent_places[9])
			print("User moved down.")

		else:
			print("invalid direction")

# define the "Place" class
class Place:

	# constructor expects:
	# game(game object), name(string), descriptions[day, night], adjacentPaceNames[10 strings]
	def __init__(self, game, name, descriptions, adjacentPlaceNames):
		self.name = name
		self.adjacentPlaceNames = adjacentPlaceNames

		# new in v1.1 
		timeDict = {"day" : descriptions[0], "night": descriptions[1]}
		self.description = timeDict 

		game.addPlace(self) # creates a map between name and place object in the game

	#  translates array to "adjacentplaces" array after all places created
	def setAdjacentPlaces(self, game):
		self.adjacentPlaces = list(map(game.getPlace, self.adjacentPlaceNames)) # <-- expands into calls to get place for each door

	def getPlaceName(self):
		return self.name

	def getAdjacentPlaces(self):
		return self.adjacentPlaces # an array of place or None

	def getDescriptionBasedOnTime(self, time): 
		# between 6 am and 6 pm is currently considered "day"
		if time > 6 and time < 18: 
			return self.description.get("day")
		else:
			return self.description.get("night")

# define the User class
class User:

	# constructor expects: 
	# game(game object), name(string), place name (string), user direction(string), saved game(bool) 
	def __init__(self, game, name, startingPlace, startingDirection, saved):
		if saved == False:
			self.name = name
			self.current_place = game.getPlace(startingPlace)

			# new in v1.1 
			self.direction = startingDirection
		else:
			print("Constructing user from saved game")


	def getCurrentPlace(self):
		return self.current_place

	# new in v1.1
	def getUserDirection(self):
		return self.direction
	def updateUserDirection(self, newDirection):
		self.direction = newDirection 


	def updatePlace(self, place):
		self.current_place = place

	def printUser(self, game):
		place = self.current_place
		place_name = place.getPlaceName()
		print("Username: " + self.name + " Current place: " + place_name)