from parser import Parser
from action import Action

# Create parser for testing
parser = Parser()

# Unit tests - 'errors'
def test_pick_nose():

    errors = []

    action = parser.parseInput("pick nose")

    # Replace individual assertions with conditions
    if (action is not None):
        errors.append("expected a 'None' type, got " + type(action))

    # Now assert there've been no errors, else print them
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
