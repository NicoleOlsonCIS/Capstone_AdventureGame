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
        "get": "take",
        "pick": "take", 
        "keep": "take",
        "take": "take",
        "grab": "take",
        "steal": "take",
        "drop": "drop", 
        "abandon": "drop",
        "discard": "drop",
        "trash": "drop",
        "put": "drop",
        "insert": "drop_inside_thing",
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
        "read": "look",
        "find": "look",
        "touch": "look",
        "look_in": "search",
        "search": "search", 
        "open": "open_thing",
        "unlock": "unlock_thing",
        "help": "show_help",
        "inventory": "show_inventory",
        "save": "save_game",
        "load": "load_game"
    }

    directionDict = {
        "north": "north",
        "n": "north",
        "east": "east",
        "e": "east",
        "south": "south",
        "s": "south",
        "west": "west",
        "w": "west",
        "northeast": "northeast",
        "ne": "northeast",
        "northwest": "northwest",
        "nw": "northwest",
        "se": "southeast",
        "southeast": "southeast",
        "sw": "southwest",
        "southwest": "southwest",
        "up": "up",
        "down": "down",
        "u": "up",
        "d": "down" 
    }

    articlesList = ["the", "an", "a"]

    pronounsList = ["that", "her", "it", "she", "he", "him", "his", "hers", "they", "them", "their",
                    "you", "your", "yours", "me", "my", "mine", "myself", "yourself", "himself", "herself",
                    "its", "itself", "we", "our", "ours", "ourselves", "yourselves", "theirs", "themselves",
                    "this", "these", "those"]

    conjunctionsList = ["and", "or", "nor", "but", "yet", "so", "whether", "neither", "either", "though", "although", "because", "while"] 

    quantifiersList = ["all", "some", "few", "many", "several", "both", "every", "each", "first", "last", "next", "other", "same"]

    prepositionsList = [
        "about", "above", "across", "after", "against", "along", "among", "around", "at",
        "before", "behind", "below", "beneath", "beside", "between", "beyond", "by",
        "for", "from", "in", "inside", "into", "near", "of", "off", "on", "onto", "out", "outside",
        "over", "past", "through", "to", "toward", "towards", "under", "upon", "with", "within"
    ]

    # Default constructor - no instance variables

    # Count how many verbs in tokens
    def verbCount(self, tokens):
        numverbs = 0
        for token in tokens:
            if token in verbDict.keys():
                numverbs += 1
        return numverbs 

    # Count how many directions in tokens
    def directionCount(self, tokens):
        numdirections = 0
        for token in tokens:
            if token in directionDict.keys():
                numdirections += 1 
        return numdirections


    # Parse user input into action object
    # TODO - add "context" parameter so engine can talk *to* parser?
    def parseInput(self, input):

        # Convert input to lowercase
        input = input.lower()

        # Tokenize input 
        tokens = input.split()

        # Remove articles 
        tokens = [token for token in tokens if token not in self.articlesList]
        # Remove quantifiers 
        tokens = [token for token in tokens if token not in self.quantifiersList] 
        # Remove pronouns
        tokens = [token for token in tokens if token not in self.pronounsList] 
        # Remove conjunctions
        tokens = [token for token in tokens if token not in self.conjunctionsList] 
        # Remove prepositions
        tokens = [token for token in tokens if token not in self.prepositionsList]

        # There must be at least one token after stripping
        if len(tokens) < 1:
            return Action() # return action with None verb, direction, direct obj to engine 

        elif len(tokens) == 1:
            # if only one token, see if it is a verb, direction, or direct obj
            verb = self.parseVerb(tokens[0])
            direction = self.parseDirection(tokens[0]) 
            directObj = None 
            # if it is not an available verb or direction, assume it is a direct obj  
            # TODO: (may want to expand this later to check a text file of common English verbs.
                # that way if a word is a verb, just unavailable in the game, we can detect that.)  
            if verb == None and direction == None:
                directObj = tokens[0]
            return Action(verb, direction, directObj)  

        elif len(tokens) == 2:
            # there should not be more than one verb in tokens. return empty action if 2+ verbs
            verbct = self.verbCount(tokens)
            if verbct > 1:
                return Action()
            # there should not be more than one direction in tokens. return empty action if 2+ directions
            directionct = self.directionCount(tokens)
            if directionct > 1:
                return Action()

            # calculate number of objects in tokens
            objct = 2 - verbct - directionct 
            # if 2 objects and 2 tokens, that means both tokens are objs
            if objct == 2:
                return Action(None, None, tokens[0], tokens[1])
            # 1 obj in tokens, so other token is a verb or direction
            elif objct == 1:
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
 
            # 0 objs in token, so there is 1 verb and 1 direction    
            else:  
                verb = self.parseVerb(tokens[0])
                direction = None
                # first token is verb, 2nd token is direction  
                if verb != None:
                    direction = self.parseDirection(tokens[1])
                # 1st token is direction, 2nd is verb
                else:
                    direction = self.parseDirection(tokens[0])
                    verb = self.parseVerb(tokens[1]) 
                return Action(verb, direction, None, None) 

        else:
            # TODO: will need some extra handling if 3+ tokens 
            return Action()


    # Convert user verb to valid form, return None on error
    def parseVerb(self, verb):
        return self.verbDict.get(verb)

    # Convert user-desired direction to valid form, return None on error
    def parseDirection(self, direction):
        return self.directionDict.get(direction)
