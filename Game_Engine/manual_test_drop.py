# Manual Testing Game Engine Drop Object
# 
#
# 1 - 2 places created
# 2 objects that are pickupable
# 1 user
# 
# Scenario 1: drop object when you don't have any objects --> error
#
# Scenario 2: pick up objects, drop object (in same room). 
#       --> verify that object gets back in room and user doesn't have
#
# Scenario 3: pick up object, drop in different room (move user to adjacent room)
#       --> verify that object gets put in different room and user doens't have it
#
# Scenario 4: pick up multiple objects, drop one
#       --> verify that correct object was dropped
#

import game_engine_v1
import action
from game_engine_v1 import *
from action import *