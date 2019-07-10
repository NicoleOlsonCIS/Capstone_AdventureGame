from action import Action

class Parser:

    # Class variables
    verbDict = {
        "go": "move_user",
        "move": "move_user",
        "run": "move_user"
    }

    directionDict = {
        "north": "north",
        "east": "east",
        "right": "east",
        "south": "south",
        "west": "west",
        "left": "left"
    }

    articlesList = ["the", "an", "a"]

    prepositionsList = [
        "above", "across", "against", "along", "among", "around", "at",
        "before", "behind", "below", "beneath", "beside", "between", "by",
        "down", "from", "in", "into", "near", "of", "off", "on", "to",
        "toward", "under", "upon", "with", "within"
    ]

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
        if len(tokens) < 2:
            return Action() # return "null" Action to engine

        # Remove articles 
        tokens = [token for token in tokens if token not in self.articlesList]

        # FIXME - right now:
        # Remove prepositions
        tokens = [token for token in tokens if token not in self.prepositionsList]

        # FIXME - right now:
        # Assume first token in string is the verb
        verb = self.parseVerb(tokens[0])
        # Assume second token is the direction
        direction = self.parseDirection(tokens[1])

        # Create and return valid action
        return Action(verb, direction)

    # Convert user verb to valid form, return None on error
    def parseVerb(self, verb):
        return self.verbDict.get(verb)

    # Convert user-desired direction to valid form, return None on error
    def parseDirection(self, direction):
        return self.directionDict.get(direction)
