class Action:
    
    # Constructor 
    def __init__(self, verb = None, direction = None, direct_obj = None):
        self.verb = verb 
        self.direction = direction 
        self.direct_obj = direct_obj

    def setVerb(self, verb):
        self.verb = verb
    
    def setDirection(self, direction):
        self.direction = direction

    def setDirect_Obj(self, direct_obj):
        self.direct_obj = direct_obj
