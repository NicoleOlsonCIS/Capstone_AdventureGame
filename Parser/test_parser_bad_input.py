from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - edge cases
def test_no_input():

    errors = []

    action = parser.parseInput("")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_one_bad_token():

    errors = []

    action = parser.parseInput("fdaskjfalskdfjas;lkdghjakdfgh")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "fdaskjfalskdfjas;lkdghjakdfgh":
        errors.append("expected 'fdaskjfalskdfjas;lkdghjakdfgh', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_two_bad_tokens():

    errors = []

    action = parser.parseInput("fdaskjfalskdfj;l ;;;!!fdsf.///f")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "fdaskjfalskdfj;l":
        errors.append("expected 'fdaskjfalskdfj;l', got " + str(action.direct_obj))
    if not action.indirect_obj == ";;;!!fdsf.///f":
        errors.append("expected ';;;!!fdsf.///f', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_three_bad_tokens():

    errors = []

    action = parser.parseInput("fdaskjfalskdfj;l ;;;!!fdsf.///f ewrf2133")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "fdaskjfalskdfj;l":
        errors.append("expected do = 'fdaskjfalskdfj;l', got " + str(action.direct_obj))
    if not action.indirect_obj == ";;;!!fdsf.///f":
        errors.append("expected io = ';;;!!fdsf.///f', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_rock_the_casbah():

    errors = []

    action = parser.parseInput("rock the casbah")

    if not action.verb == None:
        errors.append("expected 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "rock":
        errors.append("expected do = 'rock', got " + str(action.direct_obj))
    if not action.indirect_obj == "casbah":
        errors.append("expected io = 'casbah', got " + str(action.direct_obj))


    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
