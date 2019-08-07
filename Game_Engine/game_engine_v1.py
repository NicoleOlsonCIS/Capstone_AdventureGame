# Game Engine Unit of Capstone Adventure Game Version 1 (Week 4)
# 
# v1.1 --> change "Room" class to "Place" and enable 3D movement (just "up/down")
# v2  --> add "Thing" class
# v3 --> add support and error handling for "look" action
# v4 --> finish support and error handling for "take", "drop", "look", "sleep"
# v5 --> additional error handling. refine sleep action
# v6 --> implement show_help and show_inventory
# v7 --> update "look"/"take"/"drop" and time with integration/gameplay issue fixes
# v8 --> change print statements to incorporate formatted output
# v9 --> implement "doors" on places that have doors (changes in playgame.py as well)
# v10 --> change 'up' and 'down' to 'u' and 'd' to match parser
# v11 --> descriptions of Place now based on number of visits as well
# v11.1 --> error handling for "search" and "read"
# v11.2 --> toggle item description for when it is present/not present//viewable/not viewable 
# v11.3 --> accommodate alternate thing names (e.g. "scrap of fabric"/"fabric scrap"/"scrap"/"fabric")
# v11.4 --> finish implementing search and read, add new day message 
# v11.5 --> make dropped items show up in room description (unless dropped inside a feature) 
# v11.6 --> implement insert, update error handling 
# v11.7 --> implement listen 
# v12   --> implement character, including edits to output
# v13   --> verbs with no objects condition, implementation added to "handle" functions
# v13.1 --> sleep msg, exit msg from platform to fields, lock front door after user is inside, start impl. "open", expand help, add narrative intro 
# v13   --> verbs with no objects condition, implementation added to "handle" functions
# v13.1 --> sleep msg, exit msg from platform to fields, lock front door after user is inside, start impl. "open", expand help, add narrative intro 
# v13.2 --> restrict user movement until after speaking to Maude; error msgs for violent actions (e.g. kill), fromParserToGame None check, verbOnlyTake fix 
# v13.3 --> impl. looking out windows, opening vs. searching

# define the "Game" class
#
import action
from output import *

class Game:

	def __init__(self, day, time):
		self.places = {}
		self.isValid = {}
		self.day = day	# time component new in v1.1
		self.time = time
		# v13 Thing object (and only Thing objs) the user last looked at (for disambiguating verb without subject)
		self.lastLooked = None 
		self.narrativeIntro = [] 

	def setUser(self, user):
		self.user = user

	def addPlace(self, place):
		self.places[place.name] = place

	# takes the change in hours per an event in the game
	def updateTime(self, timeChange):
		self.time += timeChange
		
		# v7: if we've crossed into a new 40-hr day
		if self.time > 39: 
			self.time -= 39 
			self.day = self.day + 1
			Output.print_look("Start of Day {}".format(self.day))

	# v13.3: tell whether it is day or night
	def dayOrNight(self):
		if self.time > 5 and self.time < 25:
			return "day"
		else:
			return "night" 

	def getPlace(self, name):
		if name in self.places.keys():
			return self.places[name]
		return None

	# v13 
	def upDateLastLooked(self, thing):
		self.lastLooked = thing

	# v13 handle when only thing input is "take"
	# handles context of when user has just looked at somethign that reveals a takeable object not in room descriptoin
	def verbOnlyTake(self):
		numThings = len(self.user.current_place.things)
		takeable_things = []
		if numThings > 0:
			# count up how many are takable
			count = 0
			things = self.user.current_place.things
			for n in things:
				if n.is_takeable:
					count += 1
					takeable_things.append(n)
			# if there is something in the room that is takeable
			available_takeable_things = []
			if count > 0:
				# now count of how many are takeable that are NOT in the "hasOtherItems" list of another
				# create a list of items that are not on any hasOtherItems list
				att = 0
				for tt in takeable_things:
					found_on_another_thing = False
					for c in things:
						# if this isn't the same thing
						if c.name != tt.name:
							# if the thing has other items
							if len(c.hasOtherItems) > 0:
								other_items = c.hasOtherItems
								for oi in other_items:
									if tt.name == oi:
										found_on_another_thing = True
					if found_on_another_thing == False:
						available_takeable_things.append(tt)
						att += 1
				# if there is a takeable thing that is NOT on another thing's "hasOtherItems" list
				if att > 0:
					# if there is one thing, then take it
					if att == 1:
						self.user.pickUpObject(available_takeable_things[0].name)
						# update the clock
						self.updateTime(1)
						# print about it
						Output.print_take(available_takeable_things[0].name)
					# if there is more than on thing, tell user to be more specific 
					if att > 1: 
						Output.print_input_hint("You see multiple things you could take. Be more specific.")

				# if att is 0, then all things that are takeable are related to other things.
				# check what the user has just looked at. If there is one thing related to that 
				# thing AND it is takeable, then take it. Otherwise, tell user to look around more. 
				else:
					if self.lastLooked != None:
						print(self.lastLooked.name)
						ll = self.lastLooked
						
						# check if what the user last looked at was in this room
						present = False
						for t in things: 
							if t.name == ll.name:
								present = True

						# if the last thing they looked at was elsewhere, then it's not relevent 
						if present == False:
							Output.print_input_hint("Try looking around more. There may be things present that you can take.")
							return
						else:
							# if the last object the user looked at is present and has 1 other thing
							if len(ll.hasOtherItems) == 1:
								name = ll.hasOtherItems[0]
								# go through the things in the room, match name, check if takeable
								# the last thing the user looked at could be in a different room or not takeable
								for t in things:
									if t.name == name:
										if t.is_takeable:
											# infer that user just looked at a hidden takeable thing (i.e. scrap of fabric)
											# take the object
											self.user.pickUpObject(t.name)
											# update the clock
											self.updateTime(1)
											# print about it
											Output.print_take(t.name)
											return
							# last thing the user looked at is present but has nothing
							elif len(ll.hasOtherItems) == 0:
								Output.print_input_hint("Try looking around more. There may be things present that you can take.")
							# last looked item is present but has multiple things associated
							else:
								Output.print_input_hint("You need to be more specific.")
					else:
						Output.print_input_hint("Try looking around more. There may be things present that you can take.")
			# there are things, but they are not takeable, so are features or characters
			elif count == 0: 
				Output.print_input_hint("You see only things you can look at or talk to.")
		# there are no features or objects or characters
		else:
			Output.print_error("This room is currently devoid of features, things and characters. It may be haunted, or someone has taken everything already.")

	#v13 when only input is "move", it is valid when: there is only one way to move and door is not locked
	def verbOnlyMove(self):
		adjacent_places = self.user.current_place.adjacent_places
		count = 0
		i = 0
		dir = -1
		opposing_door_dict = {0: "s", 1: "sw", 2: "w", 3: "nw", 4: "n", 5: "ne", 6: "e", 7: "se", 8: "d", 9: "u"}
		int_to_str_dict = {0: "n", 1: "ne", 2: "e", 3: "se", 4: "s", 5: "sw", 6: "w", 7: "nw", 8: "u", 9: "d"}

		for a in adjacent_places:
			if a != None:
				count += 1
				dir = i   # if there is only 1 exit, dir will be the index of that exit
			i += 1

		# if more than one, output error message
		if count > 1: 
			Output.print_error("There is more than one way to move from this place.")
		# if one, determine if it is a locked door
		if count == 1:
			# get the corresponding door from the dictionary
			doorDir = opposing_door_dict.get(dir)
			if adjacent_places[dir].doors[doorDir] != "locked":
				# move user in that direction (sending string not int)
				self.moveUser(int_to_str_dict.get(dir))
				# otherwise this is not called
				self.setIsValid()
				self.user.current_place.printRoom(self.time)
				self.user.current_place.updateNumEntries()
			else:
				# door is looked
				self.handleLockedDoor(int_to_str_dict.get(dir))

	#v15 singular objects, i.e. "wooden door", "archway", "north door", etc. 
	def handleSingularInput(self,direction, directObj, indirectObj):
		compass = ["n", "ne", "e", "se", "s", "sw", "w", "nw", "u", "d"]
		int_to_str_dict = {0: "n", 1: "ne", 2: "e", 3: "se", 4: "s", 5: "sw", 6: "w", 7: "nw", 8: "u", 9: "d"}
		opposing_door_dict = {0: "s", 1: "sw", 2: "w", 3: "nw", 4: "n", 5: "ne", 6: "e", 7: "se", 8: "d", 9: "u"}
		adjacent_places = self.user.current_place.adjacent_places
		
		dict_passages = self.user.current_place.passages
		
		current_place = self.user.current_place
		
		two_words = ""
		combined = False
		if directObj != None and indirectObj != None:
			two_words = directObj + " " + indirectObj
			combined = True

		i = 0
		match = False
		match2 = False
		direction = None
		while i < 10:
			#get the passage by key
			passages = dict_passages.get(compass[i])
			# check if the array has anything in it
			if len(passages) > 0:
				for p in passages:
					if directObj == p:
						if match == False:
							match = True
							direction = i # store number not string for lookup purposes
						else:
							match2 = True
					elif combined:
						if p == two_words:
							if match == False:
								match = True
								direction = i # store number not string for lookup purposes
							else:
								match2 = True
			i += 1

		if match and match2:
			if directObj == "leave":
				Output.print_input_hint("There is more than one way to leave. Be more specific.")
				return
			elif directObj == "exit":
				Output.print_input_hint("There is more than one way to exit. Be more specific.")
				return
			if combined:
				directObj = two_words

			Output.print_input_hint("There is more than one " + directObj + ". Be more specific")
		elif match and not match2:
			# move the user 
			# get the opposing door info
			otherdoor = opposing_door_dict.get(direction)
			if adjacent_places[direction].doors[otherdoor] != "locked":
				# move user in that direction (sending string not int)
				self.moveUser(int_to_str_dict.get(direction))
				# otherwise this is not called
				self.setIsValid()
				self.user.current_place.printRoom(self.time)
				self.user.current_place.updateNumEntries()
			else:
				# door is looked
				self.handleLockedDoor(int_to_str_dict.get(direction))
		else:
			Output.print_error("That's not something you can do from here.")

	#v13.2
	def handleViolence(self, attemptObj, indirObj, canViolence):
		if canViolence:
			# TODO: ending scene
			return
		else:
			Output.print_error("Such unruly behavior is quite beyond you.")

	#v13.3
	def handleOpen(self, attemptedObj, indirObj, canOpen):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj

		if canOpen:
			for t in self.user.current_place.things:
				if t.name.lower() == attemptedObj or attemptedObj in t.altNames:
					# if user opens a searchable thing, automatically search the thing 
					if t.is_searchable:
						self.handleSearch(attemptedObj, indirObj, True)
					else:
						Output.print_look(t.openDescrip)
		else:
			# if user tries to open a door
			if "door" in attemptedObj:
				Output.print_input_hint("You don't need to explicitly open or close doors in this game. Try simply going in the direction you want.")
			# if user tries to open a book
			elif "book" in attemptedObj:
				Output.print_input_hint("You don't need to explicitly open books in this game. Try simply reading the book.")
			# TODO: ending scene
			else:
				Output.print_error("You don't see a way to open that.") 

	# v3: prints the description of a feature or object 
	# v11.2: also prints description of other objects dependent on this one 
	# v11.3: allow alternate thing names
	# v11.4: if a thing must be searched before revealing another thing inside,
	#  don't reveal thing just upon examining	
	def showThing(self, itemname):
		for t in self.user.things:
			if t.name.lower() == itemname or itemname in t.altNames:
				des = t.getDescription(self.time)
				Output.print_look(des) 
				return
		for t in self.user.current_place.things:
			if t.name.lower() == itemname or itemname in t.altNames:
				des = t.getDescription(self.time) 
				Output.print_look(des)

				# v11.2: if there are other objects viewable because of this one,
				# describe those other objects also.
				# v11.4: separate handling for searchable things in handleSearch function.
				if not t.is_searchable:
					for obj in t.hasOtherItems:
						for thingObj in self.user.current_place.things:
							if obj.lower() == thingObj.name.lower():
								Output.print_look(thingObj.isHereDescription)

		#v12 character interaction for looking at character
		if self.user.current_place.hasCharacter:
			character = self.user.current_place.character
			if character.name == itemname or itemname in character.altNames:
				Output.print_look(character.getDescription(self.time))
			return

	# v3: takes the thing the user wants to examine
	# prints appropriate outputs
	# v7: handle two-word obj names
	#v13.3: handle looking outside
	def handleLook(self, attemptedObj, indirObj, canLook):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj

		if canLook:
			# if nothing or "room" specified, examine current room 
			if attemptedObj == None or attemptedObj == "room":
				self.user.current_place.printRoom(self.time)
				self.user.current_place.updateNumLooks()
			# if current room name specified, examine current room
			elif attemptedObj == self.user.current_place.name.lower():
				self.user.current_place.printRoom(self.time)
				self.user.current_place.updateNumLooks()
			# look outside
			elif attemptedObj == "outside":
				for t in self.user.current_place.things:
					if t.is_window:
						if self.dayOrNight() == "day":
							Output.print_look(t.windowDescrips[0])
						else:
							Output.print_look(t.windowDescrips[1])
			# print thing description if thing available for examining
			else:
				self.showThing(attemptedObj)
				# v13 get the obj and update lastLooked
				things = self.user.current_place.things
				for t in things:
					if t.name == attemptedObj or attemptedObj in t.altNames:
						self.upDateLastLooked(t)
		else:
			# if user tries to examine a room that is not the current one, error
			for placename in self.places.keys():
				if attemptedObj == placename.lower():
					Output.print_error("You can't look around a room if you aren't in it.")
					return

			# if user tries to look outside in a windowless room
			if attemptedObj == "outside":
				Output.print_error("You can't look outside in a windowless place.") 
				return
	
			# otherwise print generic error msg
			Output.print_error("You don't see that here.")


	# v4: handle output for "take", "drop", "sleep"
	# v7: handle two-word obj names
	def handleTake(self, attemptedObj, indirObj, takeable):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj

		if takeable:
			if self.user.userHasThing(attemptedObj): 
				Output.print_error("You can't take what's already in your inventory.")
			else:
				Output.print_take(attemptedObj)

		# v13 edit to handle various cases of user just inputing "take"
		elif attemptedObj == None:
			self.verbOnlyTake()

		# thing is in current room but not takeable
		elif self.user.current_place.roomHasThing(attemptedObj): 
			Output.print_error("You can't put that in your inventory.")
			return
		else:
			# thing is not in current room
			Output.print_error("You don't see a " + attemptedObj + " that you can take.")


	def handleDrop(self, attemptedObj, indirObj, canDrop):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj

		if canDrop:
			Output.print_drop(attemptedObj) 
		else:
			if attemptedObj == None:
				Output.print_input_hint("Try being more specific about what you want to drop.")
			else:
				Output.print_error("You can't drop something that's not in your inventory.")	

	def handleSleep(self, attemptedObj, canSleep):
		if canSleep:
			print("You sleep.")
		else:
			if self.user.current_place.name != "Spare Room":
				Output.print_input_hint("You can only sleep in your room. You are not in your room at the moment.")
			elif self.dayOrNight() == "day": 
				Output.print_input_hint("You can only sleep at night.")
			elif attemptedObj != None and attemptedObj != "bed":
				Output.print_input_hint("You can only sleep on a bed.") 
			else:
				Output.print_input_hint("You aren't sleepy right now.")

	# new in v11.1
	def handleSearch(self, attemptedObj, indirObj, canSearch):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj
		if canSearch:
			# 11.4: reveal hidden item upon searching the enclosing item
			for t in self.user.current_place.things:
				if t.name.lower() == attemptedObj or attemptedObj in t.altNames:
					t.hasBeenSearched = True
					Output.print_look(t.searchDescrip)
					for obj in t.hasOtherItems:
						for thingObj in self.user.current_place.things:
							if obj.lower() == thingObj.name.lower():
								Output.print_look(thingObj.isHereDescription)
		else:
			if attemptedObj == None:
				Output.print_input_hint("Try being more specific about what you want to search.")
				return
			Output.print_error("That's not something you can search.")

	def handleRead(self, attemptedObj, indirObj, canRead):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj
		if canRead:
			# check for readable thing in current location
			for t in self.user.current_place.things:
				if t.name.lower() == attemptedObj or attemptedObj in t.altNames:
					# cycle through descriptions until exhausted, then start over at first description
					if len(t.readDescrips) > t.numTimesRead:
						Output.print_look(t.readDescrips[t.numTimesRead])
					else:
						t.numTimesRead -= len(t.readDescrips) 
						Output.print_look(t.readDescrips[t.numTimesRead])
					t.numTimesRead += 1
					return
			# check for readable thing in inventory
			for ob in self.user.things:
				if ob.name.lower() == attemptedObj or attemptedObj in ob.altNames:
					if len(ob.readDescrips) > 0:
						# cycle through descriptions until exhausted, then start over at first description
						if len(ob.readDescrips) > ob.numTimesRead:
							Output.print_look(ob.readDescrips[ob.numTimesRead])
						else:
							ob.numTimesRead -= len(ob.readDescrips)
							Output.print_look(ob.readDescrips[ob.numTimesRead])
						ob.numTimesRead += 1
						return 
		else:
			if attemptedObj == None:
				Output.print_input_hint("Try being more specific about what you want to read.")
				return
			if "book" in attemptedObj:
				Output.print_input_hint("Try being more specific about which book you want to read.")
				return
			Output.print_error("That's not something you can read.")

	# new in v11.6 
	def handleInsert(self, attemptedObj, indirObj, canInsert):
		if canInsert:
			if attemptedObj != None and indirObj != None: 
				Output.print_drop(attemptedObj + " inside the " + indirObj)
		else:
			if attemptedObj == None or indirObj == None:
				Output.print_input_hint("Try being more specific about what you want to put where.")
			else:
				if not self.user.userHasThing(attemptedObj):
					Output.print_error("You can't drop something that's not in your inventory.")
					return	
				if not self.user.current_place.roomHasThing(indirObj):
					Output.print_error("You don't see a " + indirObj + " here.")
					return
				if self.user.current_place.roomHasThing(indirObj):
					Output.print_error("You can't put things inside the {}.".format(indirObj)) 
					return

	#v11.7
	def handleListen(self, obj1, obj2, canListen):
		attemptedObj = obj1
		if not canListen:
			if attemptedObj == None:
				Output.print_error("You don't hear anything out of the ordinary here.")
				return
			if obj2 != None:
				attemptedObj = attemptedObj + " " + obj2	
			if self.user.current_place.roomHasThing(attemptedObj) or self.user.userHasThing(attemptedObj):
				Output.print_error("That's not something you can listen to.")
			else:
				Output.print_error("You don't see a {} to listen to here.".format(attemptedObj))
		else:
			currRoom = self.user.current_place
			# cycle through listen descriptions; when exhausted, start at first listen description
			if len(currRoom.listenDescrips) > 0:
				if len(currRoom.listenDescrips) > currRoom.numTimesListened:
					Output.print_look(currRoom.listenDescrips[currRoom.numTimesListened])
				else:
					currRoom.numTimesListened -= len(currRoom.listenDescrips)
					Output.print_look(currRoom.listenDescrips[currRoom.numTimesListened])
				currRoom.numTimesListened += 1

	# new in v9: print special error message for locked door
	def handleLockedDoor(self, direction):

		doors = self.user.current_place.doors

		# v11.1: fix "go to X" bug.
		if direction == None:
			Output.print_error("That's not somewhere you can go.")

		# if there is a door, and the move is invalid, then "locked"
		elif doors[direction] == "locked":
			Output.doorIsLocked(self.user.current_place.name, True)

		# otherwise, there is no place in that direction
		else:
			Output.print_error("There is no place in the " + direction + " direction")

	# v12 handling talking to characters
	def handleTalk(self, attemptedObj, canTalk):
		if canTalk:
			character = self.user.current_place.character
			if character.name.lower() == attemptedObj.lower():
				Output.print_talk(character.getCharacterSpeak(self.time), character.name)
				if character.name.lower() == "maude":
					self.user.hasMetMaude = True
				elif character.name.lower() == "dworkin":
					self.user.hasMetDworkin = True
				elif character.name.lower() == "mina":
					self.user.hasMetMina = True 
				return
			if attemptedObj.lower() in character.altNames:
				Output.print_talk(character.getCharacterSpeak(self.time), character.name)
				if character.name.lower() == "maude":
					self.user.hasMetMaude = True
				elif character.name.lower() == "dworkin":
					self.user.hasMetDworkin = True
				elif character.name.lower() == "mina":
					self.user.hasMetMina = True	 
				return
		else:
			Output.print_error("You cannot talk to " + attemptedObj)


	# v6: displays list of supported verbs
	def showHelp(self):
		Output.print_input_hint("go, move, run, walk, head, hurry")
		print()
		Output.print_input_hint("n, s, e, w, nw, ne, sw, se, u, d")
		Output.print_input_hint("north, south, east, west, northwest, northeast, southwest, southeast, up, down, upstairs, downstairs")
		print()
		Output.print_input_hint("get, pick up, take, grab, keep, steal, acquire, collect")
		print()
		Output.print_input_hint("drop, put down, abandon, discard, trash")
		Output.print_input_hint("insert, put in, put inside")
		print()
		Output.print_input_hint("look, l, look around")
		Output.print_input_hint("look at, examine, x, inspect, study, stare, gaze")
		Output.print_input_hint("search, look in, look inside")
		Output.print_input_hint("open")
		Output.print_input_hint("read")
		print()
		Output.print_input_hint("talk, say, greet, ask, chat, speak, tell, call")
		print()
		Output.print_input_hint("sleep, rest, relax, go to bed")
		print()
		Output.print_input_hint("help, inventory")

	# point of entry from parser, game takes care of input from this point
	# either by updating the game or sending error messages
	def fromParserToGame(self, action): 
	
		#v13.2: return cleanly if action is None
		if action == None:
			return
	
		valid = self.checkIsValid(action)

		if(valid):

			self.executeRequest(action)

			# update the list of valid moves in the new game state
			self.setIsValid()
			
			# if the user was moved, re-orient user
			if action.verb == "move_user":
				self.user.current_place.printRoom(self.time)
				self.user.current_place.updateNumEntries()
 
		else: 
			if action.verb == "move_user": 
				# if there's a direction that's invalid (and there are no other inputs)
				if action.direction != None and action.direct_obj == None and action.indirect_obj == None:
					self.handleLockedDoor(action.direction)
				# when the only input is "move"
				elif action.direction == None and action.direct_obj == None and action.indirect_obj == None:
					self.verbOnlyMove()
				# when the user tries to move things
				elif action.direct_obj != None or action.indirect_obj != None: 
					print("You can't move things unless they are objects you can pick up and carry with you.") 

			elif action.verb == "look":
				self.handleLook(action.direct_obj, action.indirect_obj, False)
			elif action.verb == "take":
				self.handleTake(action.direct_obj, action.indirect_obj, False) 
			elif action.verb == "move_user":
				Output.print_error("You can't move in that direction. Try another.")
			elif action.verb == "drop":
				self.handleDrop(action.direct_obj, action.indirect_obj, False)
			elif action.verb == "sleep":
				self.handleSleep(action.direct_obj, False)
			elif action.verb == "search":
				self.handleSearch(action.direct_obj, action.indirect_obj, False)
			elif action.verb == "read":
				self.handleRead(action.direct_obj, action.indirect_obj, False)
			elif action.verb == "insert":
				self.handleInsert(action.direct_obj, action.indirect_obj, False)
			elif action.verb == "listen":
				self.handleListen(action.direct_obj, action.indirect_obj, False)
			elif action.verb == None and action.direct_obj != None:
				self.handleSingularInput(action.direction, action.direct_obj, action.indirect_obj)
			elif action.verb == "leave" and action.direct_obj == None and action.indirect_obj == None:
				self.handleSingularInput(None, "leave", None)
			elif action.verb == "do_violence":
				self.handleViolence(action.direct_obj, action.indirect_obj, False)
			elif action.verb == "open_thing":
				self.handleOpen(action.direct_obj, action.indirect_obj, False)
			else:
				if action.direct_obj == None or action.verb == None:
					Output.print_error("You don't see the point of doing that right now.")
					return
				attempted = action.direct_obj 
				if action.indirect_obj != None: 
					attempted = attempted + " " + action.indirect_obj
				# thing is present, but action.verb doesn't work with the thing
				if self.user.canAccessThing(attempted): 
					Output.print_error("You can't " + action.verb + " the " + attempted + ". Try doing something else with it.")
					return
				else:
					Output.print_error("You don't see a {} that you can {}.".format(attempted, action.verb))
					return
				Output.print_error("You don't see the point of doing that right now.")

	# called after every change in game state in preparation for next input from parser
	def setIsValid(self):
		
		newdict={} 
		
		user_place = self.user.current_place
		
		adjacent_places = self.user.current_place.adjacent_places
   
		# create a list of available move locations
		# new in v9, update to account for locked opposing doors (if going north, check place north south door is not locked)
		valid_moves = []
		if adjacent_places[0] is not None:
			if adjacent_places[0].doors["s"] is not "locked":
				valid_moves.append("n")
		if adjacent_places[1] is not None: 
			if adjacent_places[1].doors["sw"] is not "locked":
				valid_moves.append("ne")
		if adjacent_places[2] is not None:
			if adjacent_places[2].doors["w"] is not "locked":
				valid_moves.append("e")
		if adjacent_places[3] is not None: 
			if adjacent_places[3].doors["nw"] is not "locked":
				valid_moves.append("se")
		if adjacent_places[4] is not None: 
			if adjacent_places[4].doors["n"] is not "locked":
				valid_moves.append("s")
		if adjacent_places[5] is not None: 
			if adjacent_places[5].doors["ne"] is not "locked":
				valid_moves.append("sw")
		if adjacent_places[6] is not None: 
			if adjacent_places[6].doors["e"] is not "locked":
				valid_moves.append("w")
		if adjacent_places[7] is not None: 
			if adjacent_places[7].doors["se"] is not "locked":
				valid_moves.append("nw")
		if adjacent_places[8] is not None: 
			if adjacent_places[8].doors["d"] is not "locked":
				valid_moves.append("u")
		if adjacent_places[9] is not None: 
			if adjacent_places[9].doors["u"] is not "locked":
				valid_moves.append("d")

		# v11.3: change from strings to objects 
		valid_takes = [item for item in user_place.things if item.is_takeable]
		valid_drops = [item for item in self.user.things]
		valid_looks = [item for item in user_place.things]
		for item in self.user.things:
			valid_looks.append(item)
	
		valid_searches = [item for item in user_place.things if item.is_searchable]
		valid_reads = [item for item in user_place.things if item.is_readable]
		for item in self.user.things:
			if item.is_readable:
				valid_reads.append(item)

		#v13.3
		valid_opens = [item for item in user_place.things if item.is_openable]

		# v12 add a character to the list of things to look at and talk with
		valid_talks = []
		if user_place.hasCharacter: 
			valid_looks.append(user_place.character) # character is a Thing obj
			valid_talks.append(user_place.character) # you can also talk to characters

		# set the dictionary with keys as actions and values as valid corresponding things
		newdict = {"move_user": valid_moves, "take": valid_takes, "drop": valid_drops, "look": valid_looks, "search": valid_searches, "read": valid_reads, "talk_npc": valid_talks, "open_thing": valid_opens}

		# set the "is valid" attribute to the current dictionary of valid game operations
		self.isValid = newdict

	# take action object and consult "isValid" dictionary 
	def checkIsValid(self, action): 
		if action.verb == "move_user":
			v = self.isValid.get("move_user")
			for i in v:
				if i == action.direction:
					return True
			return False
		elif action.verb == "take":
			# v7: make sure direct_obj is not None to avoid crash 
			if action.direct_obj == None:
				return False
			v = self.isValid.get("take")
			for i in v:
				#v11.3: check for alternate thing names
				if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
					return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True
			# new in v4: case where item is takeable but already in inventory
			if self.user.userHasThing(action.direct_obj):
				return True
			# v7
			if action.indirect_obj != None:
				objName = action.direct_obj + " " + action.indirect_obj
				if self.user.userHasThing(objName): 
					return True 
			return False
		elif action.verb == "drop":
			if action.direct_obj == None:
				return False
			v = self.isValid.get("drop")
			for i in v:
				#v11.3: check for alternate thing names 
				if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
					return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True 
			return False

		# new in v3
		elif action.verb == "look":
			v = self.isValid.get("look")
			# check if specified object can be examined (is in current place or inventory)
			for i in v:
				if action.direct_obj != None:
					#v11.3: check for alternate thing names
					if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
                                		return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True
			# if no object specified or current room specified, examine room
			if action.direct_obj == None:
                        	return True
			if action.direct_obj == "room":
                        	return True
			if action.direct_obj == self.user.current_place.name.lower(): 
                        	return True

			#v13.3 handle "look outside"
			if action.direct_obj == "outside" and action.indirect_obj == None:
				# check for a window in the room
				for i in v:
					if i.is_window:
						return True
				return False

			return False

		# new in v4 
		elif action.verb == "sleep":
			# can only sleep on bed in Spare Room at night
			correctRoom = (self.user.current_place.name == "Spare Room")
			correctObj = (action.direct_obj == None or action.direct_obj == "bed")
			correctTime = (self.time >= 25 or self.time <= 5)
			if correctRoom and (correctObj and correctTime):
				return True
			else:
				return False

		# new in v6
		elif action.verb == "show_help":
			return True 
		elif action.verb == "show_inventory":
			return True

		# new in v11.1
		elif action.verb == "search":
			if action.direct_obj == None:
				return False
			v = self.isValid.get("search")
			for i in v:
				#v11.3: check for alternate thing names
				if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
					return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True

		elif action.verb == "read":
			if action.direct_obj == None:
				return False
			v = self.isValid.get("read")
			for i in v:
				#v11.3: check for alternate thing names
				if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
					return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True
		# v11.6
		elif action.verb == "insert":
			if action.direct_obj == None or action.indirect_obj == None:
				return False
			v = self.isValid.get("search")
			d = self.isValid.get("drop")
			whereToPut = None
			whatToPut = None
			for feat in v:
				if feat.name.lower() == action.indirect_obj or action.indirect_obj in feat.altNames:
					whereToPut = feat
			for o in d:
				if o.name.lower() == action.direct_obj or action.direct_obj in o.altNames:
					whatToPut = o
			if whereToPut == None or whatToPut == None:
				return False
			return True
		#v11.7
		elif action.verb == "listen":
			if self.user.current_place.name == "Drawing Room" and (self.day == 2 or self.day == 3):
				return True
			return False
		# v12 talking to things (characters)
		elif action.verb == "talk_npc":
			v = self.isValid.get("talk_npc")
			for i in v:
				if action.direct_obj != None:
					if i.name.lower() == action.direct_obj:
						return True
					elif action.direct_obj in i.altNames:
						return True
		#v13.2. TODO: to be expanded later
		elif action.verb == "do_violence":
			return False 
		#v13.3 
		elif action.verb == "open_thing":
			if action.direct_obj == None:
				return False
			v = self.isValid.get("open_thing")
			for i in v:
				if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
					return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True
		else:
			return False	

	# Precondition: called after checkIsValid() returns True
	def executeRequest(self, action):
		if action.verb == "move_user":
			self.moveUser(action.direction)
			self.updateTime(1)
			return

		if action.verb == "take":
			# v4: error handling
			self.handleTake(action.direct_obj, action.indirect_obj, True)
			# v7: two-word object names
			if action.indirect_obj != None:
				obj_name = action.direct_obj + " " + action.indirect_obj
			else:
				obj_name = action.direct_obj
			self.user.pickUpObject(obj_name)

			# time update of 1 hour 
			self.updateTime(1)
			return

		if action.verb == "drop":
			self.handleDrop(action.direct_obj, action.indirect_obj, True)
			if action.indirect_obj != None:
				obj_name = action.direct_obj + " " + action.indirect_obj
			else:
				obj_name = action.direct_obj
			self.user.dropObject(obj_name)
			# add a time update
			self.updateTime(1)
			return

		# updated to handle two-word object names 
		if action.verb == "look":
			self.handleLook(action.direct_obj, action.indirect_obj, True)
			self.updateTime(1)
			return

		if action.verb == "sleep":
			self.handleSleep(action.direct_obj, True)
			Output.print_look("Drained from the day's activity, you shuck off your things and burrow under the covers. You're asleep by the time your head hits the pillow.")
			# start new morning 
			self.time = 6
			self.day += 1
			# v11.4: wakeup message
			Output.print_look("Start of Day {}".format(self.day))
			Output.print_look("You awake to morning light streaming softly into the room. The House is still and silent around you as you climb out of bed, walking gingerly on frigid floorboards.")
			return
		# don't increment time for help/inventory
		# since these are not "in-game" actions 
		if action.verb == "show_help":
			self.showHelp()
			return
		if action.verb == "talk_npc":
			self.handleTalk(action.direct_obj, True)
			self.updateTime(1)
			return 
		if action.verb == "show_inventory":
			self.user.printInventory()
			return
		if action.verb == "search":
			self.handleSearch(action.direct_obj, action.indirect_obj, True)
			self.updateTime(1)
			return
		if action.verb == "read":
			self.handleRead(action.direct_obj, action.indirect_obj, True)
			self.updateTime(1)
			return
		if action.verb == "insert":
			self.handleInsert(action.direct_obj, action.indirect_obj, True)
			self.user.insertObject(action.direct_obj, action.indirect_obj)
			self.updateTime(1)
			return
		if action.verb == "listen":
			self.handleListen(action.direct_obj, action.indirect_obj, True)
			self.updateTime(1)
			return
		if action.verb == "do_violence":
			self.handleViolence(action.direct_obj, action.indirect_obj, True)
			self.updateTime(1)
			return
		if action.verb == "open_thing":
			self.handleOpen(action.direct_obj, action.indirect_obj, True)
			self.updateTime(1)
			return
		else:
			return

	# Precondition: place adjacency pre-validated
	# new in v9: it has also been verified that if there is a door, it is not locked
	def moveUser(self, direction):
		user_place = self.user.current_place
		adjacent_places = user_place.adjacent_places
		is_door = False

		#v13.2: restrict movement until after speaking to Maude
		if user_place.name.lower() == "train platform" and self.user.hasMetMaude == False:
			Output.print_talk("The stern woman on the platform stops you.#Just where do you think you're going without greeting your elders?#", "Maude")
			return

		if direction == "n":
			self.user.updatePlace(adjacent_places[0])
			if adjacent_places[0].doors["s"] == "unlocked":
				is_door = True
		elif direction == "ne":
			self.user.updatePlace(adjacent_places[1])
			if adjacent_places[1].doors["sw"] == "unlocked":
				is_door = True
		elif direction == "e":
			self.user.updatePlace(adjacent_places[2])
			if adjacent_places[2].doors["w"] == "unlocked":
				is_door = True
		elif direction == "se":
			self.user.updatePlace(adjacent_places[3])
			if adjacent_places[3].doors["nw"] == "unlocked":
				is_door = True
		elif direction == "s":
			self.user.updatePlace(adjacent_places[4])
			if adjacent_places[4].doors["n"] == "unlocked":
				is_door = True
		elif direction == "sw":
			self.user.updatePlace(adjacent_places[5])
			if adjacent_places[5].doors["ne"] == "unlocked":
				is_door = True
		elif direction == "w":
			self.user.updatePlace(adjacent_places[6])
			if adjacent_places[6].doors["e"] == "unlocked":
				is_door = True
		elif direction == "nw":
			self.user.updatePlace(adjacent_places[7])
			if adjacent_places[7].doors["se"] == "unlocked":
				is_door = True
		elif direction == "u":
			self.user.updatePlace(adjacent_places[8])
			if adjacent_places[8].doors["d"] == "unlocked":
				is_door = True
		elif direction == "d":
			self.user.updatePlace(adjacent_places[9])
			if adjacent_places[9].doors["u"] == "unlocked":
				is_door = True

		# new in v9
		# print door animation if there is a door
		new_place = self.user.current_place

		#v11.7 make Fields take longer to cross
		if user_place.name.lower() == "fields" and new_place.name.lower() != "fields":
			self.updateTime(3)

		# exit msg from Front Manor Grounds to Foyer
		# only shows up on first entry into foyer
		if new_place.numTimesEntered == 0 and (user_place.name.lower() == "front manor grounds" and new_place.name.lower() == "foyer"):
			Output.print_look("You hurl yourself up the path as it starts to rain in earnest. Maude follows right on your heels, fishing an iron keyring out of her pockets. At the front door, she shoulders you aside, unlocks the door, and heaves it open with a grunt of effort, dragging you inside by the wrist and dumping you in a rain-soaked heap on the floor.")

			# 13.1: lock front door of house once user is inside foyer
			# (lock north door of front manor grounds, lock south door of foyer) 
			user_place.lockDoor("n")
			new_place.lockDoor("s") 
	
		# 13.1: exit message from Train Platform to Fields
		# only shows up on first entry into fields
		if new_place.numTimesEntered == 0 and (user_place.name.lower() == "train platform" and new_place.name.lower() == "fields"): 
			Output.print_look("Leaving the station behind, you trail doggedly after Maude, who doesn't spare so much as a backward glance. You mechanically put one foot in front of another, resigning yourself to what already feels like a long journey to the House.")
	
		if (is_door):
			Output.newPlaceWithDoor(new_place.name)
		else: # not a door
			return
			# print("You move to the " + new_place.name)

# define the "Place" class
class Place:
	# game(game object), name(string), day[], night[], adjacentPaceNames[10 strings], things[strings], doors{ })
	def __init__(self, game, name, day, night, adjacentPlaceNames, things = None, doors = None, passages = None):
		self.name = name
		self.adjacent_place_names = adjacentPlaceNames 

		#v11.5: list of items dropped in this place 
		# (separate handling for items dropped inside features) 
		self.droppedHere = []
		#v11.7: list of "listen" descriptions
		self.listenDescrips = [] 
		self.numTimesListened = 0

		# new in v9: a dictionary of doors tracking: whether there is a door, and whether it is locked or unlocked
		# dictionary: key is direction, value is either 'locked', 'unlocked', or None
		self.doors = doors

		# new in v14 special passages in a dictionary
		# eg. {"ne": "archway"}
		# look up passage type
		# used for printing but also for special handling of input ex user input only "archway" or "wooden door"
		self.passages = passages

		if things is not None:
			self.things = things
		else:
			self.things = []
		
		self.numTimesEntered = -1
		self.numTimesLooked = -1	

		# v11 day and night are arrays with different values based on "userVisitCount"
		self.day = day
		self.night = night

		game.addPlace(self) # creates a map between name and place object in the game

		# v12 characters as part of places
		self.character = None
		self.hasCharacter = False

	# new in v9 update the doors dictionary when a door becomes locked
	def lockDoor(self, direction):
		self.doors[direction] = "locked"

	# new in v9 update the doors dictionary when a door becomes unlocked
	def unlockDoor(self, direction):
		self.doors[direction] = "unlocked"

	#  translates array to "adjacentplaces" array after all places created
	def setAdjacentPlaces(self, game):
		self.adjacent_places = list(map(game.getPlace, self.adjacent_place_names))

	# v14 track passage types in a dictionary i.e. archway
	def setPassages(self, passages):
		self.passages = passages

	# v11 return a description that also considers the how many times the user has been there
	def getDescriptionBasedOnTimeAndVisitCount(self, time): 
		# v7: longer clock (40 hours) to allow more moves per day 
		uvc = self.numTimesEntered
		if uvc == -1:
			uvc = 0
		if uvc > 2:
			uvc = 2
		if time > 5 and time < 25: 
			return self.day[uvc]
		else:
			return self.night[uvc]
	
	# new in v2 (correpond to take and drop)
	def addThing(self, thing):
		self.things.append(thing)

	# v12 adding character to place
	def addCharacter(self, thing):
		self.character = thing
		self.hasCharacter = True

	def removeThing(self, thing):
		self.things.remove(thing)

	# check if a thing is in a room
	def roomHasThing(self, itemname):
		for t in self.things:
			# v11.2: check for alternate thing names
			if t.name.lower() == itemname or itemname in t.altNames: 
				return True
		return False	

	# v5: updates number of times examined
	def updateNumLooks(self):
		self.numTimesLooked += 1

	# v5: update number of entries
	def updateNumEntries(self):
		self.numTimesEntered += 1

	# v5: display room description
	def printRoom(self, time):
		place_name = self.name
		place_description = self.getDescriptionBasedOnTimeAndVisitCount(time)
		# v9: call output function to orient user 
		Output.orientUser(place_name, place_description)
		# v11.5: show any dropped objects currently in the room
		# (don't show objects that were dropped inside features)
		features = [feat for feat in self.things if feat.is_searchable]
		hiddenItems = []
		for ft in features:
			for hidden in ft.hasOtherItems:
				hiddenItems.append(hidden) 
		for i in self.droppedHere:
			if i.name not in hiddenItems: 
				Output.print_look(i.isHereDescription)

# define the User class
class User:
	# game(game object), name(string), place name (string), user direction(string), saved game(bool) 
	def __init__(self, game, name, startingPlace, startingDirection, saved):
		if saved == False:
			self.name = name
			self.current_place = game.getPlace(startingPlace)
			self.direction = startingDirection
			self.hasMetMaude = False
			self.hasMetMina = False
			self.hasMetDworkin = False
			self.foundStudyKey = False

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
	def pickUpObject(self, thing_name):
		# EDIT get actual thing obj reference 
		room_things = self.current_place.things
		for t in room_things:
			# v11.3: check for alternate thing names
			if t.name == thing_name or thing_name in t.altNames:
				thing = t
				# v4: only add to inventory if not already in it
				if self.userHasThing(thing.name) == False: 
					# add to user array
					self.things.append(thing)
					# remove the thing from the Place it is in
					self.current_place.removeThing(thing)
					# v11.5: remove from place's droppedHere list, if present
					for i in self.current_place.droppedHere:
						if thing.name == i.name:
							r = i 
							self.current_place.droppedHere.remove(r)
					# v11.5: remove from feature's hasOtherItems list, if present
					for feat in self.current_place.things:
						if thing.name in feat.hasOtherItems:
							feat.hasOtherItems.remove(thing.name)	

	# new in v2
	def dropObject(self, thing_name):
		# EDIT get actual thing obj reference, only remove if user has
		if self.userHasThing(thing_name):
			for t in self.things:
				# v11.3: check for alternate thing names
				if t.name == thing_name or thing_name in t.altNames:
					thing = t
					# remove from user array
					self.things.remove(thing)
					# add thing to the place the user is in
					self.current_place.addThing(thing)
					# v11.5: add thing to the place's droppedHere list
					self.current_place.droppedHere.append(thing)
					break

	# v11.6: implement dropping objects inside searchable features (e.g. trunk, wardrobe) 
	def insertObject(self, thingToDrop, thingToContain):
		print("dropping obj inside other obj")
		self.dropObject(thingToDrop)
		dropped = None
		for i in self.current_place.things:
			if i.name == thingToDrop or thingToDrop in i.altNames:
				dropped = i
		if dropped == None:
			return
		for t in self.current_place.things:
			if t.name == thingToContain or thingToContain in t.altNames:
				containerThing = t
				if containerThing.is_searchable and not containerThing.is_takeable:
					containerThing.hasOtherItems.append(dropped.name)  

	# new in v2, for figuring out if user has an thing in possession
	def userHasThing(self, itemname):
		found = False
		for t in self.things:
			# v11.3: check for alternate thing names 
			if t.name.lower() == itemname or itemname in t.altNames: 
				found = True
		return found

	def updatePlace(self, place):
		self.current_place = place
		# new in v11: num times entered
		self.current_place.updateNumEntries()

	def printUser(self, game):
		print("Username: " + self.name + " Current place: " + self.current_place.name)

	# v5: check if user can access a thing 
	def canAccessThing(self, itemname):
		if self.userHasThing(itemname) or self.current_place.roomHasThing(itemname):
			return True
		return False		

	# v5: check if user can perform a particular action on a thing 
	def canActOnThing(self, itemname, verb):
		if not self.canAccessThing(itemname):
			return False
		else:
			for t in self.things:
				#v11.3: check for alternate thing names
				if t.name == itemname or itemname in t.altNames:
					if verb in t.permittedVerbs:
						return True
			for t in self.current_place.things:
				if t.name == itemname or itemname in t.altNames:
					if verb in t.permittedVerbs:
						return True
			return False 

	# v6: show inventory contents
	def printInventory(self):
                if len(self.things) == 0:
                        Output.print_input_hint("You currently have nothing in your inventory.")
                else:
                	Output.print_input_hint("You have, in various locations on your person:")
                	for t in self.things:
                        	Output.print_input_hint(t.name)

	def getAllThingsInPlace(self):
		return self.things

#define the "Thing" class
class Thing: 
	def __init__(self, name, day, night, starting_location, is_takeable, is_character = False, char_day = None, char_night = None):
		self.name = name
		self.day = day     # size of 5
		self.night = night # size of 5
		self.location = starting_location # place object
		self.is_takeable = is_takeable # defines whether feature or object
		self.with_user = False
		# v11.1
		self.is_searchable = False
		self.is_readable = False
		self.hasBeenSearched = False
		# v13.1: start implementing open (for openable things like windows) 
		# (if an item is both openable and searchable, e.g. trunk, default to searching)  
		self.is_openable = False
		self.openDescrip = "" 

		# v11.2
		self.isHereDescription = "You see a " + self.name + " here."
 
		# v11.2: for things that have other things on/in them
		self.hasOtherItems = []
		# v11.3: alternate names for items
		self.altNames = [] 

		# v12 things can now be characters 
		self.is_character = is_character
		# set the day and night dialogue of the character
		if is_character:
			print(self.name)
			self.char_day = char_day
			self.char_night = char_night

		#v11.4: search/read descriptions for searchable/readable items
		self.searchDescrip = "" 
		self.readDescrips = []
		#v13.3
		self.windowDescrips = [] 
		self.is_window = False

		# keep track of allowed verbs for each thing
		self.permittedVerbs = [] 

		self.numTimesRead = 0
		self.numTimesExamined = -1 # start at -1 to account for "+1" at beginning of getDescription/array indexing
		self.numTimesTalked = -1

	def getDescription(self, time):
		self.numTimesExamined += 1
		if time > 5 and time < 25:					# do we want this time of 5 - 25 here?
			if self.numTimesExamined > 5:
				return self.day[4]
			else:
				return self.day[self.numTimesExamined]
		else:
			if self.numTimesExamined > 5:
				return self.night[4]
			else:
				return self.night[self.numTimesExamined]

	# add a permitted verb for this thing 
	def addVerb(self, verb):
		self.permittedVerbs.append(verb)

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

	# differentiate character from object or feature
	def isCharacter(self):
		return self.is_character

	# get the character's dialogue based on time of day and num of times talked prior
	# characters have up to 5 different things to say in the day and night, and after that just say the last thing
	def getCharacterSpeak(self, time):
		self.numTimesTalked += 1
		if time > 5 and time < 25:
			if self.numTimesTalked > 5:
				return self.char_day[4]
			else:
				return self.char_day[self.numTimesTalked]
		else:
			if self.numTimesTalked > 5:
				return self.char_night[4]
			else:
				return self.char_night[self.numTimesTalked]

	# edit description
	def editDescription(self, day, night):
		self.day = day
		self.night = night



