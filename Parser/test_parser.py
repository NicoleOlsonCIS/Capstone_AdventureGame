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
        errors.append("expected a 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected a 'None' type', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_one_bad_token():

    errors = []

    action = parser.parseInput("fdaskjfalskdfjas;lkdghjakdfgh")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected a 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected a 'None' type', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_two_bad_tokens():

    errors = []

    action = parser.parseInput("fdaskjfalskdfj;l ;;;!!fdsf.///f")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected a 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected a 'None' type', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_three_bad_tokens():

    errors = []

    action = parser.parseInput("fdaskjfalskdfj;l ;;;!!fdsf.///f ewrf2133")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected a 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected a 'None' type', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - basic function
def test_go_north():

    errors = []

    action = parser.parseInput("go north")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "north":
        errors.append("expected 'north', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_go_east():

    errors = []

    action = parser.parseInput("go east")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "east":
        errors.append("expected 'east', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_go_south():

    errors = []

    action = parser.parseInput("go south")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "south":
        errors.append("expected 'south', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_go_west():

    errors = []

    action = parser.parseInput("go west")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "west":
        errors.append("expected 'west', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - capital letters 
def test_Go_North():

    errors = []

    action = parser.parseInput("Go North")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "north":
        errors.append("expected 'north', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_gO_nORTH():

    errors = []

    action = parser.parseInput("gO nORTH")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "north":
        errors.append("expected 'north', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - strip prepositions
def test_go_to_the_north():

    errors = []

    action = parser.parseInput("go to the north")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "north":
        errors.append("expected 'north', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - alternative forms
def test_run_to_the_north():

    errors = []

    action = parser.parseInput("run to the north")

    # Replace individual assertions with conditions
    if not action.verb == "move_user":
        errors.append("expected 'move_user', got " + str(action.verb))
    if not action.direction == "north":
        errors.append("expected 'north', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Unit tests - invalid verbs
def test_fly_to_the_north():

    errors = []

    action = parser.parseInput("fly to the north")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected a 'None' type, got " + str(action.verb))
    if not action.direction == "north":
        errors.append("expected 'north', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_rock_the_casbah():

    errors = []

    action = parser.parseInput("rock the casbah")

    # Replace individual assertions with conditions
    if not action.verb == None:
        errors.append("expected a 'None' type, got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected a 'None' type', got " + str(action.direction))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
