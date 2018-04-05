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
        # Class variable will hold the starting state value of the Finite Autonama
        self.startingState = 0
        # Class variable will hold the accepting state value of the Finite Autanama
        self.acceptState = 0
        # Class variable will hold the two dimentional list what will hold the rules of the Finite Autanama
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

    # Method Name:
    # Purpose:
    # Parameter: self, integer, list
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def __createRuleBook(self, lstLines):

        # Pattern used to find any numbers(or consecutive numbers) in a string
        paramState = r'[\d*]+'
        # PATTERN USED TO FIND ANY NUMBER(OR CONSECUTIVE NUMBERS) IN A STRING FOLLOWING A PARENTHESIS
        param1 = r'(?<=\()\s*\d*'
        # PATTEN USED TO FIND ANY ALPHABETIC(OR CONSECUTIVE ALPHABETS) IN A STRING FOLLOWING A COMMA
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

            #
            if re.search(param2, lstLines[i]).group() == 'a':

                self.RuleBook[0][int(re.search(param1, lstLines[i]).group()) - 1] = int(
                    re.search(param3, lstLines[i]).group())

            elif re.search(param2, lstLines[i]).group() == 'b':

                self.RuleBook[1][int(re.search(param1, lstLines[i]).group()) - 1] = int(
                    re.search(param3, lstLines[i]).group().strip())

        self.startingState = int(re.search(paramState, lstLines[0]).group())
        self.acceptState = int(re.search(paramState, lstLines[1]).group())

    # Method Name:
    # Purpose:
    # Parameter: self, integer, list
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def readFile(self):

        try:

            file = open('' + self.file + '', 'r')

            lineString = []

            for line in file:
                lineString.append(line)

            self.__createRuleBook(lineString)

        except:
            print('eh')

            self.fileName = 'No File Selected'
        else:

            file.close()

