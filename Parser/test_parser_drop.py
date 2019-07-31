from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - basic function
def test_drop_thing():

    errors = []

    action = parser.parseInput("drop thing")

    # Replace individual assertions with conditions
    if not action.verb == "drop":
        errors.append("expected 'drop', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_discard_thing():

    errors = []

    action = parser.parseInput("discard thing")

    # Replace individual assertions with conditions
    if not action.verb == "drop":
        errors.append("expected 'drop', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_abandon_thing():

    errors = []

    action = parser.parseInput("abandon thing")

    # Replace individual assertions with conditions
    if not action.verb == "drop":
        errors.append("expected 'drop', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# OBSOLETE TEST CASE - "leave" no longer means drop
# Changed on Leslie's commit c43487e4cac3c5f579a81fe32091012f18d13c59
# def test_leave_out_thing():
#
#     errors = []
#
#     action = parser.parseInput("leave out thing")
#
#     # Replace individual assertions with conditions
#     if not action.verb == "drop":
#         errors.append("expected 'drop', got " + str(action.verb))
#     if not action.direction == None:
#         errors.append("expected 'None' type, got " + str(action.direction))
#     if not action.direct_obj == "thing":
#         errors.append("expected 'thing', got " + str(action.direct_obj))
#
#     # Now assert there've been no errors, else print them
#     assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_put_down_thing():

    errors = []

    action = parser.parseInput("put down thing")

    # Replace individual assertions with conditions
    if not action.verb == "drop":
        errors.append("expected 'drop', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))
    # TODO: Indirect object - table?

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))

# More complex phrases 
# OBSOLETE TEST CASE - "leave" no longer means drop
# Changed on Leslie's commit c43487e4cac3c5f579a81fe32091012f18d13c59
# def test_leave_thing_on_table():
#
#     errors = []
#
#     action = parser.parseInput("leave thing on table")
#
#     # Replace individual assertions with conditions
#     if not action.verb == "drop":
#         errors.append("expected 'drop', got " + str(action.verb))
#     if not action.direction == None:
#         errors.append("expected 'None' type, got " + str(action.direction))
#     if not action.direct_obj == "thing":
#         errors.append("expected 'thing', got " + str(action.direct_obj))
#     # TODO: Indirect object - table?
#
#     # Now assert there've been no errors, else print them
#     assert not errors, "errors occurred:\n{}".format("\n".join(errors))

def test_drop_thing_from_inventory():

    errors = []

    action = parser.parseInput("drop thing from inventory")

    # Replace individual assertions with conditions
    if not action.verb == "drop":
        errors.append("expected 'drop', got " + str(action.verb))
    if not action.direction == None:
        errors.append("expected 'None' type, got " + str(action.direction))
    if not action.direct_obj == "thing":
        errors.append("expected 'thing', got " + str(action.direct_obj))
    # TODO: Indirect object - table?

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
