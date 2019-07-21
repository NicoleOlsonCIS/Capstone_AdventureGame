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
        "north": "n",
        "n": "n",
        "east": "e",
        "e": "e",
        "right": "e",
        "south": "s",
        "s": "s",
        "west": "w",
        "w": "w",
        "left": "w",
        "up": "u",
        "upstairs": "u",
        "u": "u",
        "down": "d",
        "downstairs": "d",
        "d": "d"
    }

    articlesList = ["the", "an", "a"]

    quantifiersList = ["all", "some", "few", "many", "little", "several", "both", "every", "each", "first", "last", "next", "other", "same"]

    prepositionsList = [
        "about", "above", "across", "after", "against", "along", "among", "around", "at",
        "before", "behind", "below", "beneath", "beside", "between", "by",
        "for", "from", "in", "inside", "into", "near", "of", "off", "on", "onto",
        "through", "to", "toward", "towards", "under", "upon", "with", "within",
        "out"
    ] # removed 'down' - otherwise direction 'down' will be removed as preposition

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

        # Parse input depending on number of tokens
        # There must be at least one token after stripping
        if len(tokens) < 1:
            return None

        elif len(tokens) == 1:
            return self.parseSingleToken(tokens[0])

        elif len(tokens) == 2:
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

    # Return Action from single token input
    def parseSingleToken(self, token):
        if (token in self.directionDict):
            return Action("move_user", self.parseDirection(token))
        else:
            return None
    
    # Return Action from two token input
    def parseTwoTokens(self, tokens):
        # check first token for a verb 
        verb = self.parseVerb(tokens[0])

        # Determine what other token is used for, depending on verb
        direction = None
        directObj = None
        # If invalid verb, return None
        if (verb is None):
            return None
        # If verb is "move_user", second token is probably direction
        elif (verb is "move_user"):
            direction = self.parseDirection(tokens[1])
        # Otherwise, the second token is probably a direct object
        else:
            # fix for verb "pairs" like "pick up":
            # ignore token[1] here if it is also a direction
            if (self.parseDirection(tokens[1]) is None):
                directObj = tokens[1]

        return Action(verb, direction, directObj)

    def parseThreeOrMoreTokens(self, tokens):
        action = self.parseTwoTokens(tokens[:2])    # parse first two tokens
        if (action is None):                        # check if invalid
            return None

        # FIXME: right now, just assume next token is a direct_obj
        # Should probably use a setter here...
        if (action.direct_obj == None):
            action.direct_obj = tokens[2]
        else:
            action.indirect_obj = tokens[2]

        # Return action
        return action
