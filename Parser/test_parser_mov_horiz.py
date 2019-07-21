from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_go_north():

    errors = []

    action = parser.parseInput("go north")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "n":
        errors.append("expected 'n', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_go_east():

    errors = []

    action = parser.parseInput("go east")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "e":
        errors.append("expected 'e', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_go_south():

    errors = []

    action = parser.parseInput("go south")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "s":
        errors.append("expected 's', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_go_west():

    errors = []

    action = parser.parseInput("go west")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "w":
        errors.append("expected 'w', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - single tokens
def test_n():

    errors = []

    action = parser.parseInput("n")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "n":
        errors.append("expected 'n', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_e():

    errors = []

    action = parser.parseInput("e")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "e":
        errors.append("expected 'e', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_s():

    errors = []

    action = parser.parseInput("s")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "s":
        errors.append("expected 's', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_w():

    errors = []

    action = parser.parseInput("w")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "w":
        errors.append("expected 'w', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

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

# Unit tests - capital letters 
def test_Go_North():

    errors = []

    action = parser.parseInput("Go North")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "n":
        errors.append("expected 'n', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_gO_nORTH():

    errors = []

    action = parser.parseInput("gO nORTH")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "n":
        errors.append("expected 'n', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - strip prepositions
def test_go_to_the_north():

    errors = []

    action = parser.parseInput("go to the north")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "n":
        errors.append("expected 'n', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - alternative forms
def test_run_to_the_north():

    errors = []

    action = parser.parseInput("run to the north")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "n":
        errors.append("expected 'n', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_walk_to_the_north():

    errors = []

    action = parser.parseInput("walk to the north")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "n":
        errors.append("expected 'n', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_head_to_the_north():

    errors = []

    action = parser.parseInput("head to the north")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "n":
        errors.append("expected 'n', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - invalid verbs
def test_fly_to_the_north():

    errors = []

    action = parser.parseInput("fly to the north")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected 'None' type, got " + str(action.verb))
    if not action.direction == "n":
        errors.append("expected 'n', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
