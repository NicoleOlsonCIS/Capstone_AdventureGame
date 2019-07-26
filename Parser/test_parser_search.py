from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_search_thing():

    errors = []

    action = parser.parseInput("search thing")

    # Replace individual assertions with conditions
    if not action.verb == "search":
        errors.append("expected 'search', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_look_in_thing():

    errors = []

    action = parser.parseInput("look in thing")

    # Replace individual assertions with conditions
    if not action.verb == "search":
        errors.append("expected 'search', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_look_inside_thing():

    errors = []

    action = parser.parseInput("look inside thing")

    # Replace individual assertions with conditions
    if not action.verb == "search":
        errors.append("expected 'search', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
