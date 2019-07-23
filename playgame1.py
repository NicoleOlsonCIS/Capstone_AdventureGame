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

# playgame1.py works with v6 of the game engine

# reads in place information from room file
def loadPlaceData(place_obj, filename):

    dayDescrip = ""
    nightDescrip = ""
 
    # build path to data file
    fpath = "./Game_Files/" + filename
 
    # read file line by line
    with open(fpath) as f:
        read_data = f.read()
        data_chunks = read_data.split("***\n")
    
    # day and night descriptions
    dayDescrip = data_chunks[0].rstrip("\n")
    nightDescrip = data_chunks[1].rstrip("\n")

    # add descriptions to place_obj dictionary
    place_obj.description["day"] = dayDescrip
    place_obj.description["night"] = nightDescrip 

    # load feature information and create/add Things
    if "no features" not in data_chunks[2]:
        featurenames = data_chunks[2].split("\n")
        for feature in featurenames:
            feature = feature.rstrip()
            feature = feature.lstrip()
            if feature != "":
                newthing = g.Thing(feature, feature + " descrip", place_obj, False)
                place_obj.addThing(newthing)

    # load object information and create/add Things
    if "no objects" not in data_chunks[3]:
        objnames = data_chunks[3].split("\n")
        for obj in objnames:
            obj = obj.rstrip()
            obj = obj.lstrip()
            if obj != "":
                newthing = g.Thing(obj, obj + " descrip", place_obj, True)
                place_obj.addThing(newthing)


def buildGame():

    # start game at 7 am
    game = g.Game(1,7)

    descriptions = ["place during day", "place during night"]

    # populate room topology 
    place1 = g.Place(game, "Train Platform", descriptions, [None, "Fields", None, None, None, None, "Station-House", None, None, None])
    place2 = g.Place(game, "Station-House", descriptions, [None, None, "Train Platform", None, None, None, None, None, None, None])
    place3 = g.Place(game, "Fields", descriptions, ["Front Manor Grounds", None, None, None, None, "Train Platform", None, None, None, None])
    place4 = g.Place(game, "Front Manor Grounds", descriptions, ["Foyer", None, None, None, "Fields", None, None, "Ash Grove", None, None])
    place5 = g.Place(game, "Foyer", descriptions, ["Downstairs Hallway 1", None, None, None, "Front Manor Grounds", None, "Cloakroom", None, "Upstairs Hallway 1", None])
    place6 = g.Place(game, "Upstairs Hallway 1", descriptions, ["Upstairs Hallway 2", None, None, None, None, None, "Spare Room", None, None, "Foyer"])
    place7 = g.Place(game, "Upstairs Hallway 2", descriptions, ["Upstairs Hallway 3", None, "Small Lavatory", None, "Upstairs Hallway 1", None, "Bedroom", None, None, None])
    place8 = g.Place(game, "Upstairs Hallway 3", descriptions, ["Upstairs Hallway 4", None, "Library", None, "Upstairs Hallway 2", None, None, None, None, None])
    place9 = g.Place(game, "Upstairs Hallway 4", descriptions, ["Upstairs Hallway 5", None, "Study", None, "Upstairs Hallway 3", None, "Large Bedroom", None, None, None])
    place10 = g.Place(game, "Upstairs Hallway 5", descriptions, ["Servants\' Stair Top", None, None, None, "Upstairs Hallway 4", None, None, None, None, None])
    place11 = g.Place(game, "Spare Room", descriptions, [None, None, "Upstairs Hallway 1", None, None, None, None, None, None, None])  
    place12 = g.Place(game, "Small Lavatory", descriptions, [None, None, None, None, None, None, "Upstairs Hallway 2", None, None, None])
    place13 = g.Place(game, "Bedroom", descriptions, [None, None, "Upstairs Hallway 2", None, None, None, None, None, None, None]) 
    place14 = g.Place(game, "Library", descriptions, [None, None, None, None, None, None, "Upstairs Hallway 3", None, None, None])
    place15 = g.Place(game, "Study", descriptions, [None, None, None, None, None, None, "Upstairs Hallway 4", None, None, None])
    place16 = g.Place(game, "Large Bedroom", descriptions, [None, None, "Upstairs Hallway 4", None, None, None, None, None, None, None])
    place17 = g.Place(game, "Servants\' Stair Top", descriptions, [None, None, None, None, "Upstairs Hallway 5", None, None, None, None, "Servants\' Stair Bottom"])
    place18 = g.Place(game, "Servants\' Stair Bottom", descriptions, [None, None, None, None, "Downstairs Hallway 3", None, None, None, "Servants\' Stair Top", None])    
    place19 = g.Place(game, "Downstairs Hallway 3", descriptions, ["Servants\' Stair Bottom", None, None, None, "Downstairs Hallway 2", None, None, None, None, None])
    place20 = g.Place(game, "Downstairs Hallway 2", descriptions, ["Downstairs Hallway 3", None, "Kitchen", None, "Downstairs Hallway 1", None, "Servants\' Quarters", None, None, None])
    place21 = g.Place(game, "Downstairs Hallway 1", descriptions, ["Downstairs Hallway 2", None, "Dining Room", None, "Foyer", None, "Drawing Room", None, None, None])
    place22 = g.Place(game, "Kitchen", descriptions, [None, None, None, None, None, None, "Downstairs Hallway 2", None, None, None])
    place23 = g.Place(game, "Servants\' Quarters", descriptions, [None, None, "Downstairs Hallway 2", None, None, None, None, None, None, None])
    place24 = g.Place(game, "Drawing Room", descriptions, [None, None, "Downstairs Hallway 1", None, None, None, None, None, None, None])
    place25 = g.Place(game, "Dining Room", descriptions, [None, None, None, None, None, None, "Downstairs Hallway 1", None, None, None])
    place26 = g.Place(game, "Cloakroom", descriptions, [None, None, "Foyer", None, None, None, None, None, None, None])
    place27 = g.Place(game, "Ash Grove", descriptions, ["Rear Manor Grounds", None, None, "Front Manor Grounds", None, None, None, None, None, None]) 
    place28 = g.Place(game, "Rear Manor Grounds", descriptions, [None, None, "Root Cellar", None, "Ash Grove", None, None, None, None, None]) 
    place29 = g.Place(game, "Root Cellar", descriptions, [None, None, None, None, None, None, "Rear Manor Grounds", None, None, None])

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
       
        # set up parser
        playparser = p.Parser()

        # start playing
        while True:

            game.user.printUser(game) 
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
