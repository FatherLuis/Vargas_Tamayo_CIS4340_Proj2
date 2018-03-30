import tkinter as tk
from tkinter import filedialog

class File_IO:

    def __init__(self):
        self.fileName = filedialog.askopenfilename()

    def readFile(self):

        try:

            file = open('' + self.fileName + '', 'r')

            for line in file:
                print(line)

        finally:

            file.close()



