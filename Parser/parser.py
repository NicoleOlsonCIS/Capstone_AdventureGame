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
        "stow": "take",
        "take": "take",
        "grab": "take",
        "steal": "take",
        "drop": "drop", 
        "leave": "drop",
        "abandon": "drop",
        "discard": "drop",
        "trash": "drop",
        "sleep": "sleep",
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
        "touch": "look",
        "find": "look",
        "open": "open",
        "unlock": "unlock",
        "help": "show_help",
        "inventory": "show_inventory",
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

    quantifiersList = ["all", "some", "few", "many", "little", "several", "both", "every", "each", "first", "last", "next", "other", "same"]

    prepositionsList = [
        "about", "above", "across", "after", "against", "along", "among", "around", "at",
        "before", "behind", "below", "beneath", "beside", "between", "by",
        "down", "for", "from", "in", "inside", "into", "near", "of", "off", "on", "onto",
        "through", "to", "toward", "towards", "under", "upon", "with", "within"
    ]

    # Default constructor - no instance variables

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
            # check first token for a verb 
            verb = self.parseVerb(tokens[0])
            # check second token for a direction 
            direction = self.parseDirection(tokens[1])
            directObj = None
            # if second token is not a direction, assume it is a direct obj
            if direction == None:
                directObj = tokens[1] 
            return Action(verb, direction, directObj)

        else:
            # TODO: will need some extra handling if 3+ tokens 
            return Action()


    # Convert user verb to valid form, return None on error
    def parseVerb(self, verb):
        return self.verbDict.get(verb)

    # Convert user-desired direction to valid form, return None on error
    def parseDirection(self, direction):
        return self.directionDict.get(direction)
