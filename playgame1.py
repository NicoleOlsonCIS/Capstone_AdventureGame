# Allow access to files in other directories.
# Note: The Parser and Game_Engine folders
#   must be subdirectories of the current directory,
#   and playgame1.py must be in the current directory.
import sys
sys.path.insert(0, './Parser')
sys.path.insert(0, './Game_Engine')
import game_engine_v1 as g
import action
import parser as p
from output import *
import termios
from termios import tcflush, TCIFLUSH
import pickle
import os.path
from os import path


# Place parser, returns an array of place objects
def parsePlaces(game):

    arr_of_places = []

    fpath = "./Game_Files/places.txt"
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")
    
    ref_direction = {0: "n", 1: "ne", 2: "e", 3: "se", 4: "s", 5: "sw", 6: "w", 7:"nw", 8: "u", 9: "d"}

    for p in data_chunks:
        doors = {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None}
        l = p.split("\n")
        name = l[0]
        adjacent_places = l[1].split(",")
        for a in adjacent_places:
            if a == "None":
                a = None
        doors_arr = l[2].split(",")

        if len(doors_arr) == 1:
            doors = {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None}
        else:
            door_dict = {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None}
            i = 0
            for d in doors_arr:
                if d != "None":
                    dir = ref_direction[i]
                    door_dict[dir] = d
                i += 1
            doors = door_dict
        
        place = g.Place(game,name,"day","night",adjacent_places,None,doors)
        arr_of_places.append(place)

    return arr_of_places

# Loads information about readable objects.
def loadReadables(filename1, filename2, filename3, thing_obj):
    if thing_obj.name == "newspaper":
        fpath = "./Game_Files/" + filename2
        with open(fpath) as f:
            read_data = f.read()
            data_chunks = read_data.split("***\n")

        for chunk in data_chunks: 
            chunk = chunk.rstrip("\n")
            thing_obj.readDescrips.append(chunk)

        thing_obj.is_readable = True
        return

    elif thing_obj.name == "sheaf of papers":
        fpath = "./Game_Files/" + filename3 
        with open(fpath) as f:
            read_data = f.read()
            data_chunks = read_data.split("***\n")

        for chunk in data_chunks:
            chunk = chunk.rstrip("\n")
            thing_obj.readDescrips.append(chunk)

        thing_obj.is_readable = True
        return

    else: 
        fpath = "./Game_Files/" + filename1
        with open(fpath) as f: 
            read_data = f.read()
            data_chunks = read_data.split("***\n")

        for chunk in data_chunks:
            chunk = chunk.rstrip("\n")
            parts = chunk.split("###")
            if parts[0] == thing_obj.name:
                thing_obj.readDescrips.append(parts[1])
                thing_obj.is_readable = True
                return

# Loads information about openable features.
def loadOpenables(filename, thing_obj):
    fpath = "./Game_Files/" + filename
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")

    for chunk in data_chunks:
        chunk = chunk.rstrip("\n")
        parts = chunk.split(":")
        if parts[0].lower() == thing_obj.name.lower():
            thing_obj.openDescrip = parts[1]
            thing_obj.is_openable = True
            return

# Loads info about features that are windows.
def loadWindows(filename, thing_obj):
    fpath = "./Game_Files/" + filename
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")

    for chunk in data_chunks:
        chunk = chunk.rstrip("\n")
        parts = chunk.split(":")
        descrips = parts[1].split("###")

        if parts[0].lower() == thing_obj.name.lower():
            thing_obj.windowDescrips.append(descrips[0])
            thing_obj.windowDescrips.append(descrips[1]) 
            thing_obj.is_window = True
            return 

# Loads information about searchable features.
def loadSearchables(filename, thing_obj):
    fpath = "./Game_Files/" + filename
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")

    for chunk in data_chunks:
        chunk = chunk.rstrip("\n")
        parts = chunk.split(":")
        if parts[0].lower() == thing_obj.name.lower():
            thing_obj.searchDescrip = parts[1]
            thing_obj.is_searchable = True
            # any searchable obj is also openable
            thing_obj.is_openable = True
            return

# Load text data for listenable conversation 
def loadListens(place_obj, filename):
    fpath = "./Game_Files/" + filename
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")

    for chunk in data_chunks:
        chunk = chunk.rstrip("\n")     
        place_obj.listenDescrips.append(chunk)

# Some things in the game are related to each other,
# e.g. one thing is viewable only after another thing has been viewed.
# This function loads those relationships from a file. 
def loadThingDependencies(filename, thing_obj):
    fpath = "./Game_Files/" + filename
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")

    for chunk in data_chunks:
        chunk = chunk.rstrip("\n")
        objNames = chunk.split(":")
        if objNames[0].lower() == thing_obj.name.lower():
            thing_obj.hasOtherItems.append(objNames[1])


# Some things in the game have alternate names.
# e.g. "scrap of fabric"/"fabric scrap", or "ticket counter"/"counter"
# This function loads those alt names from a file.
def loadAltNames(filename, thing_obj):
    fpath = "./Game_Files/" + filename
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")

    for chunk in data_chunks:
        chunk = chunk.rstrip("\n")
        objNames = chunk.split(":")
        if len(objNames) > 1: 
            synonyms = objNames[1].split(",")
            if objNames[0].lower() == thing_obj.name.lower():
                for syn in synonyms:
                    thing_obj.altNames.append(syn)
                return

# read passage descriptions from file "placepassages.txt" and set place
def loadPassageData(places):

    ref_direction = {0: "n", 1: "ne", 2: "e", 3: "se", 4: "s", 5: "sw", 6: "w", 7:"nw", 8: "u", 9: "d"}

    # build path to data file
    fpath = "./Game_Files/" + "placepassages.txt"
 
    # read file all in at once 
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")

    i = 0
    for p in places: 
        placeInfo = data_chunks[i]
        place_arr = placeInfo.split("\n")
        name = place_arr[0]
        #print("Name coming from file: " + name)
        #print("Name coming from places array: " + p.name)
        name = name.rstrip("\n")
        passages_inp = place_arr[1]
        #if name != p.name: 
            #print("mismatch")
        passages_int = passages_inp.split("-")
        emptyArr = []
        passages_dict = {"n": emptyArr, "ne": emptyArr, "e": emptyArr, "se": emptyArr, "s": emptyArr, "sw": emptyArr, "w": emptyArr, "nw": emptyArr, "u": emptyArr, "d": emptyArr}
        j = 0
        for passage in passages_int:
            if passage != "None":
                pKey = ref_direction.get(j)
                # print(pKey)
                # check if there's a comma
                if "," in passage:
                    arr = passage.split(",")
                else: 
                    arr = []
                    arr.append(passage)
                p1 = {pKey: arr}
                passages_dict.update(p1)
                # print(passages_dict.get(pKey))
            j += 1
        # now set the place object with the passager dictionary
        p.setPassages(passages_dict)
        i += 1

# dependency: places array is in order created in main game building
def loadTransitionData(places): 
    # build path to data file
    fpath = "./Game_Files/" + "transitions.txt"
 
    # read file all in at once 
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")

    i = 0
    for p in places:
        tr = data_chunks[i] # get the text for the section
        lines = tr.split("\n") # divide up by line
        eArr = ["None", "None", "None"]
        transitions_dict = {"n": eArr, "ne": eArr, "e": eArr, "se": eArr, "s": eArr, "sw": eArr, "w": eArr, "nw": eArr, "u": eArr, "d": eArr}
        arr = []
        for l in lines:
            div = l.split("#")
            str = div[0] # represents the direction component
            if(len(div) > 1):
                arr = div[1].split("--") # represents each entry for that direction
                p1 = {str: arr}
                transitions_dict.update(p1)
                # set the transitions on the place
        p.setTransitions(transitions_dict)
        i += 1

def loadPlaceData(place_obj, filename, game_obj):

    # build path to data file
    fpath = "./Game_Files/" + filename
 
    # read file all in at once 
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")

    # day and night descriptions
    dayDescrip1 = data_chunks[0].rstrip("\n")
    dayDescrip2 = data_chunks[1].rstrip("\n")
    dayDescrip3 = data_chunks[2].rstrip("\n")
    
    day = [dayDescrip1, dayDescrip2, dayDescrip3]

    nightDescrip1 = data_chunks[3].rstrip("\n")
    nightDescrip2 = data_chunks[4].rstrip("\n")
    nightDescrip3 = data_chunks[5].rstrip("\n")

    night = [nightDescrip1, nightDescrip2, nightDescrip3]

    # v11 implement visit related descriptions
    # add descriptions to place_obj dictionary
    place_obj.day = day
    place_obj.night = night 

    nextIdxIncrement = 0

    # load feature information and create/add Things
    if "no features" not in data_chunks[6]:
        featurenames = data_chunks[6].split("\n")
        
        # have to remove the non-features before setting index tracking 
        for f in featurenames:
            if f == "":
                featurenames.remove(f)

        # get the count of features
        numFeatures = len(featurenames)

        # figure out where the next type section starts based on how many *** there will be for features
        # for instance, if there is 1 feature, then we index past that feature's descriptions
        nextIdxIncrement = numFeatures

        featureDescriptions = []
        count = 0

        # starting in the next *** section, get the corresponding descriptions for each feature
        while count < numFeatures: 
            featureDescriptions.append(data_chunks[7 + count])
            count += 1

        count = 0
        for feature in featurenames:
            feature = feature.rstrip()
            feature = feature.lstrip()
            if feature != "":

                # get the description block for this feature
                fd = featureDescriptions[count]

                # separate out by delimeter and remove blank descriptions
                fd_arr = fd.split("\n")
                for f in fd_arr:
                    if f == "":
                        fd_arr.remove(f)

                # find out how many descriptions have been entered
                numDescriptions = len(fd_arr)

                # if there is less than 5, fill up to 5 by copying the last one over
                while numDescriptions < 5:
                    fd_arr.append(fd_arr[numDescriptions - 1])
                    numDescriptions = len(fd_arr)

                # check if there are any 'day/night' aspects to descriptions (otherwise all day)
                day = []
                night = []
                for f in fd_arr:
                    day_night = f.split("###")
                    if day_night[1] != "No night":
                        night.append(day_night[1])
                    day.append(day_night[0])
                
                # if there are no night specific descriptions, then set them the same as day
                if len(night) == 0:
                    night = day

                newthing = g.Thing(feature, day, night, place_obj, False, False)
                place_obj.addThing(newthing)

                # load thing dependencies
                loadThingDependencies("objdependencies.txt", newthing)
		        # load alternate names
                loadAltNames("objalternatenames.txt", newthing)
                # load info about searchable features
                loadSearchables("searchables.txt", newthing) 
                # load info about openable features
                loadOpenables("openables.txt", newthing)
                # load info about windows
                loadWindows("windowdescriptions.txt", newthing) 

                count += 1

    # load object information and create/add Things
    # v12 if there were no features, then nextIdxIncrement is 1 and we are on chunk 7
    if "no objects" not in data_chunks[7 + nextIdxIncrement]:

        idx = 7 + nextIdxIncrement
        objnames = data_chunks[idx].split("\n")

        for o in objnames:
            if o == "":
                objnames.remove(o)

        # get the count of objects
        numObjects = len(objnames)

        # figure out where the next type section starts based on how many sections there will be for objects
        # for instance, if there is 1 object, then we index past that object's descriptions
        nextIdxIncrement = nextIdxIncrement + numObjects

        objectDescriptions = []
        count = 0

        # starting in the next *** section, get the corresponding descriptions for each object
        while count < numObjects: 
            objectDescriptions.append(data_chunks[idx + 1 + count])
            count += 1

        count = 0
        for obj in objnames:
            obj = obj.rstrip()
            obj = obj.lstrip()
            if obj != "":
                # get the description block for this object
                od = objectDescriptions[count]

                # separate out by delimeter and remove empty descriptions
                od_arr = od.split("\n")
                for o in od_arr:
                    if o == "":
                        od_arr.remove(o)
                
                # find out how many descriptions have been entered
                numDescriptions = len(od_arr)

                # if there is less than 5, fill up to 5 by copying the last one over
                while numDescriptions < 5:
                    od_arr.append(od_arr[numDescriptions - 1])
                    numDescriptions = len(od_arr)

                # check if there are any 'day/night' aspects to descriptions (otherwise all day)
                day = []
                night = []
                for o in od_arr:
                    day_night = o.split("###")
                    if day_night[1] != "No night":
                        night.append(day_night[1])
                    day.append(day_night[0])
                
                # if there are no night specific descriptions, then set them the same as day
                if len(night) == 0:
                    night = day

                newthing = g.Thing(obj, day, night, place_obj, True, False)
                place_obj.addThing(newthing)
             
                # load alternate thing names
                loadAltNames("objalternatenames.txt", newthing)
                # load readable things
                loadReadables("readables.txt", "newspaper.txt", "sheafpapers.txt", newthing)
                # load openable things
                loadOpenables("openables.txt", newthing)

                count += 1 
    
    # character loading section
    if "no characters" not in data_chunks[8 + nextIdxIncrement]:
        idx = 8 + nextIdxIncrement
        charnames = data_chunks[idx].split("\n")

        for c in charnames:
            if c == "":
                charnames.remove(c)

        # get the count of characters
        numCharacters = len(charnames)

        # figure out where the next type section starts based on how many sections there will be for characters
        nextIdxIncrement = (2 * numCharacters) + 1 # x2 because each character has a description section and dialogue section

        characterDescriptions = []
        characterDialogue = []
        count = 0

        # starting in the next *** section, get the corresponding descriptions for each character
        while count < numCharacters: 
            characterDescriptions.append(data_chunks[idx + 1 + count])
            count += 1
        #while count < numCharacters * 2:
            #characterDialogue.append(data_chunks[idx + 1 + count])
            #count += 1
    
        count = 0
        for char in charnames:
            char = char.rstrip()
            char = char.lstrip()
            if char != "":
                # get the description block for this character
                cd = characterDescriptions[count]

                # separate out by delimeter and remove empty descriptions
                cd_arr = cd.split("\n")
                for c in cd_arr:
                    if c == "":
                        cd_arr.remove(c)
                
                # find out how many descriptions have been entered
                numDescriptions = len(cd_arr)

                # if there is less than 5, fill up to 5 by copying the last one over
                while numDescriptions < 5:
                    cd_arr.append(cd_arr[numDescriptions - 1])
                    numDescriptions = len(cd_arr)

                # check if there are any 'day/night' aspects to descriptions (otherwise all day)
                day = []
                night = []
                for c in cd_arr:
                    day_night = c.split("###")
                    if day_night[1] != "No night":
                        night.append(day_night[1])
                    day.append(day_night[0])
                
                # if there are no night specific descriptions, then set them the same as day
                if len(night) == 0:
                    night = day

                ''' 
                # Do the same now for dialogue
                # get the description block for this character
                cdi = characterDialogue[count]

                # separate out by delimeter and remove empty descriptions
                cdi_arr = cdi.split("\n")
                for c in cdi_arr:
                    if c == "":
                        cdi_arr.remove(c)
                
                # find out how many dialogues have been entered
                numDialogues = len(cdi_arr)

                # if there is less than 5, fill up to 5 by copying the last one over
                while numDialogues < 5:
                    cdi_arr.append(cdi_arr[numDialogues - 1])
                    numDialogues = len(cdi_arr)

                # check if there are any 'day/night' aspects to descriptions (otherwise all day)
                char_day = []
                char_night = []
                for c in cdi_arr:
                    day_night = c.split("&&&")
                    if day_night[1] != "No night":
                        char_night.append(day_night[1])
                    char_day.append(day_night[0])
                
                # if there are no night specific descriptions, then set them the same as day
                if len(char_night) == 0:
                    char_night = char_day

                newthing = g.Thing(char, day, night, place_obj, False, True, char_day, char_night)
                ''' 
       
                # dialogue will be loaded separately
                newthing = g.Thing(char, day, night, place_obj, False, True)

                #place_obj.addThing(newthing)
                place_obj.addCharacter(newthing)

                game_obj.allCharacters.append(newthing)

                # load alternate thing names
                loadAltNames("objalternatenames.txt", newthing)

                count += 1
    

# load character dialog for various locations/topics
def loadDialogDict(filename, character):

    fpath = "./Game_Files/" + filename

    with open(fpath) as mfile:
        dialogues = mfile.read()

    dm_chunks = dialogues.split("***\n")
    dialogue_dict = {}

    for dmchunk in dm_chunks:
        dmchunk = dmchunk.rstrip("\n")
        dmpieces = dmchunk.split(":::")
        placeOrTopic = dmpieces[0]
        if placeOrTopic not in dialogue_dict.keys():
            dialogue_dict[placeOrTopic] = []
            # key is place or topic name, value is list of dialogues for that place/topic
            dialogue_dict[placeOrTopic].append(dmpieces[1])
        else:
            dialogue_dict[placeOrTopic].append(dmpieces[1])

    character.char_dict = dialogue_dict
    
def buildGame():

    # start game at 8 am
    game = g.Game(1,8.00) # time is now a float

    places = parsePlaces(game)

    # set up the user 
    user = g.User(game, "user1", "Train Platform", "n", False) 

    # finish populating room topology
    for p in places:
        p.setAdjacentPlaces(game)

    
    # Order of places: 
    '''
    Train Platform
    Station-House
    Fields
    Front Manor Grounds
    Foyer
    Upstairs Hallway 1
    Upstairs Hallway 2
    Upstairs Hallway 3
    Upstairs Hallway 4
    Upstairs Hallway 5
    Spare Room
    Small Lavatory
    Bedroom
    Library
    Study
    Large Bedroom
    Servant Stair Top
    Servant Stair Bottom
    Downstairs Hallway 3
    Downstairs Hallway 2
    Downstairs Hallway 1
    Kitchen
    Servant Quarters
    Drawing Room
    Dining Room
    Cloakroom
    Ash Grove
    Rear Manor Grounds
    Root Cellar'''



    place_data_files = [
        "trainplatform.txt",
        "stationhouse.txt",
        "fields.txt",
        "frontmanorgrounds.txt",
        "foyer.txt",
        "upstairshallway1.txt",
        "upstairshallway2.txt",
        "upstairshallway3.txt",
        "upstairshallway4.txt",
        "upstairshallway5.txt",
        "spareroom.txt",
        "smalllavatory.txt",
        "bedroom.txt",
        "library.txt",
        "study.txt",
        "None",
        "servantsstairtop.txt",
        "servantsstairbottom.txt",
        "downstairshallway3.txt",
        "downstairshallway2.txt",
        "downstairshallway1.txt",
        "kitchen.txt",
        "None",
        "drawingroom.txt",
        "diningroom.txt",
        "cloakroom.txt",
        "ashgrove.txt",
        "rearmanorgrounds.txt",
        "None"
        ]
    
    i = 0
    for data in place_data_files:
        # provisions for places that don't have text files
        if data != "None":
            loadPlaceData(places[i], data, game)
            #print("place name " + places[i].name + " data file: " + data)
            i += 1
        else:
            i += 1

    loadListens(places[23], "drawinglisten.txt")

    # load passage data
    loadPassageData(places)
    # load transition data
    loadTransitionData(places)

    # load maude dialogue for various locations
    currChar = None
    for char in game.allCharacters:
        if char.name.lower() == "maude":
            currChar = char

    if currChar != None:
        loadDialogDict("maude.txt", currChar) 

    # load mina dialogue for various locations
    currChar = None
    for char in game.allCharacters:
        if char.name.lower() == "mina":
            currChar = char
    if currChar != None:
        loadDialogDict("mina.txt", currChar) 

    # load narrative intro text
    with open("./Game_Files/intro.txt") as ifile:
        intro = ifile.read()
    intro_chunks = intro.split("***\n")
    for ichunk in intro_chunks: 
        game.narrativeIntro.append(ichunk)

    # load ending event text
    with open("./Game_Files/endingevents.txt") as efile:
        endings = efile.read()
    end_chunks = endings.split("***\n")
    for echunk in end_chunks:
        game.endingEvents.append(echunk) 


    # associate user with game 
    game.setUser(user)

    return game

# returns a game object
def fromSave():
    
    pickle_in = open("savedGame.pickle", "rb")
    game = pickle.load(pickle_in)
    # get the game object
    return game

def saveGame(game):
    print("saving game . . . ")
    pickle_out = open("savedGame.pickle", "wb")
    pickle.dump(game, pickle_out)
    pickle_out.close()
    #time.sleep(0.5)
    print("your game has been saved")


def gameLoop(game):
    # set up parser
    playparser = p.Parser()
    # start playing
    while True:
        # flush standard in 
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

        # game.getTime() # uncomment this if you need it!

        # game continues until user enters quit at the prompt 
        received = input("> ")
        if "quit" in received:
            print("Do you want to save this game? (y/n)")
            received = input("> ")
            if "y" in received:
                saveGame(game)
                return
            else:
                break
        elif "savegame" in received:
                saveGame(game)
                return
        else:
            playaction = action.Action()
            playaction = playparser.parseInput(received)
            if (isinstance(playaction, action.Action)):
                #print(playaction.verb, playaction.direction, playaction.direct_obj, playaction.indirect_obj) 
                game.fromParserToGame(playaction)

def main():

    ts = os.get_terminal_size()
    if ts.columns < 70:
        Output.print_error("Error: Please expand the width of your console window. Min width of 70 columns required for game!")
        return
    if ts.lines < 30:
        Output.print_error("Error: Please expand the height of your console window. Min height of 30 lines required for game!")
        return

    if sys.stdin.isatty():

        Output.printTrees()

        Output.welcomePage()
        print("Would you like to start a new game or load a saved game? (new/loadgame)")
        new_or_save = input("> ")

        if "new" in new_or_save:  
            game = buildGame()
            game.setIsValid()
            # prompt user to indicate whether they want to see intro narrative text
            print("Starting new game. Display narrative intro? Recommended on first play only. (y/n)")
            show_intro = input("> ")
            if "y" in show_intro:
                game.getTime()
                Output.printIntro(game.narrativeIntro) 
            Output.welcomeToGame(game.user.current_place.day[0]) # start day first visit
            # ensure characters show up in first room description
            game.user.current_place.showCharacters()

            gameLoop(game)
            print("Goodbye!")
            print("\n")
            return
    
        elif "loadgame" in new_or_save:
            print("Loadgame selected. Is this correct? (y/n)")
            confirm = input("> ")
            print("\n")
            if confirm == 'y':
                Output.searchForGameOutput("Checking for existing saves")

                if path.exists("savedGame.pickle"):
                    game = fromSave()
                    game.setIsValid()

                    time = game.time
                    Output.welcomeBackToGame(game.user.current_place.getDescriptionBasedOnTimeAndVisitCount(time))
                    game.getTime()
                    gameLoop(game)
                    print("Goodbye again!")
                    return
                else: 
                    print("No saves found. Exiting...")
                    return
            else:
                print("Loadgame not confirmed. Exiting ... ")
                return

        else:
            print("You did not choose to start a new game or load a saved game. Exiting...") 
            return
    else:
        print("Error: You must play this game on a command line interface (no simulated terminals)")
        return
main()
