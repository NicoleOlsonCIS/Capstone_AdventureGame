from action import Action

class Parser:

    # Class variables
    verbDict = {
        "go": "move_user",
        "move": "move_user",
        "run": "move_user",
        "walk": "move_user",
        "head": "move_user",
        "hurry": "move_user",
        "take": "take",
        "grab": "take",
        "get": "take",
        "pick": "take",
        "keep": "take",
        "stow": "take",
        "steal": "take",
        "drop": "drop", 
        "abandon": "drop",
        "discard": "drop",
        "trash": "drop",
        "put": "drop",
        "place": "drop",
        "insert": "insert", 
        "sleep": "sleep",
        "rest": "sleep",
        "relax": "sleep",
        "talk": "talk_npc",
        "say": "talk_npc",
        "greet": "talk_npc",
        "ask": "talk_npc",
        "yell": "talk_npc",
        "scream": "talk_npc",
        "shout": "talk_npc",
        "tell": "talk_npc",
        "call": "talk_npc",
        "chat": "talk_npc",
        "speak": "talk_npc",
        "look": "look",
        "examine": "look",
        "x": "look",
        "l": "look",
        "study": "look",
        "find": "look",
        "touch": "look",
        "look_in": "search",
        "search": "search", 
        "read": "read",
        "listen": "listen",
        "eavesdrop": "listen",
        "hear": "listen", 
        "open": "open_thing",
        "unlock": "unlock_thing",
        "help": "show_help",
        "inventory": "show_inventory",
        "save": "save_game",
        "load": "load_game"
    }

    directionDict = {
        "north": "n",
        "n": "n",
        "east": "e",
        "e": "e",
        "northeast": "ne",
        "ne": "ne",
        "south": "s",
        "s": "s",
        "west": "w",
        "w": "w",
        "northwest": "nw",
        "nw": "nw",
        "southeast": "se",
        "se": "se",
        "southwest": "sw",
        "sw": "sw", 
        "up": "u",
        "upstairs": "u",
        "u": "u",
        "down": "d",
        "downstairs": "d",
        "d": "d"
    }

    articlesList = ["the", "an", "a"]

    pronounsList = ["that", "her", "it", "she", "he", "him", "his", "hers", "they", "them", "their",
                    "you", "your", "yours", "me", "my", "mine", "myself", "yourself", "himself", "herself",
                    "its", "itself", "we", "our", "ours", "ourselves", "yourselves", "theirs", "themselves",
                    "this", "these", "those"]

    conjunctionsList = ["and", "or", "nor", "but", "yet", "so", "whether", "neither", "either", "though", "although", "because", "while"] 

    quantifiersList = ["all", "some", "few", "many", "several", "both", "every", "each", "first", "last", "next", "other", "same"]

    # Two different kinds of prepositions...
    # ...those recognized by the game
    prepositionsListUnused = [
        "about", "above", "across", "after", "against", "along", "among", "around", "at",
        "before", "behind", "below", "beneath", "beside", "between", "by",
        "for", "from", "near", "of", "off", "on", "onto",
        "through", "to", "toward", "towards", "under", "upon", "with", "within",
        "out"
    ] # removed 'down' - otherwise direction 'down' will be removed as preposition
    # ...and those that are not
    prepositionsListUsed = [
        "in", "inside", "into"
    ] # removed 'down' - otherwise direction 'down' will be removed as preposition

    hardcodedPhrases = {
        "go to bed": Action("sleep")
    }

    # Default constructor - no instance variables

    # Count how many verbs in tokens
    def verbCount(self, tokens):
        numverbs = 0
        for token in tokens:
            if token in self.verbDict.keys():
                numverbs += 1
        return numverbs 

    # Count how many directions in tokens
    def directionCount(self, tokens):
        numdirections = 0
        for token in tokens:
            if token in self.directionDict.keys():
                numdirections += 1 
        return numdirections

    # Count how many usable prepositions in tokens
    def prepositionCount(self, tokens):
        numPrepositions = 0
        for token in tokens:
            if token in self.prepositionsListUsed:
                numPrepositions += 1 
        return numPrepositions

    # Parse user input into action object
    # TODO - add "context" parameter so engine can talk *to* parser?
    def parseInput(self, userInput):

        # Convert input to lowercase
        userInput = userInput.lower()

        # Check if input is a hard-coded phrase
        userAction = self.parseHardCodePhrases(userInput)
        if (userAction is not None):
            return userAction

        # Tokenize input 
        tokens = userInput.split()

        # Remove articles 
        tokens = [token for token in tokens if token not in self.articlesList]
        # Remove quantifiers 
        tokens = [token for token in tokens if token not in self.quantifiersList] 
        # Remove pronouns
        tokens = [token for token in tokens if token not in self.pronounsList] 
        # Remove conjunctions
        tokens = [token for token in tokens if token not in self.conjunctionsList] 
        # Remove prepositions
        tokens = [token for token in tokens if token not in self.prepositionsListUnused]

        # Combine directions
        tokens = self.combineDirections(tokens)

        # Parse input depending on number of tokens
        # There must be at least one token after stripping
        if len(tokens) < 1:
            return Action() 

        elif len(tokens) is 1:
            return self.parseSingleToken(tokens[0])

        elif len(tokens) is 2:
            return self.parseTwoTokens(tokens)
        else:
            return self.parseThreeOrMoreTokens(tokens)

    # Convert user verb to valid form, return None on error
    def parseVerb(self, verb):
        # Special case for 'pick up'
        # if (len(tokens) > 1 and tokens[0] == "pick" and tokens[1] == "up"):
        #     del tokens[1]
        #     return "take"
        # else:
        #     return self.verbDict.get(tokens[0])
        return self.verbDict.get(verb)

    # Convert user-desired direction to valid form, return None on error
    def parseDirection(self, direction):
        return self.directionDict.get(direction)

    def parseHardCodePhrases(self, userInput):
        return self.hardcodedPhrases.get(userInput)

    # Return Action from single token input
    def parseSingleToken(self, token):
        if (token in self.directionDict):
            return Action("move_user", self.parseDirection(token))
        elif (token in self.verbDict):
            return Action(self.parseVerb(token))
        else:
            return Action(None, None, token) 
    
    # Return Action from two token input
    def parseTwoTokens(self, tokens):
        # there should not be more than one verb in tokens. return empty action if 2+ verbs
        verbct = self.verbCount(tokens)
        if verbct > 1:
            return Action()

        # There should not be more than one preposition in tokens.
        prepct = self.prepositionCount(tokens)
        if prepct > 1:
            return Action()

        # there should not be more than one direction in tokens. return empty action if 2+ directions
        directionct = self.directionCount(tokens)
        if directionct > 1:
            return Action()

        # calculate number of objects in tokens
        objct = 2 - verbct - directionct - prepct
        # if 2 objects and 2 tokens, that means both tokens are objs
        if objct is 2:
            return Action(None, None, tokens[0], tokens[1])
        # 1 obj in tokens, so other token is a verb or direction
        elif objct is 1:
            verb = None
            direction = None
            directObj = None
            # check if first token is a verb or direction
            verb1 = self.parseVerb(tokens[0])
            direction1 = self.parseDirection(tokens[0])
            # check if second token is a verb or direction
            verb2 = self.parseVerb(tokens[1]) 
            direction2 = self.parseDirection(tokens[1])

            # populate action correctly

            # first token is verb, so second token is obj
            if verb1 != None:
                verb = verb1
                directObj = tokens[1]
            # second token is verb, so first token is obj
            elif verb2 != None:
                verb = verb2
                directObj = tokens[0]
            
            # 1st token is direction, so 2nd token is obj 
            if direction1 != None:
                direction = direction1
                directObj = tokens[1]
            # 2nd token is direction so 1st token is obj 
            elif direction2 != None:
                direction = direction2 
                directObj = tokens[0]
            
            return Action(verb, direction, directObj, None)

        # 0 objs in token, so there is 1 verb and either 1 direction or prep
        else:  
            if (prepct is 0):
                verb = self.parseVerb(tokens[0])
                direction = None
                # first token is verb "move_user", 2nd token is direction  
                if (verb is "move_user"):
                    direction = self.parseDirection(tokens[1])
                    return Action(verb, direction, None, None)
                # first token is verb other than "move_user", ignore direction
                else:
                    return Action(verb, None, None, None) 
            else:
                verb = self.parseVerb(tokens[0])
                # Only used prepositions are to put things inside something else
                if (verb is "drop"):
                    verb = "insert"
                elif (verb is "look"):
                    verb = "search"
                # Return action with modified verb
                return Action(verb, None, None, None)

    def parseThreeOrMoreTokens(self, tokens):
        action = self.parseTwoTokens(tokens[:2])    # parse first two tokens
        if (action.verb is None):                        # check if invalid
            return action 

        # FIXME: come up with something more robust than this?
        nextTokenPos = 2
        if (tokens[nextTokenPos] in self.prepositionsListUsed):
            if (action.verb is "drop"):
                action.verb = "insert"
            elif (action.verb is "look"):
                action.verb = "search"
            del tokens[nextTokenPos]

        if (action.direct_obj is None):
            action.direct_obj = tokens[nextTokenPos]
        else:
            action.indirect_obj = tokens[nextTokenPos]

        # Return action
        return action

    # Combines all directions in a user's input into one string
    def combineDirections(self, tokens):
        index = -1
        for i, token in enumerate(tokens):
            if token in self.directionDict.keys():
                if (index < 0):
                    index = i
                else:
                    tokens[index] += token
                    tokens.remove(token)
        return tokens

# Debug
# parser = Parser()
# parser.parseInput("insert foo in bar")
