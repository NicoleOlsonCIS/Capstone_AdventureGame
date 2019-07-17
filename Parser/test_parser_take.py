from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_take_thing():

    errors = []

    action = parser.parseInput("take thing")

    # Replace individual assertions with conditions
    if not action.verb == "take":
        errors.append("expected 'take', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_grab_thing():

    errors = []

    action = parser.parseInput("grab thing")

    # Replace individual assertions with conditions
    if not action.verb == "take":
        errors.append("expected 'take', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_pick_up_thing():

    errors = []

    action = parser.parseInput("pick up thing")

    # Replace individual assertions with conditions
    if not action.verb == "take":
        errors.append("expected 'take', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# More complex phrases 
def test_pick_up_thing_from_table():

    errors = []

    action = parser.parseInput("pick up thing from table")

    # Replace individual assertions with conditions
    if not action.verb == "take":
        errors.append("expected 'take', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
