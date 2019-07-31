import os
import sys
import re
import time
import random

##
##
## Strings for approaching door
##
b1 = "                "
z1 = b1 + "\n" + b1 + "\n" + "        _       \n       |_|      \n" + b1 + "\n" + b1 + "\n"
z2 = b1 + "\n" + b1 + "\n" + "        __      \n       |  |     \n       |__|     \n"+ b1 + "\n" + b1 + "\n" 
z3 = b1 + "\n" + "       ____     \n      |    |    \n      |  * |    \n      |____|    \n" + b1 + "\n"
z4 = "      ______    \n     |      |   \n     |      |   \n     |    * |   \n     |      |   \n     |______|   \n"
_approachDoor2 = [z1, z2, z3, z4]


##
##
## Strings for opening door
##
od0 = "      ______\n     |      |\n     |      |\n     |    * |\n     |      |\n     |______|\n"
od1 = "      ______\n     |     ||\n     |     ||\n     |    *||\n     |     ||\n     |_____||\n"
od2 = "      ______\n     |    | |\n     |    | |\n     |   *| |\n     |    | |\n     |____| |\n"
od3 = "      ______\n     |   |  |\n     |   |  |\n     |  *|  |\n     |   |  |\n     |___|  |\n"
od4 = "      ______\n     |  |   |\n     |  |   |\n     | .|   |\n     |  |   |\n     |__|   |\n"
od5 = "      ______\n     | |    |\n     | |    |\n     |.|    |\n     | |    |\n     |_|    |\n"
od6 = "      ______\n     | |    |\n     | |    |\n     |.|    |\n     | |    |\n     |/     |\n"
od7 = "      ______\n     | |    |\n     | |    |\n     | |    |\n     | /    |\n     |/     |\n"
od8 = "      /_____\n     ||     |\n     ||     |\n     ||     |\n     ||     |\n     ||     |\n"
od9 = "      ______\n     |      |\n     |      |\n     |      |\n     |      |\n     |      |\n"
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

    # print a helpful hint in yellow, result to defaul afterwards
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

    # print "look"
    @classmethod
    def print_look(self, look_description):
        length = len(look_description)

        # if message is long, break up into lines of ~60 characters 
        if length > 60:
            look_description = Output.break_up_long_message(look_description)

        # when not using a proper terminal (such as a GUI i.e. vscode), print in plain text
        if sys.stdin.isatty():
            sys.stdout.write(u'\u001b[38;5;$31m')
            for elem in look_description:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            sys.stdout.write('\033[0m')
            print("\n")
        else:
            print(look_description)

    # print "take"
    @classmethod
    def print_take(self, obj_name):

        msg = "You take the " + obj_name

        # when not using a proper terminal (such as a GUI i.e. vscode), print in plain text
        if sys.stdin.isatty():
            sys.stdout.write(u'\u001b[38;5;$12m')
            for elem in msg:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            sys.stdout.write('\033[0m')
            print("\n")
        else:
            print(msg)

    # print "drop"
    @classmethod
    def print_drop(self, obj_name):

        msg = "You drop the " + obj_name

        # when not using a proper terminal (such as a GUI i.e. vscode), print in plain text
        if sys.stdin.isatty():
            sys.stdout.write(u'\u001b[38;5;$11m')
            for elem in msg:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            sys.stdout.write('\033[0m')
            # sys.stdout.write(u'\u001b[38;5;$12m' + obj_name + "\n" +'\033[0m')
            print("\n")
        else:
            print(msg)

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

            # If that was the last word, append this line
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
        # Output.approachDoor(_approachDoor2)
        # Output.printFlashingDoor(od0, "green", 1, 0.1)
        print("\n\n\n\n\n\n")
        Output.openDoor(_openDoor, placeName)
        # Output.printFlashingDoor(od9, "green", 1, 0.1)
        time.sleep(0.1)
        Output.clearEntryWriting()
        sys.stdout.write(u"\u001b[0m") # reset

    @classmethod
    def approachDoor(self,_approachDoor):
        print("\n\n\n\n\n\n\n\n\n")
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.flush()
        i = 0
        for d in _approachDoor:
            time.sleep(0.08)
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
            # print("\t"+ door)
            print(door)
            sys.stdout.write(u"\u001b[0m") # reset
            time.sleep(speed)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\033[7A")
            sys.stdout.flush()
            # print("\t" + door)
            print(door)
            time.sleep(speed)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\033[7A")
            sys.stdout.flush()
            sys.stdout.write(u"\u001b" + c) # color
            # print("\t" + door)
            print(door)
            sys.stdout.write(u"\u001b[0m")
            i += 1
        sys.stdout.write(u"\u001b[0m") # reset

    @classmethod
    def openDoor(self,_openDoor, placeName):
        for d in _openDoor:
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\033[7A")
            sys.stdout.flush()
            print(d) 
            time.sleep(0.09) # slow part is door opening
            str = "Entering " + placeName
        str = "Entering " + placeName
        sys.stdout.flush()
        for elem in str:
            time.sleep(0.04)
            sys.stdout.write(elem)
            sys.stdout.flush()
        time.sleep(0.1)

    @classmethod
    def clearEntryWriting(self):
        # go back to beginning of line and write over with clear
        clr = "                                     "
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.write(clr)
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
            str = "That door is locked."
            # sys.stdout.write("\t")
            for elem in str:
                time.sleep(0.04)
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
                # sys.stdout.write("\t")
                for elem in strHint:
                    time.sleep(0.04)
                    sys.stdout.write(elem)
                    sys.stdout.flush()
                time.sleep(1) # pause after printing "hint"
                for elem in strHint2:
                    time.sleep(0.04)
                    sys.stdout.write(elem)
                    sys.stdout.flush()
                time.sleep(1) # pause before printing key
                Output.printKey(keyline1, keyline2, keyline3)
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
        length = len(placeDescription)
        if length > 60:
            placeDescription = Output.break_up_long_message(placeDescription)

        welcome = "You are now in the " + placeName

        if sys.stdin.isatty():
            sys.stdout.write(u'\u001b[38;5;$146m')
            for elem in placeDescription:
                time.sleep(0.04)
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
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write(u'\u001b[38;5;$146m')
            for elem in placeDescription:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            sys.stdout.write(u"\u001b[0m")
            print("\n")
            sys.stdout.flush()
        else:
            print(welcome)
            print(placeDescription)
