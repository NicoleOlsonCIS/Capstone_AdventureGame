from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_x():

    errors = []

    action = parser.parseInput("x")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == None:
        errors.append("expected 'None' type, got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_look():

    errors = []

    action = parser.parseInput("look")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == None:
        errors.append("expected 'None' type, got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_x_bench():

    errors = []

    action = parser.parseInput("x bench")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "bench":
        errors.append("expected 'bench', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_x_sky():

    errors = []

    action = parser.parseInput("x sky")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "sky":
        errors.append("expected 'sky', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_examine_bench():

    errors = []

    action = parser.parseInput("examine bench")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "bench":
        errors.append("expected 'bench', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_touch_bench():

    errors = []

    action = parser.parseInput("touch bench")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "bench":
        errors.append("expected 'bench', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_look_at_bench():

    errors = []

    action = parser.parseInput("look at bench")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "bench":
        errors.append("expected 'bench', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_look_in_mirror():

    errors = []

    action = parser.parseInput("look in mirror")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "mirror":
        errors.append("expected 'mirror', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_look_out_window():

    errors = []

    action = parser.parseInput("look out window")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "outside":
        errors.append("expected 'outside', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_see_out_window():

    errors = []

    action = parser.parseInput("see out window")

    # Replace individual assertions with conditions
    if not action.verb == "look":
        errors.append("expected 'look', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "outside":
        errors.append("expected 'outside', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
        