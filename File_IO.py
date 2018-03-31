import os
from tkinter import filedialog
import re


class File_IO:

    def __init__(self):
        self.file = filedialog.askopenfilename()

        self.fileName = os.path.basename(self.file)

        self.startingState = 0
        self.acceptState = 0

        self.RuleBook = [[], []]

    def readFile(self):

        paramState = r'[\d*]+'
        param1 = r'(?<=\()\s*\d*'
        param2 = r'(?<=\,)\s*\w*'
        param3 = r'(?<=\=)\s*\d*'

        try:

            file = open('' + self.file + '', 'r')

            lineString = []

            for line in file:
                lineString.append(line)

            print(lineString)

            numLines = (len(lineString) - 3) / 2.0
            numLines = int(numLines)

            #############################################################################
            for i in range(numLines):
                self.RuleBook[0].append(0)
                self.RuleBook[1].append(0)
            #############################################################################

            print(self.RuleBook)

            for i in range(3, len(lineString)):

                if re.search(param2, lineString[i]).group() == 'a':

                    self.RuleBook[0][int(re.search(param1, lineString[i]).group()) - 1] = int(
                        re.search(param3, lineString[i]).group())

                else:

                    self.RuleBook[1][int(re.search(param1, lineString[i]).group()) - 1] = int(
                        re.search(param3, lineString[i]).group().strip())

            print(self.RuleBook)

            self.startingState = int(re.search(paramState, lineString[0]).group())
            self.acceptState = int(re.search(paramState, lineString[1]).group())










        except:
            print('eh')

            self.fileName = 'No File Selected'
        else:

            file.close()
