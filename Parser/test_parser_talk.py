from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_talk():

    errors = []

    action = parser.parseInput("talk")

    # Replace individual assertions with conditions
    if not action.verb == "talk_npc":
        errors.append("expected 'talk_npc', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == None:
        errors.append("expected 'None' type, got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_talk_to_person():

    errors = []

    action = parser.parseInput("talk to person")

    # Replace individual assertions with conditions
    if not action.verb == "talk_npc":
        errors.append("expected 'talk_npc', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "person":
        errors.append("expected 'person', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_ask_person():

    errors = []

    action = parser.parseInput("ask person")

    # Replace individual assertions with conditions
    if not action.verb == "talk_npc":
        errors.append("expected 'talk_npc', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "person":
        errors.append("expected 'person', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
