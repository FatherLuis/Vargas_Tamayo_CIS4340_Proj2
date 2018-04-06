import os
from tkinter import filedialog
import re

# Class name: File_IO
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Has the functionality to read a text file and create a Rulebook
# Date: 2/2/2018
# List of changes with dates: none
# Special Notes: none


class File_IO:

    # Method Name: __init__
    # Purpose: Class Constructor
    # Parameter: self, integer, integer, list
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def __init__(self):
        # class variable will hold the string name of a file
        self.fileName = ''
        # Class variable will hold the starting state value of the Finite State Machine
        self.startingState = 0
        # Class variable will hold the accepting state value of the Finite Finite State Machine
        self.acceptState = 0
        # Class variable will hold the two dimentional list what will hold the rules of the Finite AutanamaFinite State Machine
        self.RuleBook = [[], []]

    # Method Name: openFile()
    # Purpose: Class Constructor
    # Parameter: self, integer, integer, list
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def openFile(self):

        # opens file dialog to get file path
        self.file = filedialog.askopenfilename()
        # get basic file names
        self.fileName = os.path.basename(self.file)

    # Method Name: __createRuleBook()
    # Purpose: Takes in a given list and creates the rules used for the finite Finite State Machine
    # Parameter: self, integer, list
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def __createRuleBook(self, lstLines):

        # Pattern used to find any numbers(or consecutive numbers) in a string
        paramState = r'[\d*]+'
        # PATTERN USED TO FIND ANY NUMBER(OR CONSECUTIVE NUMBERS) IN A STRING FOLLOWING A PARENTHESIS
        param1 = r'(?<=\()\s*\d*'
        # PATTERN USED TO FIND ANY ALPHABETIC(OR CONSECUTIVE ALPHABETS) IN A STRING FOLLOWING A COMMA
        param2 = r'(?<=\,)\s*\w*'
        # PATTERN USED TO FIND ANY NUMBER(OR CONSECUTIVE NUMBERS) IN A STRING FOLLOWING A EQUAL SIGN
        param3 = r'(?<=\=)\s*\d*'

        # GET THE NUMBER OF STAGES
        numLines = int((len(lstLines) - 3) / 2.0)

        #############################################################################
        # CREATE AND INITIALIZE THE LIST TO THE NUMBER OF STAGES
        for i in range(numLines):
            self.RuleBook[0].append(0)
            self.RuleBook[1].append(0)
        #############################################################################

        # ITERATES BY THE AMOUNT OF STAGES IN THE FILE
        for i in range(3, len(lstLines)):

            # CHECKS FOR THE PATTERN IN PARAM2 IS FOUND IN THE GIVEN ELEMENT IS EQUAL TO 'A'
            if re.search(param2, lstLines[i]).group() == 'a':
                # GETS THE INTEGER FOUND IN THE LIST WITH THE GIVEN PATTERN PARAM1 (USED AS THE INDEX) AND SET THE VALUE
                # EQUAL TO THE PATTERN IN PARAM3 FOUND IN THE LIST
                self.RuleBook[0][int(re.search(param1, lstLines[i]).group()) - 1] = \
                    int(re.search(param3, lstLines[i]).group())

            # CHECKS FOR THE PATTERN IN PARAM2 IS FOUND IN THE GIVEN ELEMENT IS EQUAL TO 'B'
            elif re.search(param2, lstLines[i]).group() == 'b':

                # GETS THE INTEGER FOUND IN THE LIST WITH THE GIVEN PATTERN PARAM1 (USED AS THE INDEX) AND SET THE VALUE
                # EQUAL TO THE PATTERN IN PARAM3 FOUND IN THE LIST
                self.RuleBook[1][int(re.search(param1, lstLines[i]).group()) - 1] = \
                    int(re.search(param3, lstLines[i]).group().strip())

        # GETS THE STARTING STATE FROM THE STRING USING THE PATTERN PARAMSTATE
        self.startingState = int(re.search(paramState, lstLines[0]).group())
        # GETS THE STARTING STATE FROM THE STRING USING THE PATTERN PARAMSTATE
        self.acceptState = int(re.search(paramState, lstLines[1]).group())

    # Method Name: readFile()
    # Purpose: Opens file and collects information
    # Parameter: self
    # Method used: createRuleBook()
    # Return Value: none
    # Date:  April 2, 2019
    def readFile(self):

        try:
            # Opens file from filepath # Read Only
            file = open('' + self.file + '', 'r')

            # CREATES A LIST STRING THAT WILL HOLD EACH LINE FROM THE TEXT FILE
            lineString = []

            # ITERATES THROUGH EACH LINE OF THE FILE AND APPENDS TO THE LIST
            for line in file:
                lineString.append(line)

            # SENDS LIST TO THE METHOD
            self.__createRuleBook(lineString)

        except:

            # IF ANY ERROR, FILE IS CLOSED AND USER WILL BE NOTIFIED THAT THE FILE WAS NOT USED
            self.fileName = 'No File Selected'
        else:
            # FILE IS CLOSED
            file.close()

