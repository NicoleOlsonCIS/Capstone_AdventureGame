from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_sleep():

    errors = []

    action = parser.parseInput("sleep")

    # Replace individual assertions with conditions
    if not action.verb == "sleep":
        errors.append("expected 'sleep', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == None:
        errors.append("expected 'None' type, got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_go_to_bed():

    errors = []

    action = parser.parseInput("go to bed")

    # Replace individual assertions with conditions
    if not action.verb == "sleep":
        errors.append("expected 'sleep', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == None:
        errors.append("expected 'None' type, got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
