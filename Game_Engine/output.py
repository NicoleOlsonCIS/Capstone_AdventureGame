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

##
##
## Strings for speech bubbles
##
##
sb1 = " ____________________________"
sb2 = "/" + "                            " + "\\"
sb3 = "| "
sb4 = "\\" + "___    _____________________" + "/"
sb5 = "    | " + "/"
sb6 = "    |" + "/"
sb7 = "   |"


# archway 1

a1 ="          -__-___---_--_"
a2 ="         -__--___--_--_-_"
a3 ="        -__-___-___---_--_"
a4 ="      -__-_-/////\\\\-_--__  "
a5 ="     __--  /////\\\\\\\\-__--__"
a6 ="    __--- ///// \\\\\\\\\\-__-_--_"
a7 =" _-___---/////   \\\\\\\\\\--_--_-_"
a8 ="-__-___--|||||   |||||-__-___-- "
a9 ="-__--___-|||||   |||||-__---___-"
a10="-__-_--_-|||||   |||||-__--__---"
a11="-__-___--|||||   |||||-__--___--"
a12="-__-_--_-||||/   \\||||-__-___--_"
a13="_________|||/     \\|||__________"

archway1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13]



# static class
class Output(object):

    # print an error message in red, reset to default afterwards
    @classmethod
    def print_error(self, error_message):

        length = len(error_message)

        # if message is long, break up into lines of ~60 characters 
        if length > 60:
            error_message = Output.break_up_long_message(error_message, 60, False)

        # when not using a proper terminal (such as a GUI i.e. vscode), print in plain text
        if sys.stdin.isatty():
            print(u'\u001b[31m' + error_message + '\033[0m')
        else:
            print(error_message)

    # print a helpful hint in yellow, result to defaul afterwards
    @classmethod
    def print_input_hint(self, hint_message):
        # hint_message = "Hint: " + hint_message
        length = len(hint_message)

        # if message is long, break up into lines of ~60 characters 
        if length > 60:
            hint_message = Output.break_up_long_message(hint_message, 60, False)

        # when not using a proper terminal (such as a GUI i.e. vscode), print in plain text
        if sys.stdin.isatty():
            sys.stdout.write(u'\u001b[38;5;$220m')
            for elem in hint_message:
                sys.stdout.write(elem)
                time.sleep(0.04)
                sys.stdout.flush()
            print('\033[0m') # reset color
        else:
            print(hint_message)

    # print "look"
    @classmethod
    def print_look(self, look_description):
        length = len(look_description)

        # if message is long, break up into lines of ~60 characters 
        if length > 60:
            look_description = Output.break_up_long_message(look_description, 60, False)

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

    # user moves through something other than door
    #@classmethod 
    #def move_NotDoor(self, direction, newPlaceName, oldPlaceName, passageType) # eg archway, stairs

    # print a speach bubble + a newline, return full bubble
    @classmethod
    def print_bubble(self, speech):
        fullBubble = sb1 + "\n" + sb2 + "\n"
        # print the top of the bubble
        sys.stdout.write(u'\u001b[38;5;$244m') # speech bubble color
        print(sb1 + "\n" + sb2)
        count = len(speech)
        lineNum = 0
        while lineNum < count:
            # fill the line to 24 characters by adding spaces
            while len(speech[lineNum]) < 24:
                speech[lineNum] = speech[lineNum] + " "

            # print the start of the bubble
            sys.stdout.write(sb3)
            fullBubble = fullBubble + sb3

            # print the line
            sys.stdout.write(u'\u001b[38;5;$206m') # change to text color
            sys.stdout.write(speech[lineNum])
            fullBubble = fullBubble + speech[lineNum]
            time.sleep(0.2)
            
            # print the end of the bubble + newline
            sys.stdout.write(u'\u001b[38;5;$244m') # speech bubble color
            print(sb7)
            fullBubble = fullBubble + sb7 + "\n"

            # increment index
            lineNum += 1

        # print the bottom of the bubble
        print(sb4)
        time.sleep(0.2)
        print(sb5 + "\n" + sb6)
        fullBubble = fullBubble + sb4 + "\n" + sb5 + "\n" + sb6 + "\n"
        return fullBubble

    # print conversations
    @classmethod
    def print_talk(self, characters_message, person_name):

        print("\n")

        # if there is a person name, print that first
        if person_name != None: 
            d = "You talk to " + person_name
            for elem in d:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            print("\n")
            time.sleep(0.5)

        # break it up in terms of "|||" (these are conversation parts that go together)
        chunks = characters_message.split("|||")

        # for each piece, parse the pattern (in terms of ^)
        for c in chunks:
            # break up in terms of ^
            components = c.split("^")

            # if there is only 1 component, then it is a speach bubble
            if len(components) == 1:
                full = ""

                # get rid of "#"
                speech = ""
                for s in components[0]:
                    if s != "#":
                        speech = speech + s

                # separate into lines of length <= 24 if necessary
                length = len(speech)
                speaking_lines = []
                if length > 24:
                    speaking_lines = Output.getLines(speech, 24)
                else:
                    speaking_lines.append(speech)
                
                # send to print function
                # print the speech bubble and a newline
                bubble = Output.print_bubble(speaking_lines)
                print("\n")
                time.sleep(1)

                full += bubble  + "\n\n"

                # fade the printed things
                Output.fadeString(full)

            # it will be a speaking and description pair (never two speaking and never two description)
            elif len(components) == 2:
                speaking = ""
                description = ""
                comesFirst = ""
                full = ""

                component1 = components[0]
                component2 = components[1]

                if component1[0] == "#":
                    speaking = component1
                    description = component2
                    comesFirst = "Speaking"
                else:
                    speaking = component2
                    description = component1
                    comesFirst = "Description"

                # get rid of "#"
                speech = ""
                for s in speaking:
                    if s != "#":
                        speech = speech + s

                # add the appropriate newlines in the description and record the hieght
                # the width of the description is 32 characters
                if len(description) > 32:
                    description = Output.break_up_long_message(description, 32, False)

                # add the appropriate newlines in the speaking and record the height
                # the width of the text inside speach bubbles is 32 characters
                length = len(speech)
                speaking_lines = []
                if length > 24:
                    speaking_lines = Output.getLines(speech, 24)
                else:
                    speaking_lines.append(speech)

                # do the printing
                if comesFirst == "Description": 
                    # print the description with a newline
                    # change color
                    sys.stdout.write(u'\u001b[38;5;$63m')
                    for elem in description:
                        time.sleep(0.04)
                        sys.stdout.write(elem)
                        sys.stdout.flush()
                    print("\n")
                    full = description + "\n\n"

                    # print the speech bubble and a newline
                    bubble = Output.print_bubble(speaking_lines)
                    print("\n")
                    time.sleep(1)

                    full = full + bubble + "\n\n"
                
                else:
                    # print the speech bubble with a newline
                    bubble = Output.print_bubble(speaking_lines)
                    print("\n") # print "\n" 
                    full += bubble + "\n\n"

                    # print the description with a newline
                    sys.stdout.write(u'\u001b[38;5;$63m')
                    for elem in description:
                        time.sleep(0.04)
                        sys.stdout.write(elem)
                        sys.stdout.flush()
                    print("\n")
                    full = full + description + "\n\n"
                    time.sleep(1)
                
                # fade the printed things
                Output.fadeString(full)
        sys.stdout.write(u"\u001b[0m") # reset

    # fade string to black
    @classmethod
    def fadeString(self, stringToFade):
        #print(stringToFade)
        time.sleep(1)
        lineCount = Output.countNewLines(stringToFade)
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.write(u"\033[" + str(lineCount-1) + "A") # up the line count
        code = 255
        while code > 233:
            sys.stdout.write(u'\u001b[38;5;' + str(code) +'m')
            sys.stdout.write(stringToFade)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\033[" + str(lineCount-1) + "A") # up the line count
            code -= 1
            time.sleep(0.04)
        sys.stdout.write(u'\u001b[38;5;232m')
        sys.stdout.write(stringToFade)
        #reset
        sys.stdout.write(u"\u001b[0m")
        Output.clearTalk(lineCount)


    # clear number of lines (helper method)
    @classmethod
    def clearTalk(self, height):
        height -= 2
        pc = "                                                                     "
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.write(u"\033[" + str(height + 1) + "A") # up height
        # print clear lines
        for i in range(1, height):
            print(pc)
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.write(u"\033[" + str(height - 1) + "A") # up height

    # count new lines in str (helper method)
    @classmethod
    def countNewLines(self, line):
        numNewLines = line.split("\n")
        return len(numNewLines)

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

#  @classmethod
#    def print_archway(self):
#        if sys.stdin.isatty():
#            for a in archway1:
#                # reset previous
#                previousElem1 = " "
#                previousElem2 = " "
#                previousElem3 = " "
#                previousElem4 = " "
#                for elem in a:
#                    # random (of 3) light color grey background
#                    if elem == "-":
#                        color = random.randint(1,4)
#                        if color == 1:
#                            # set background and text color #248
#                        elif color == 2:
#                            # set background and text color #249
#                        elif color == 3:
#                            # set background and text color #250
#                        
#                    # random (of 3) dark color grey background
#                    elif elem == "_":
#                        color = random.randint(1,4)
#                        if color == 1:
#                            # set background and text color #243
#                        elif color == 2:
#                            # set background and text color #244
#                        elif color == 3: 
#                            # set background and text color #245
#
#                    # color based on previous (darker color upon consequetive)
#                    elif elem == "/":
#
#                    # color based on previous (lighter color upon consequtive)
#                    elif elem == "\\":#
#
#                    # color based on previous (if previous was not space, then light to dark, else light to dark)
#                   elif elem == "|":
#                    
#                    # shift the previous
#                    previousElem4 = previousElem3
#                    previousElem3 = previousElem2
#                    previousElem2 = previousElem1
#                    previousElem1 = elem#
#
#                print("\n") # new line
#        else:
#            for a in archway1:
#            print(a)


    @classmethod
    # helper functions, break up message to lines of specified length and whether it should be indented
    def break_up_long_message(self, extended_message, length, indent = None):

        if indent == None:
            indent = True
        # split at white space, turn it into an array of words
        words = extended_message.split()
        count = len(words)

        # array of lines, where lines are max 60 characters
        lines = []
        line = ""
        first = True

        for w in words:
             # get the length of a word
            l = len(w)
            # get the current length of the line
            l2 = len(line)

            if l2 + l > length:
                # add the line even though it is less than length
                lines.append(line)
                # resert the line variable to the new word
                line = w
                count -= 1
            # otherwise, add the word to the line
            else:
                if first == True and indent == False:
                    line = line + w
                    count -= 1
                    first = False
                else:
                    line = line + " " + w
                    count -= 1
                    first = False

            # If that was the last word, append this line
            if count == 0:
                lines.append(line)

        # now append the lines to one another with a "\n" between lines
        result = ""
        count = 0
        for l in lines:
            if len(lines) > 1:
                if count > 0:
                    result = result + "\n" + l
                    count += 1
                else:
                    result = result + l
                    count += 1
            else:
                result = result + l

        return result

    @classmethod
    # helper function, called for conversation messages, returns array of lines <=size char each
    def getLines(self, message, size):

        # split at white space, turn it into an array of words
        words = message.split()
        count = len(words)

        lines = []
        line = ""

        for w in words:
             # get the length of a word
            l = len(w)
            # get the current length of the line
            l2 = len(line)

            if l2 + l > size:
                # add the line to the [] without adding the new word
                lines.append(line)
                # reset the line variable to the new word
                line = w
                count -= 1
            # otherwise, add the word to the line
            else:
                line = line + " " + w
                count -= 1

            # If that was the last word, append this line
            if count == 0:
                lines.append(line)

        return lines

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
            time.sleep(0.05)
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
            time.sleep(speed) # pause
            sys.stdout.write(u"\u001b[1000D") # move cursor left
            sys.stdout.write(u"\033[7A") # move cursor up
            sys.stdout.flush() # clear std out
            sys.stdout.write(u"\u001b" + c) # change color
            print(door) # print the door
            sys.stdout.write(u"\u001b[0m") # reset the color
            i += 1

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
            time.sleep(0.4)
            Output.printFlashingDoor(od0, "red", 4, 0.2)
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
        sys.stdout.write(u"\u001b[250;1m")
        sys.stdout.write(keyline1[0])
        sys.stdout.write(u"\u001b[0m") # reset
        sys.stdout.write("\n")

        # print keyline2
        sys.stdout.write(u"\u001b[250;1m") # yellow text
        sys.stdout.write(keyline2[0])
        sys.stdout.write(u"\u001b[0m") # reset

        sys.stdout.write(u"\u001b[47m") # white background
        sys.stdout.write(u"\u001b[30m") # black text
        sys.stdout.write(keyline2[1])
        sys.stdout.write(u"\u001b[0m") # reset

        sys.stdout.write(u"\u001b[250;1m") # yellow text
        sys.stdout.write(keyline2[2])
        sys.stdout.write(u"\u001b[0m") # reset
        sys.stdout.write("\n")

        # print keyline3
        sys.stdout.write(u"\u001b[250;1m") # yellow text
        sys.stdout.write(keyline3[0])
        sys.stdout.write(u"\u001b[47m") # add white background
        sys.stdout.write(u"\u001b[30m") # change text black
        sys.stdout.write(keyline3[1])
        sys.stdout.write(keyline3[2])
        sys.stdout.write(keyline3[3])
        sys.stdout.write(u"\u001b[0m") # reset
        sys.stdout.write(u"\u001b[250;1m") # yellow text
        sys.stdout.write(keyline3[4])
        sys.stdout.write(u"\u001b[0m") # reset
        sys.stdout.write("\n\n\n")

    @classmethod
    def orientUser(self, placeName, placeDescription):
        length = len(placeDescription)
        if length > 60:
            placeDescription = Output.break_up_long_message(placeDescription, 60, True)

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
            placeDescription = Output.break_up_long_message(placeDescription, 60, True)

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

    @classmethod
    def printIntro(self, introList):
        if len(introList) == 3: 
            length = len(introList[0])
            intro = ""
            if length > 60:
                intro = Output.break_up_long_message(introList[0], 60)

            daymsg = introList[1]
 
            length = len(introList[2])
            nextText = ""
            if length > 60:
                nextText = Output.break_up_long_message(introList[2], 60) 
      
            if sys.stdin.isatty():
                sys.stdout.write(u'\u001b[38;5;$69m')
                for elem in intro:
                    time.sleep(0.04)
                    sys.stdout.write(elem)
                    sys.stdout.flush()
                sys.stdout.write("\n")
                sys.stdout.write(u'\u001b[38;5;$61m')
                sys.stdout.write("\n")
                sys.stdout.write("\n")
                for elem in daymsg:
                    time.sleep(0.04)
                    sys.stdout.write(elem)
                    sys.stdout.flush()
                sys.stdout.write("\n")
                for elem in nextText:
                    time.sleep(0.04)
                    sys.stdout.write(elem)
                    sys.stdout.flush() 
                sys.stdout.write(u"\u001b[0m")
                print("\n")
                sys.stdout.flush()
            else:
                print(intro)

    @classmethod
    def searchForGameOutput(self, message):
        dots = " . . . . "
        if sys.stdin.isatty():
            #sys.stdout.write(u'\u001b[38;5;$10m')
            for elem in message:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
                #sys.stdout.write(u'\u001b[38;5;$10m')
            for elem in dots:
                time.sleep(0.5)
                sys.stdout.write(elem)
                sys.stdout.flush()
        else:
            message = message + dots
            print(message)


    @classmethod
    def welcomeBackToGame(self, placeDescription):
        length = len(placeDescription)
        if length > 60:
            placeDescription = Output.break_up_long_message(placeDescription, 60, True)

        pl1 = "Saved game found!"
        pl2 = "Loading . "
        pl3 = ". . . "
        printClear = "                                                        "

        welcome = 'Welcome back user!'
        welcome2 = " A recap of where you are: "


        if sys.stdin.isatty():
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(printClear)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u'\u001b[38;5;252m')
            for elem in pl1:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(printClear)
            sys.stdout.write(u"\u001b[1000D")
            for elem in pl2:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            for elem in pl3:
                time.sleep(0.5)
                sys.stdout.write(elem)
                sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(printClear)
            sys.stdout.write(u"\u001b[1000D")
            # welcome message 
            sys.stdout.write(u'\u001b[38;5;$51m')
            for elem in welcome:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            time.sleep(1)
            for elem in welcome2:
                time.sleep(0.04)
                sys.stdout.write(elem)
                sys.stdout.flush()
            time.sleep(0.5)
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
            print(pl1 + pl2 + pl3)
            print(welcome)
            print(placeDescription)
