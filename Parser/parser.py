from action import Action

class Parser:

    # Class variables
    verbDict = {
        "go": "move_user",
        "move": "move_user",
        "run": "move_user",
        "walk": "move_user",
        "head": "move_user",
        "take": "take",
        "grab": "take"
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

    prepositionsList = [
        "above", "across", "against", "along", "among", "around", "at",
        "before", "behind", "below", "beneath", "beside", "between", "by",
        "from", "in", "into", "near", "of", "off", "on", "to",
        "toward", "under", "upon", "with", "within"
    ] # Had 'down', removed to fix bug

    # Default constructor - no instance variables

    # Parse user input into action object
    # TODO - add "context" parameter so engine can talk *to* parser?
    def parseInput(self, input):

        # Convert input to lowercase
        input = input.lower()

        # Tokenize input
        tokens = input.split()

        # FIXME - right now:
        # Assume that there must be at least two tokens
        if len(tokens) < 1:
            return None
        elif len(tokens) < 2:
            return self.parseSingleToken(tokens[0])

        # Remove articles 
        tokens = [token for token in tokens if token not in self.articlesList]

        # FIXME - right now:
        # Remove prepositions
        tokens = [token for token in tokens if token not in self.prepositionsList]

        # FIXME - right now:
        # Assume first token in string is the verb
        verb = self.parseVerb(tokens)
        # Assume second token is the direction, if verb == "move_user"
        if (verb == "move_user"):
            direction = self.parseDirection(tokens[1])
            return Action(verb, direction)
        # If verb is something else, look for direct_obj
        elif (verb != None):
            if (len(tokens) > 1):
                direct_obj = tokens[1]
                return Action(verb, None, direct_obj)
            else:
                return None
        else:
            return None

    # Convert user verb to valid form, return None on error
    def parseVerb(self, tokens):
        # Special case for 'pick up'
        if (len(tokens) > 1 and tokens[0] == "pick" and tokens[1] == "up"):
            del tokens[1]
            return "take"
        else:
            return self.verbDict.get(tokens[0])

    # Convert user-desired direction to valid form, return None on error
    def parseDirection(self, direction):
        return self.directionDict.get(direction)

    # Return Action from single token input
    def parseSingleToken(self, token):
        if (token in self.directionDict):
            return Action("move_user", self.parseDirection(token))
        else:
            return None

