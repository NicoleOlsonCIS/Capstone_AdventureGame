from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - edge cases
def test_no_input():

    errors = []

    action = parser.parseInput("")

    # Replace individual assertions with conditions
    if not action == None:
        errors.append("expected a 'None' type, got " + type(action).__name__)

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_one_bad_token():

    errors = []

    action = parser.parseInput("fdaskjfalskdfjas;lkdghjakdfgh")

    # Replace individual assertions with conditions
    if not action == None:
        errors.append("expected a 'None' type, got " + type(action).__name__)

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_two_bad_tokens():

    errors = []

    action = parser.parseInput("fdaskjfalskdfj;l ;;;!!fdsf.///f")

    # Replace individual assertions with conditions
    if not action == None:
        errors.append("expected a 'None' type, got " + type(action).__name__)

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_three_bad_tokens():

    errors = []

    action = parser.parseInput("fdaskjfalskdfj;l ;;;!!fdsf.///f ewrf2133")

    # Replace individual assertions with conditions
    if not action == None:
        errors.append("expected a 'None' type, got " + type(action).__name__)

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_rock_the_casbah():

    errors = []

    action = parser.parseInput("rock the casbah")

    # Replace individual assertions with conditions
    if not action == None:
        errors.append("expected a 'None' type, got " + type(action).__name__)

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
