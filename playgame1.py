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

# playgame1.py works with v6 of the game engine

# reads in place information from room file
def loadPlaceData(place_obj, filename):

    # build path to data file
    fpath = "./Game_Files/" + filename
 
    # read file line by line
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

    nextIdxIncrement = 1

    # load feature information and create/add Things
    if "no features" not in data_chunks[6]:
        featurenames = data_chunks[6].split("\n")
        
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

                # separate out by ### delimeter
                fd_arr = fd.split("###")
                
                # find out how many descriptions have been entered
                numDescriptions = len(fd_arr)

                # if there is less than 5, fill up to 5 by copying the last one over
                while numDescriptions < 5:
                    fd_arr.append(fd_arr[numDescriptions - 1])
                    numDescriptions = len(fd_arr)

                newthing = g.Thing(feature, fd_arr, place_obj, False)
                place_obj.addThing(newthing)

                count += 1

    # load object information and create/add Things
    # v12 if there were no features, then nextIdxIncrement is 1 and we are on chunk 7
    if "no objects" not in data_chunks[6 + nextIdxIncrement]:

        idx = 6 + nextIdxIncrement
        objnames = data_chunks[idx].split("\n")

        # debug
        print("Number of objects: ")
        size = len(objnames)
        print(size)

        # debug
        for o in objnames:
            print("Object: " + o)

        # get the count of objects
        numObjects = len(objnames)

        # figure out where the next type section starts based on how many sections there will be for objects
        # for instance, if there is 1 object, then we index past that object's descriptions
        nextIdxIncrement = numObjects

        objectDescriptions = []
        count = 0

        # starting in the next *** section, get the corresponding descriptions for each object
        while count < numObjects: 
            objectDescriptions.append(data_chunks[idx + count])
            count += 1

        count = 0
        for obj in objnames:
            obj = obj.rstrip()
            obj = obj.lstrip()
            if obj != "":
                # get the description block for this object
                od = objectDescriptions[count]

                # separate out by ### delimeter
                od_arr = od.split("###")
                
                # find out how many descriptions have been entered
                numDescriptions = len(od_arr)

                # if there is less than 5, fill up to 5 by copying the last one over
                while numDescriptions < 5:
                    od_arr.append(od_arr[numDescriptions - 1])
                    numDescriptions = len(od_arr)
                newthing = g.Thing(obj, od_arr, place_obj, True)
                place_obj.addThing(newthing)


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
    place9 = g.Place(game, "Upstairs Hallway 4", day, night, ["Upstairs Hallway 5", None, "Study", None, "Upstairs Hallway 3", None, "Large Bedroom", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
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
    place20 = g.Place(game, "Downstairs Hallway 2", day, night, ["Downstairs Hallway 3", None, "Kitchen", None, "Downstairs Hallway 1", None, "Servants\' Quarters", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place21 = g.Place(game, "Downstairs Hallway 1", day, night, ["Downstairs Hallway 2", None, "Dining Room", None, "Foyer", None, "Drawing Room", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place22 = g.Place(game, "Kitchen", day, night, [None, None, None, None, None, None, "Downstairs Hallway 2", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place23 = g.Place(game, "Servants\' Quarters", day, night, [None, None, "Downstairs Hallway 2", None, None, None, None, None, None, None], None, {"n": None, "ne": None, "e": "unlocked", "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place24 = g.Place(game, "Drawing Room", day, night, [None, None, "Downstairs Hallway 1", None, None, None, None, None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place25 = g.Place(game, "Dining Room", day, night, [None, None, None, None, None, None, "Downstairs Hallway 1", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place26 = g.Place(game, "Cloakroom", day, night, [None, None, "Foyer", None, None, None, None, None, None, None], None, {"n": None, "ne": None, "e": "unlocked", "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})
    place27 = g.Place(game, "Ash Grove", day, night, ["Rear Manor Grounds", None, None, "Front Manor Grounds", None, None, None, None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None}) 
    place28 = g.Place(game, "Rear Manor Grounds", day, night, [None, None, "Root Cellar", None, "Ash Grove", None, None, None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None}) 
    place29 = g.Place(game, "Root Cellar", day, night, [None, None, None, None, None, None, "Rear Manor Grounds", None, None, None], None, {"n": None, "ne": None, "e": None, "se": None, "s": None, "sw": None, "w": None, "nw": None, "u": None, "d": None})

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
    #loadPlaceData(place3, "fields.txt")
    #loadPlaceData(place4, "frontmanorgrounds.txt")

    # associate user with game 
    game.setUser(user)

    return game



def main():

    print("Welcome! Would you like to start a new game or load a saved game? new/load")
    new_or_save = input("> ")

    if "new" in new_or_save:  
        game = buildGame()
        game.setIsValid()
        Output.welcomeToGame(game.user.current_place.day[0]) # start day first visit
       
        # set up parser
        playparser = p.Parser()

        # start playing
        while True:

            # game.user.printUser(game) 
            received = input("> ")
            if "quit" in received:
                break      
            else:
                playaction = a.Action()
                playaction = playparser.parseInput(received)
                print(playaction.verb, playaction.direction, playaction.direct_obj, playaction.indirect_obj) 
                game.fromParserToGame(playaction)
 
    elif "load" in new_or_save:
        print("Checking for existing saves...")
        # loading code here

    else:
        print("You did not choose to start a new game or load a saved game. Exiting...") 
        return


main()
