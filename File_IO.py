import os
from tkinter import filedialog
import re


class File_IO:

    def __init__(self):
        self.fileName = ''

        self.startingState = 0
        self.acceptState = 0

        self.RuleBook = [[], []]


    def openFile(self):

        self.file = filedialog.askopenfilename()
        self.fileName = os.path.basename(self.file)


    def __createRuleBook(self, lstLines):

        paramState = r'[\d*]+'
        param1 = r'(?<=\()\s*\d*'
        param2 = r'(?<=\,)\s*\w*'
        param3 = r'(?<=\=)\s*\d*'

        numLines = int((len(lstLines) - 3) / 2.0)

        #############################################################################
        for i in range(numLines):
            self.RuleBook[0].append(0)
            self.RuleBook[1].append(0)
        #############################################################################

        for i in range(3, len(lstLines)):

            if re.search(param2, lstLines[i]).group() == 'a':

                self.RuleBook[0][int(re.search(param1, lstLines[i]).group()) - 1] = int(
                    re.search(param3, lstLines[i]).group())

            else:

                self.RuleBook[1][int(re.search(param1, lstLines[i]).group()) - 1] = int(
                    re.search(param3, lstLines[i]).group().strip())

        self.startingState = int(re.search(paramState, lstLines[0]).group())
        self.acceptState = int(re.search(paramState, lstLines[1]).group())

    def readFile(self):
        #
        # paramState = r'[\d*]+'
        # param1 = r'(?<=\()\s*\d*'
        # param2 = r'(?<=\,)\s*\w*'
        # param3 = r'(?<=\=)\s*\d*'

        try:

            file = open('' + self.file + '', 'r')

            lineString = []

            for line in file:
                lineString.append(line)

            self.__createRuleBook(lineString)



            # numLines = int((len(lineString) - 3) / 2.0)
            #
            # #############################################################################
            # for i in range(numLines):
            #     self.RuleBook[0].append(0)
            #     self.RuleBook[1].append(0)
            # #############################################################################
            #
            # for i in range(3, len(lineString)):
            #
            #     if re.search(param2, lineString[i]).group() == 'a':
            #
            #         self.RuleBook[0][int(re.search(param1, lineString[i]).group()) - 1] = int(
            #             re.search(param3, lineString[i]).group())
            #
            #     else:
            #
            #         self.RuleBook[1][int(re.search(param1, lineString[i]).group()) - 1] = int(
            #             re.search(param3, lineString[i]).group().strip())
            #
            # self.startingState = int(re.search(paramState, lineString[0]).group())
            # self.acceptState = int(re.search(paramState, lineString[1]).group())

        except:
            print('eh')

            self.fileName = 'No File Selected'
        else:

            file.close()

