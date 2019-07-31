from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_insert_foo_in_bar():

    errors = []

    action = parser.parseInput("insert foo in bar")

    # Replace individual assertions with conditions
    if not action.verb == "insert":
        errors.append("expected 'insert', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "foo":
        errors.append("expected 'foo', got " + str(action.direct_obj))
    if not action.indirect_obj == "bar":
        errors.append("expected 'bar', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_drop_foo_inside_of_bar():

    errors = []

    action = parser.parseInput("drop foo inside of bar")

    # Replace individual assertions with conditions
    if not action.verb == "insert":
        errors.append("expected 'insert', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "foo":
        errors.append("expected 'foo', got " + str(action.direct_obj))
    if not action.indirect_obj == "bar":
        errors.append("expected 'bar', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_drop_foo_into_bar():

    errors = []

    action = parser.parseInput("drop foo into bar")

    # Replace individual assertions with conditions
    if not action.verb == "insert":
        errors.append("expected 'insert', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "foo":
        errors.append("expected 'foo', got " + str(action.direct_obj))
    if not action.indirect_obj == "bar":
        errors.append("expected 'bar', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_drop_foo_in_bar():

    errors = []

    action = parser.parseInput("drop foo in bar")

    # Replace individual assertions with conditions
    if not action.verb == "insert":
        errors.append("expected 'insert', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "foo":
        errors.append("expected 'foo', got " + str(action.direct_obj))
    if not action.indirect_obj == "bar":
        errors.append("expected 'bar', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_place_foo_in_bar():

    errors = []

    action = parser.parseInput("place foo in bar")

    # Replace individual assertions with conditions
    if not action.verb == "insert":
        errors.append("expected 'insert', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "foo":
        errors.append("expected 'foo', got " + str(action.direct_obj))
    if not action.indirect_obj == "bar":
        errors.append("expected 'bar', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# Bug-fix test case: issue #62
def test_put_newspaper_in():

    errors = []

    action = parser.parseInput("put newspaper in")

    # Replace individual assertions with conditions
    if not action.verb == "insert":
        errors.append("expected 'insert', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "newspaper":
        errors.append("expected 'foo', got " + str(action.direct_obj))
    if not action.indirect_obj == None: 
        errors.append("expected 'bar', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
