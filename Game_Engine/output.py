import os
import sys
import re
import time

##
##
## Strings for approaching door
##
b1 = "                "
z1 = b1 + "\n\t" + b1 + "\n\t" + "        _       \n\t       |_|      \n\t" + b1 + "\n\t" + b1 + "\n\t"
z2 = b1 + "\n\t" + b1 + "\n\t" + "        __      \n\t       |  |     \n\t       |__|     \n\t"+ b1 + "\n\t" + b1 + "\n\t" 
z3 = b1 + "\n\t" + "       ____     \n\t      |    |    \n\t      |  * |    \n\t      |____|    \n\t" + b1 + "\n\t"
z4 = "\t"+"      ______    \n\t     |      |   \n\t     |      |   \n\t     |    * |   \n\t     |      |   \n\t     |______|   \n\t"
_approachDoor2 = [z1, z2, z3, z4]


##
##
## Strings for opening door
##
od0 = "      ______\n\t     |      |\n\t     |      |\n\t     |    * |\n\t     |      |\n\t     |______|\n\t"
od1 = "      ______\n\t     |     ||\n\t     |     ||\n\t     |    *||\n\t     |     ||\n\t     |_____||\n\t"
od2 = "      ______\n\t     |    | |\n\t     |    | |\n\t     |   *| |\n\t     |    | |\n\t     |____| |\n\t"
od3 = "      ______\n\t     |   |  |\n\t     |   |  |\n\t     |  *|  |\n\t     |   |  |\n\t     |___|  |\n\t"
od4 = "      ______\n\t     |  |   |\n\t     |  |   |\n\t     | .|   |\n\t     |  |   |\n\t     |__|   |\n\t"
od5 = "      ______\n\t     | |    |\n\t     | |    |\n\t     |.|    |\n\t     | |    |\n\t     |_|    |\n\t"
od6 = "      ______\n\t     | |    |\n\t     | |    |\n\t     |.|    |\n\t     | |    |\n\t     |/     |\n\t"
od7 = "      ______\n\t     | |    |\n\t     | |    |\n\t     | |    |\n\t     | /    |\n\t     |/     |\n\t"
od8 = "      /_____\n\t     ||     |\n\t     ||     |\n\t     ||     |\n\t     ||     |\n\t     ||     |\n\t"
od9 = "      ______\n\t     |      |\n\t     |      |\n\t     |      |\n\t     |      |\n\t     |      |\n\t"
_openDoor = [od0, od1, od2, od3, od4, od5, od6, od7, od8, od9]

##
##
## Strings for key
##
k1= "    ___      _"    #(gold text)

k2p1= "   |"			#(gold text)
k2p2= " + "             #(white background, black text)
k2p3= "|____||"         #(gold text)

k3p1= "   |" # (gold text)
k3p2= "_" #(white background, gold text)
k3p3= "*" #(white background, black text)
k3p4= "_" #(white background, gold text)
k3p5= "|" #gold text


keyline1 = [k1]
keyline2 = [k2p1, k2p2, k2p3]
keyline3 = [k3p1, k3p2, k3p3, k3p4, k3p5]

# static class
class Output(object):

    # print an error message in red, reset to default afterwards
    @classmethod
    def print_error(self, error_message):

        length = len(error_message)

        # if message is long, break up into lines of ~60 characters 
        if length > 60:
            error_message = Output.break_up_long_message(error_message)

        # when not using a proper terminal (such as a GUI i.e. vscode), print in plain text
        if sys.stdin.isatty():
            print(u'\u001b[31m' + error_message + '\033[0m')
        else:
            print(error_message)

    # print a helpful hint in purple, result to defaul afterwards
    @classmethod
    def print_input_hint(self, hint_message):
        length = len(hint_message)

        # if message is long, break up into lines of ~60 characters 
        if length > 60:
            hint_message = Output.break_up_long_message(hint_message)

        # when not using a proper terminal (such as a GUI i.e. vscode), print in plain text
        if sys.stdin.isatty():
            print(u'\u001b[38;5;$220m' + hint_message + '\033[0m')
        else:
            print(hint_message)

    @classmethod
    # helper functions, called if a line is > 60 characters
    def break_up_long_message(self, extended_message):

        # split at white space, turn it into an array of words
        words = extended_message.split()
        count = len(words)

        # array of lines, where lines are max 60 characters
        lines = []
        line = ""

        for w in words:
             # get the length of a word
            l = len(w)
            # get the current length of the line
            l2 = len(line)

            if l2 + l > 60:
                # add the line even though it is less than 60
                lines.append(line)
                # resert the line variable to the new word
                line = w
                count -= 1
            # otherwise, add the word to the line
            else:
                line = line + " " + w
                count -= 1
                if count == 0:
                    lines.append(line)

        # now append the lines to one another with a "\n" between lines
        result = ""
        for l in lines: 
            result = result + "\n" + l

        return result

    # call when door is unlocked and you are moving into a new room
    @classmethod
    def newPlaceWithDoor(self, placeName):

        # when not using a proper terminal (such as a GUI i.e. vscode), print in plain text
        if not sys.stdin.isatty():
            return

        # otherwise, do animation
        Output.approachDoor(_approachDoor2)
        Output.printFlashingDoor(od0, "green", 1, 0.2)
        Output.openDoor(_openDoor, placeName)
        Output.printFlashingDoor(od9, "green", 1, 0.4)
        time.sleep(0.5)
        Output.clearEntryWriting()
        sys.stdout.write(u"\u001b[0m") # reset
        # print("\n\n")

    @classmethod
    def approachDoor(self,_approachDoor):
        print("\n\n\n\n\n\n\n\n\n\n\n")
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.flush()
        i = 0
        for d in _approachDoor:
            if i == 0:
                print("\t") # print tabs before the first line printed

            time.sleep(0.3)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\033[8A") # up 8
            sys.stdout.flush()
            print(d)
            i += 1

    @classmethod 
    def printFlashingDoor(self,door, color, num, speed):
        i = 0
        c = ""

        if color == "green":
             c = "[32;1m"
        elif color == "red":
            c = "[31;1m"

        while i < num:
            time.sleep(speed)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\033[7A")
            sys.stdout.flush()
            sys.stdout.write(u"\u001b" + c) # color
            print("\t"+ door)
            sys.stdout.write(u"\u001b[0m") # reset
            time.sleep(speed)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\033[7A")
            sys.stdout.flush()
            print("\t" + door)
            time.sleep(speed)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\033[7A")
            sys.stdout.flush()
            sys.stdout.write(u"\u001b" + c) # color
            print("\t" + door)
            sys.stdout.write(u"\u001b[0m")
            i += 1
        sys.stdout.write(u"\u001b[0m") # reset

    @classmethod
    def openDoor(self,_openDoor, placeName):
        #print("\n\n\n\n\n\n\n")
        for d in _openDoor:
            time.sleep(0.1)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\033[7A")
            sys.stdout.flush()
            print("\t" + d)
            time.sleep(0.5)
            str = "\tEntering " + placeName
            sys.stdout.write(u"\u001b[32;1m")
        for elem in str:
            time.sleep(0.03)
            sys.stdout.write(elem)
            sys.stdout.flush()
            time.sleep(0.1)

    @classmethod
    def clearEntryWriting(self):
        # go back to beginning of line and write over with clear
        clr = "                          "
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.write("\t" + clr)
        sys.stdout.write(u"\u001b[0m")

    @classmethod
    # clear a space 
    def clearSpace(self,upCount):
        bl = "                                                  "
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.write(u"\033[" + upCount + "A")
        for i in range (0, int(upCount)):
            print(bl)
        sys.stdout.write(u"\033[" + upCount + "A")
        sys.stdout.write(u"\u001b[1000D")

    @classmethod
    def doorIsLocked(self, placeName, hint):
        if sys.stdin.isatty():
            Output.approachDoor(_approachDoor2)
            time.sleep(1)
            Output.printFlashingDoor(od0, "red", 2, 0.4)
            str = "The door to the " + placeName + " is locked."
            sys.stdout.write("\t")
            for elem in str:
                time.sleep(0.07)
                sys.stdout.write(elem)
                sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\u001b[0m") # reset

            # for instance, if it's the first time the user encounters a locked door
            if hint:
                # clear the door by moving up and printing clear lines 
                #clearSpace("16")
                print("\n")
                strHint = "Hint:"
                strHint2 = " You need a key\n"
                sys.stdout.write("\t")
                for elem in strHint:
                    time.sleep(0.07)
                    sys.stdout.write(elem)
                    sys.stdout.flush()
                time.sleep(1) # pause after printing "hint"
                for elem in strHint2:
                    time.sleep(0.07)
                    sys.stdout.write(elem)
                    sys.stdout.flush()
                time.sleep(1) # pause before printing key
                Output.printKey(keyline1, keyline2, keyline3)
                time.sleep(2)
                print("\n\n\n")
        
            else:
                print("\n\n\n")
        else:
            print("The door to the " + placeName + " is locked.")

    @classmethod
    def printKey(self,keyline1, keyline2, keyline3):
        # print keyline1 #226 and then reset
        sys.stdout.write(u"\u001b[33;1m")
        sys.stdout.write("\t" + keyline1[0])
        sys.stdout.write(u"\u001b[0m") # reset
        sys.stdout.write("\n")

        # print keyline2
        sys.stdout.write(u"\u001b[33;1m") # yellow text
        sys.stdout.write("\t" + keyline2[0])
        sys.stdout.write(u"\u001b[0m") # reset

        sys.stdout.write(u"\u001b[47m") # white background
        sys.stdout.write(u"\u001b[30m") # black text
        sys.stdout.write(keyline2[1])
        sys.stdout.write(u"\u001b[0m") # reset

        sys.stdout.write(u"\u001b[33;1m") # yellow text
        sys.stdout.write(keyline2[2])
        sys.stdout.write(u"\u001b[0m") # reset
        sys.stdout.write("\n")

        # print keyline3
        sys.stdout.write(u"\u001b[33;1m") # yellow text
        sys.stdout.write("\t" + keyline3[0])
        sys.stdout.write(u"\u001b[47m") # add white background
        sys.stdout.write(u"\u001b[30m") # change text black
        sys.stdout.write(keyline3[1])
        sys.stdout.write(keyline3[2])
        #sys.stdout.write(u"\u001b[33;1m") # change back to yellow text
        sys.stdout.write(keyline3[3])
        sys.stdout.write(u"\u001b[0m") # reset
        sys.stdout.write(u"\u001b[33;1m") # yellow text
        sys.stdout.write(keyline3[4])
        sys.stdout.write(u"\u001b[0m") # reset
        sys.stdout.write("\n\n\n")

    @classmethod
    def orientUser(self, placeName, placeDescription):
        print("Trace 3")
        length = len(placeDescription)
        if length > 60:
            placeDescription = Output.break_up_long_message(placeDescription)
        # print slowly and in green
        # when not using a proper terminal (such as a GUI i.e. vscode), print in plain text

        welcome = "You are now in the " + placeName

        if sys.stdin.isatty():
            #sys.stdout.write(u'\u001b[38;5;$147m')
            #for elem in welcome:
            #    time.sleep(0.05)
            #    sys.stdout.write(elem)
            #    sys.stdout.flush()
            #sys.stdout.write("\n")
            sys.stdout.write(u'\u001b[38;5;$146m')
            for elem in placeDescription:
                time.sleep(0.05)
                sys.stdout.write(elem)
                sys.stdout.flush()
            sys.stdout.write(u"\u001b[0m")
            print("\n")
            sys.stdout.flush()
        else:
            print(welcome)
            print(placeDescription)

    @classmethod
    def welcomeToGame(self, placeDescription):
        length = len(placeDescription)
        if length > 60:
            placeDescription = Output.break_up_long_message(placeDescription)

        welcome = 'Welcome user. We wish you luck on your journey.'

        if sys.stdin.isatty():
            sys.stdout.write(u'\u001b[38;5;$147m')
            for elem in welcome:
                time.sleep(0.05)
                sys.stdout.write(elem)
                sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write(u'\u001b[38;5;$146m')
            for elem in placeDescription:
                time.sleep(0.05)
                sys.stdout.write(elem)
                sys.stdout.flush()
            sys.stdout.write(u"\u001b[0m")
            print("\n")
            sys.stdout.flush()
        else:
            print(welcome)
            print(placeDescription)
