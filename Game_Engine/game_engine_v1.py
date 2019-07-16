# Game Engine Unit of Capstone Adventure Game Version 1 (Week 3)
# 
# v1.1 --> change "Room" class to "Place" and enable 3D movement (just "up/down")
# v2  --> add "Thing" class
# v3 --> add support and error handling for "look" action
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

	def getPlace(self, name):
		if name in self.places.keys():
			return self.places[name]
		return None

	# prints the description of the current room
	def printRoom(self):
        	place_name = self.user.current_place.name 
        	# get the description of the place based on the time
        	place_description = self.user.current_place.getDescriptionBasedOnTime(self.time)
        	output = place_name + "\n" + place_description
        	print(output)

	# prints the description of a feature or object 
	def printThing(self, itemname):
		for t in self.user.things:
			if t.name == itemname:
				print(t.description)
				return
		for t in self.user.current_place.things:
			if t.name == itemname:
				print(t.description)
				return 

        # takes the thing the user wants to examine
        # prints appropriate outputs 
	def handleLook(self, attemptedObj, canLook):
		if canLook:
                	# if nothing or "room" specified, examine current room 
			if attemptedObj == None or attemptedObj == "room":
        			self.printRoom()
			# if current room name specified, examine current room
			elif attemptedObj == self.user.current_place.name:
				self.printRoom()
			# print thing description if thing available for examining
			else:
				printThing(attemptedObj)
		else:
			# if user tries to examine a room that is not the current one, error
			if attemptedObj in self.places.keys():
				print("You are not currently in that location.")
				return
			# otherwise print generic error msg
			print("You don't see anything like that here.")

	# point of entry from parser, game takes care of input from this point
	# either by updating the game or sending error messages
	def fromParserToGame(self, action): 
		valid = self.checkIsValid(action)

		if(valid):

			self.executeRequest(action)

			# update the list of valid moves in the new game state
			self.setIsValid()
			
			# if the user was moved, re-orient user
			if action.verb == "move_user":
				# get the users direction (maybe don't need this)
				# direction = self.user.direction
                                self.printRoom()
 
			if action.verb == "look":
                        	handleLook(action.direct_obj, True)
		else: 

			if action.verb == "look":
                        	handleLook(action.direct_obj, False)

			else:
				print("Invalid action")

	# called after every change in game state in preparation for next input from parser
	def setIsValid(self):
		newdict={} 
		user_place = self.user.current_place
		adjacent_places = self.user.current_place.adjacent_places
   
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

		# new in v2 (build set of valid actions regarding objects)
		valid_takes = [item.name for item in user_place.things if item.isTakeable] 
		valid_drops = [item.name for item in self.user.things]
                # new in v3
                # can examine things that are in the current place or in inventory
		valid_looks = [item.name for item in user_place.things]
		for item in self.user.things:
                    valid_looks.append(item.name) 

		# set the dictionary with keys as actions and values as valid corresponding things
		newdict = {"move_user": valid_moves, "take": valid_takes, "drop": valid_drops, "look": valid_looks}

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
		elif action.verb == "take":
			v = self.isValid.get("take")
			for i in v: 
				if i == action.direct_obj:
					return True
			return False
		elif action.verb == "drop":
			v = self.isValid.get("drop")
			for i in v: 
				if i == action.direct_obj:
					return True
			print("User is not holding " + action.direct_obj) # eventually error messages sent elsewhere for printing
			return False

		elif action.verb == "look":
                        v = self.isValid.get("look")
                        # check if specified object can be examined (is in current place or inventory) 
                        for i in v:
                                if i == action.direct_obj:
                                      return True   
                        # if no object specified or current room specified, examine room
                        if action.direct_obj == None:
                            return True
                        if action.direct_obj == "room":
                            return True
                        if action.direct_obj == self.user.current_place.name: 
                            return True
                        return False
		else:
			print("Invalid game action")
	

	# Precondition: called after checkIsValid() returns True
	def executeRequest(self, action):
		if action.verb == "move_user":
			self.moveUser(action.direction)
			self.updateTime(1)
			return

		if action.verb == "take":
			self.user.pickUpObject(action.direct_obj)
			# time update of 1 hour 
			self.updateTime(1)
			return

		if action.verb == "drop":
			self.user.dropObject(action.direct_obj)
			# add a time update
			self.updateTime(1)
			return

		if action.verb == "look":
                        # time update 
                        self.updateTime(1)
                        return 
		else:
			print("Invalid action type for version 1 or 2")


	# Precondition: place adjacency pre-validated
	def moveUser(self, direction):
		user_place = self.user.current_place
		adjacent_places = user_place.adjacent_places

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
	# game(game object), name(string), descriptions[day, night], adjacentPaceNames[10 strings])
	def __init__(self, game, name, descriptions, adjacentPlaceNames, things = None):
		self.name = name
		self.adjacent_place_names = adjacentPlaceNames
		self.things = things

		timeDict = {"day" : descriptions[0], "night": descriptions[1]}
		self.description = timeDict 

		game.addPlace(self) # creates a map between name and place object in the game

	#  translates array to "adjacentplaces" array after all places created
	def setAdjacentPlaces(self, game):
		self.adjacent_places = list(map(game.getPlace, self.adjacent_place_names))

	def getDescriptionBasedOnTime(self, time): 
		# between 6 am and 6 pm is currently considered "day"
		if time > 6 and time < 18: 
			return self.description.get("day")
		else:
			return self.description.get("night")
	
	# new in v2 (correpond to take and drop)
	def addThing(self, thing):
		self.things.append(thing)

	def removeThing(self, thing):
		self.things.remove(thing)


# define the User class
class User:
	# game(game object), name(string), place name (string), user direction(string), saved game(bool) 
	def __init__(self, game, name, startingPlace, startingDirection, saved):
		if saved == False:
			self.name = name
			self.current_place = game.getPlace(startingPlace)
			self.direction = startingDirection

			# new in v2
			arr = []
			self.things = arr
		else:
			print("Constructing user from saved game")

	def getUserDirection(self):
		return self.direction

	def updateUserDirection(self, newDirection):
		self.direction = newDirection 
	
	# new in v2
	def pickUpObject(self, thing):
		# add to user array
		self.things.append(thing)
		# remove the thing from the Place it is in
		self.current_place.removeThing(thing)

	# new in v2
	def dropObject(self, thing):
		# remove from user array
		self.things.remove(thing)
		# add thing to the place the user is in
		self.current_place.addThing(thing)

	# new in v2, for figuring out if user has an thing in possession
	def userHasThing(self, thing):
		found = False
		for t in self.things: 
			if t == thing:
				found = True
		return found

	def updatePlace(self, place):
		self.current_place = place

	def printUser(self, game):
		print("\n\n")
		place = self.current_place
		place_name = place.name
		print("Username: " + self.name + " Current place: " + place_name)

#define the "Thing" class
class Thing: 
	def __init__(self, name, description, starting_location, is_takeable):
		self.name = name
		self.description = description
		self.location = starting_location # place object
		self.is_takeable = is_takeable # defines whether feature or object
		self.with_user = False

		# when the user drops
		def leaveUser(self, new_location):
			self.location = new_location # place where user is dropping it
			self.with_user = False

		# when the user picks up
		def becomeWithUser(self):
			self.with_user = True

		# differentiates object from feature
		def isTakeable(self):
			return self.is_takeable


