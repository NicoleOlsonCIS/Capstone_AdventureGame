from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_activate_thing():

    errors = []

    action = parser.parseInput("activate thing")

    # Replace individual assertions with conditions
    if not action.verb == "activate":
        errors.append("expected 'activate', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing' type, got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_turn_on_switch():

    errors = []

    action = parser.parseInput("turn on thing")

    # Replace individual assertions with conditions
    if not action.verb == "activate":
        errors.append("expected 'activate', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing' type, got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
