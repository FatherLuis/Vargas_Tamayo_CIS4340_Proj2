import tkinter as tk
from File_IO import File_IO
from Analyzer import Analyser


# Class name: MainGUI
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Creates the GUI for the program to run
# Date: 2/2/2018
# List of changes with dates: none
# Special Notes: none

class MainGUI:

    # Method Name: __btnEnter_click()
    # Purpose: This method is an event handler for a button
    # Parameter: self, event
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def __btnEnter_click(self, event):

        # CREATES AN OBJECT OF CLASS ANALYSER
        referee = Analyser(self.rules.startingState, self.rules.acceptState, self.rules.RuleBook)

        # CHECKS IF THE USER INPUT ABIDE BY THE RULES SET UPON BY THE FILE
        # A LABEL WILL SAY IF THE USER INPUT IS ACCEPTED OR NOT
        if referee.vocabCheck(self.txtUserInput.get()):
            self.lblStatus.config(text='Word is accepted')
        else:
            self.lblStatus.config(text='Word is not accepted!!')

    # Method Name: __btnUpLoad_click()
    # Purpose: This method is an event handler for a button
    # Parameter: self, event
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def __btnUpLoad_click(self, event):

        # USES A CLASS METHOD OT OPEN A TEXT FILE
        self.rules.openFile()
        # USES A CLASS METHOD TO READ A TEXT FILE
        self.rules.readFile()

        # GUI LABEL1 WILL CONTAIN THE NAME OF THE FILE (IF ANY)
        self.lbl1.config(text=self.rules.fileName)

    # Method Name:__INIT__
    # Purpose: Class constructor
    # Parameter: self
    # Method used: __btnEnter(), __btnUpLoad()
    # Return Value: none
    # Date:  April 2, 2019
    def __init__(self):

        # class variable will hold the class object File_IO()
        self.rules = File_IO()

        # CLASS VARIABLE WILL HOLD THE REFERENCE TO THE GUI WINDOW
        self.MainGUI = tk.Tk()
        # WINDOW TEXT WILL CONTAIN A TEXT
        self.MainGUI.title('Finite Autonoma')
        # THE INITIAL SIZE OF THE GUI
        self.MainGUI.geometry('400x300')
        # THE MINIMUM SIZE OF THE GUI
        self.MainGUI.minsize(400, 300)
        # CREATES AN OBJECT BUTTON USED ON THE GUI
        btnUpload = tk.Button(self.MainGUI, width=15, height=2, text='Upload File')
        # PLACES THE BUTTON IN THE FOLLOWING COORDINATES ON THE GUI
        btnUpload.place(x=10, y=20)
        # BINDS AN EVENT METHOD TO THE BUTTON
        btnUpload.bind('<ButtonRelease-1>', self.__btnUpLoad_click)
        # CREATES AN OBJECT LABEL
        self.lbl1 = tk.Label(self.MainGUI, height=2, text='No File Selected')
        # PLACES THE LABEL IN THE FOLLOWING COORDINATES ON THE GUI
        self.lbl1.place(x=150, y=22)
        # CREATES AN OBJECT LABEL
        lbl2 = tk.Label(self.MainGUI, height=2, text='Enter Encryption:')
        # PLACES THE LABEL IN THE FOLLOWING COORDINATE ON THE GUI
        lbl2.place(x=10, y=140)
        # CREATES AN OBJECT LABEL
        self.lblStatus = tk.Label(self.MainGUI, height=2, text='')
        # PLACES THE LABEL IN THE FOLLOWING COORDINATE ON THE GUI
        self.lblStatus.place(x=120, y=120)
        # CREATES AN OBJECT TEXTBOX
        self.txtUserInput = tk.Entry(self.MainGUI, width=30, )
        # PLACES THE TEXTBOOK IN THE FOLLOWING COORDINATE ON THi GUI
        self.txtUserInput.place(x=120, y=150)
        # CREATES AN OBJECT BUTTON USED ON THE GUI
        btnEnter = tk.Button(self.MainGUI, width=20, height=2, text='Enter')
        # PLACES THE BUTTON IN THE FOLLOWING COORDINATE ON THE GUI
        btnEnter.place(x=120, y=210)
        # BINFS AN EVENT METHOD TO THE BUTTON
        btnEnter.bind('<ButtonRelease-1>', self.__btnEnter_click)

    # Method Name: Run()
    # Purpose: this will allow the the GUI to run (start)
    # Parameter: self
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def run(self):
        # This is the method used for the gui to be seen on screen
        self.MainGUI.mainloop()
