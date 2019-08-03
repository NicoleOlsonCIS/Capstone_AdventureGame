# Allow access to files in other directories.
# Note: The Parser and Game_Engine folders
#   must be subdirectories of the current directory,
#   and playgame1.py must be in the current directory.
import sys
sys.path.insert(0, './Parser')
sys.path.insert(0, './Game_Engine')
import game_engine_v1 as g
import action as a
import parser as p
from output import *
import termios
from termios import tcflush, TCIFLUSH
import pickle
import os.path
from os import path

# playgame1.py works with v11.7 of game engine

# Loads information about readable objects.
def loadReadables(filename1, filename2, thing_obj):
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

def loadPlaceData(place_obj, filename):

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

                newthing = g.Thing(feature, day, night, place_obj, False, False, None, None)
                place_obj.addThing(newthing)

                # load thing dependencies
                loadThingDependencies("objdependencies.txt", newthing)
		        # load alternate names
                loadAltNames("objalternatenames.txt", newthing)
                # load info about searchable features
                loadSearchables("searchables.txt", newthing) 

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

                newthing = g.Thing(obj, day, night, place_obj, True, False, None, None)
                place_obj.addThing(newthing)
             
                # load alternate thing names
                loadAltNames("objalternatenames.txt", newthing)
                # load readable  things
                loadReadables("readables.txt", "newspaper.txt", newthing)

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
        while count < numCharacters * 2:
            characterDialogue.append(data_chunks[idx + 1 + count])
            count += 1
    
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
                    day_night = c.split("###")
                    if day_night[1] != "No night":
                        char_night.append(day_night[1])
                    char_day.append(day_night[0])
                
                # if there are no night specific descriptions, then set them the same as day
                if len(char_night) == 0:
                    char_night = char_day

                newthing = g.Thing(char, day, night, place_obj, False, True, char_day, char_night)
                place_obj.addThing(newthing)
                place_obj.addCharacter(newthing)

                # load alternate thing names
                loadAltNames("objalternatenames.txt", newthing)

                count += 1
        
def buildGame():

    # start game at 7 am
    game = g.Game(1,7)

    # v11: descriptions are now 2D array to capture the number of visits of user (first, second, all subsequent ...)
    day = ["place during day 1", "place during day 2", "place during day 3"]
    night = ["place during night 1", "place during night 2", "place during night 3"]
    no_doors = {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None}


    # populate room topology 
    place1 = g.Place(
        game,
        "Train Platform",
        day, 
        night,
        [None, "Fields", None, None, None, None, "Station-House", None, None, None],
        None,
        no_doors)

    place2 = g.Place(
        game,
        "Station-House",
        day,
        night,
        [None, None, "Train Platform", None, None, None, None, None, None, None],
        None,
        {"n": None, "ne": None, "e": "unlocked", "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})

    place3 = g.Place(
        game,
        "Fields",
        day,
        night,
        ["Front Manor Grounds", None, None, None, None, "Train Platform", None, None, None, None],
        None,
        {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})

    place4 = g.Place(
        game,
        "Front Manor Grounds",
        day,
        night,
        ["Foyer", None, None, None, "Fields", None, None, "Ash Grove", None, None],
        None,
        {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})


    place5 = g.Place(game, "Foyer", day, night, ["Downstairs Hallway 1", None, None, None, "Front Manor Grounds", None, "Cloakroom", None, "Upstairs Hallway 1", None], None, {"n": None, "ne": None, "e": None, "se": None, "s": "unlocked", "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place6 = g.Place(game, "Upstairs Hallway 1", day, night, ["Upstairs Hallway 2", None, None, None, None, None, "Spare Room", None, None, "Foyer"], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place7 = g.Place(game, "Upstairs Hallway 2", day, night, ["Upstairs Hallway 3", None, "Small Lavatory", None, "Upstairs Hallway 1", None, "Bedroom", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place8 = g.Place(game, "Upstairs Hallway 3", day, night, ["Upstairs Hallway 4", None, "Library", None, "Upstairs Hallway 2", None, None, None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place9 = g.Place(game, "Upstairs Hallway 4", day, night, ["Upstairs Hallway 5", None, "Study", None, "Upstairs Hallway 3", None, "Large Bedroom", None, None, None], None, {"n": None, "ne": None, "e": "locked", "se": None, "s": None, "sw": None, "w": "locked", "nw": None, "u": None, "d": None})
    place10 = g.Place(game, "Upstairs Hallway 5", day, night, ["Servants\' Stair Top", None, None, None, "Upstairs Hallway 4", None, None, None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place11 = g.Place(game, "Spare Room", day, night, [None, None, "Upstairs Hallway 1", None, None, None, None, None, None, None], None, {"n": None, "ne": None, "e": "unlocked", "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})  
    place12 = g.Place(game, "Small Lavatory", day, night, [None, None, None, None, None, None, "Upstairs Hallway 2", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": "unlocked", "nw": None, "u": None, "d": None})
    place13 = g.Place(game, "Bedroom", day, night, [None, None, "Upstairs Hallway 2", None, None, None, None, None, None, None], None, {"n": None, "ne": None, "e": "unlocked", "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None}) 
    place14 = g.Place(game, "Library", day, night, [None, None, None, None, None, None, "Upstairs Hallway 3", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place15 = g.Place(game, "Study", day, night, [None, None, None, None, None, None, "Upstairs Hallway 4", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": "locked", "nw": None, "u": None, "d": None})
    place16 = g.Place(game, "Large Bedroom", day, night, [None, None, "Upstairs Hallway 4", None, None, None, None, None, None, None], None, {"n": None, "ne": None, "e": "locked", "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place17 = g.Place(game, "Servants\' Stair Top", day, night, [None, None, None, None, "Upstairs Hallway 5", None, None, None, None, "Servants\' Stair Bottom"], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place18 = g.Place(game, "Servants\' Stair Bottom", day, night, [None, None, None, None, "Downstairs Hallway 3", None, None, None, "Servants\' Stair Top", None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})    
    place19 = g.Place(game, "Downstairs Hallway 3", day, night, ["Servants\' Stair Bottom", None, None, None, "Downstairs Hallway 2", None, None, None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place20 = g.Place(game, "Downstairs Hallway 2", day, night, ["Downstairs Hallway 3", None, "Kitchen", None, "Downstairs Hallway 1", None, "Servants\' Quarters", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": "locked", "nw": None, "u": None, "d": None})
    place21 = g.Place(game, "Downstairs Hallway 1", day, night, ["Downstairs Hallway 2", None, "Dining Room", None, "Foyer", None, "Drawing Room", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place22 = g.Place(game, "Kitchen", day, night, [None, None, None, None, None, None, "Downstairs Hallway 2", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place23 = g.Place(game, "Servants\' Quarters", day, night, [None, None, "Downstairs Hallway 2", None, None, None, None, None, None, None], None, {"n": None, "ne": None, "e": "locked", "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place24 = g.Place(game, "Drawing Room", day, night, [None, None, "Downstairs Hallway 1", None, None, None, None, None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place25 = g.Place(game, "Dining Room", day, night, [None, None, None, None, None, None, "Downstairs Hallway 1", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place26 = g.Place(game, "Cloakroom", day, night, [None, None, "Foyer", None, None, None, None, None, None, None], None, {"n": None, "ne": None, "e": "unlocked", "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place27 = g.Place(game, "Ash Grove", day, night, ["Rear Manor Grounds", None, None, "Front Manor Grounds", None, None, None, None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None}) 
    place28 = g.Place(game, "Rear Manor Grounds", day, night, [None, None, "Root Cellar", None, "Ash Grove", None, None, None, None, None], None, {"n": None, "ne": None, "e": "locked", "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None}) 
    place29 = g.Place(game, "Root Cellar", day, night, [None, None, None, None, None, None, "Rear Manor Grounds", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": "locked", "nw": None, "u": None, "d": None})

    # set up the user 
    user = g.User(game, "user1", "Train Platform", "n", False) 

    # finish populating room topology
    place1.setAdjacentPlaces(game)
    place2.setAdjacentPlaces(game)
    place3.setAdjacentPlaces(game)
    place4.setAdjacentPlaces(game)
    place5.setAdjacentPlaces(game)
    place6.setAdjacentPlaces(game)
    place7.setAdjacentPlaces(game)
    place8.setAdjacentPlaces(game)
    place9.setAdjacentPlaces(game)
    place10.setAdjacentPlaces(game)
    place11.setAdjacentPlaces(game)
    place12.setAdjacentPlaces(game)
    place13.setAdjacentPlaces(game)
    place14.setAdjacentPlaces(game)
    place15.setAdjacentPlaces(game)
    place16.setAdjacentPlaces(game)
    place17.setAdjacentPlaces(game)
    place18.setAdjacentPlaces(game)
    place19.setAdjacentPlaces(game) 
    place20.setAdjacentPlaces(game)
    place21.setAdjacentPlaces(game)
    place22.setAdjacentPlaces(game)
    place23.setAdjacentPlaces(game)
    place24.setAdjacentPlaces(game)
    place25.setAdjacentPlaces(game)
    place26.setAdjacentPlaces(game)
    place27.setAdjacentPlaces(game)
    place28.setAdjacentPlaces(game)
    place29.setAdjacentPlaces(game)

    # load room data from files
    loadPlaceData(place1, "trainplatform.txt") 
    loadPlaceData(place2, "stationhouse.txt")
    loadPlaceData(place3, "fields.txt")
    loadPlaceData(place4, "frontmanorgrounds.txt")
    loadPlaceData(place5, "foyer.txt")
    loadPlaceData(place6, "upstairshallway1.txt")
    loadPlaceData(place7, "upstairshallway2.txt")
    loadPlaceData(place8, "upstairshallway3.txt")
    loadPlaceData(place9, "upstairshallway4.txt")
    loadPlaceData(place10, "upstairshallway5.txt")
    loadPlaceData(place11, "spareroom.txt")
    loadPlaceData(place12, "smalllavatory.txt")
    loadPlaceData(place13, "bedroom.txt")
    loadPlaceData(place14, "library.txt")
    
    loadPlaceData(place17, "servantsstairtop.txt")
    loadPlaceData(place18, "servantsstairbottom.txt")
    loadPlaceData(place19, "downstairshallway3.txt")
    loadPlaceData(place20, "downstairshallway2.txt")
    loadPlaceData(place21, "downstairshallway1.txt")
    loadPlaceData(place22, "kitchen.txt")

    loadPlaceData(place24, "drawingroom.txt")
    loadPlaceData(place25, "diningroom.txt")
    loadPlaceData(place26, "cloakroom.txt")
    loadPlaceData(place27, "ashgrove.txt")
    loadPlaceData(place28, "rearmanorgrounds.txt")

    loadListens(place24, "drawinglisten.txt")

    places = [place1, place2, place3, place4, place5, place6, place7, place8, place9, place10, place11, place12, place13, place14, place15, place16, place17, place18, place19, place20, place21, place22, place23, place24, place25, place26, place27, place28, place29]

    loadPassageData(places)

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
    pickle_out = open("savedGame.pickle", "wb")
    pickle.dump(game, pickle_out)
    pickle_out.close()


def gameLoop(game):
    # set up parser
    playparser = p.Parser()

    # start playing
    while True:
        # flush standard in 
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
        #sys.stdin.flush()

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
        elif "save" in received:
            print("Saving game ... ")
            saveGame(game)
            return
        else:
            playaction = a.Action()
            playaction = playparser.parseInput(received)
            print(playaction.verb, playaction.direction, playaction.direct_obj, playaction.indirect_obj) 
            game.fromParserToGame(playaction)

def main():

    print("Welcome! Would you like to start a new game or load a saved game? new/load")
    new_or_save = input("> ")

    if "new" in new_or_save:  
        game = buildGame()
        game.setIsValid()
        Output.welcomeToGame(game.user.current_place.day[0]) # start day first visit
        print("Enter \'quit\' at the prompt to quit the game at any time.")
        gameLoop(game)
        print("Goodbye!")
        return
 
    elif "load" in new_or_save:
        print("\n")
        Output.searchForGameOutput("Checking for existing saves")

        if path.exists("savedGame.pickle"):
            game = fromSave()
            game.setIsValid()

            time = game.time
            Output.welcomeBackToGame(game.user.current_place.getDescriptionBasedOnTimeAndVisitCount(time))

            print("Enter \'quit\' at the prompt to quit the game at any time.")
            gameLoop(game)
            print("Goodbye again!")
            return
        else: 
            print("No saves found. Exiting...")
            return

    else:
        print("You did not choose to start a new game or load a saved game. Exiting...") 
        return

main()
