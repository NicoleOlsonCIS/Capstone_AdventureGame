from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_go_up():

    errors = []

    action = parser.parseInput("go up")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_go_down():

    errors = []

    action = parser.parseInput("go down")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "d":
        errors.append("expected 'd', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_head_up():

    errors = []

    action = parser.parseInput("head up")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', headt " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', headt " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_head_down():

    errors = []

    action = parser.parseInput("head down")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', headt " + str(action.verb))
    if not action.direction == "d":
        errors.append("expected 'd', headt " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_head_upstairs():

    errors = []

    action = parser.parseInput("head upstairs")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', headt " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', headt " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_head_downstairs():

    errors = []

    action = parser.parseInput("head downstairs")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', headt " + str(action.verb))
    if not action.direction == "d":
        errors.append("expected 'd', headt " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - single character
def test_up():

    errors = []

    action = parser.parseInput("up")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_down():

    errors = []

    action = parser.parseInput("down")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "d":
        errors.append("expected 'd', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_u():

    errors = []

    action = parser.parseInput("u")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_d():

    errors = []

    action = parser.parseInput("d")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "d":
        errors.append("expected 'd', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


# Unit tests - capital letters 
def test_Go_Up():

    errors = []

    action = parser.parseInput("Go Up")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_gO_uP():

    errors = []

    action = parser.parseInput("gO uP")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - strip prepositions
def test_go_up_the_stairs():

    errors = []

    action = parser.parseInput("go up the stairs")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - alternative forms
def test_run_up_the_stairs():

    errors = []

    action = parser.parseInput("run up the stairs")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_walk_up_the_stairs():

    errors = []

    action = parser.parseInput("walk up the stairs")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "u":
        errors.append("expected 'u', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
