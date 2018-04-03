import tkinter as tk
from File_IO import File_IO
from Analyzer import Analyser

class MainGUI:

    def __btnEnter_click(self,event):
        print('Entered')
        referee = Analyser(self.rules.startingState,self.rules.acceptState,self.rules.RuleBook)

        if(referee.vocabCheck(self.txtUserInput.get())):
            self.lblStatus.config(text='Word is accepted')
        else:
            self.lblStatus.config(text='Word is not accepted!!')



    def __btnUpLoad_click(self,event):
        print('Uploaded')
        self.rules.openFile()
        self.rules.readFile()

        self.lbl1.config(text= self.rules.fileName)

    def __init__(self):

        self.rules = File_IO()

        self.MainGUI = tk.Tk()
        self.MainGUI.title('Finite Autonoma')
        self.MainGUI.geometry('400x300')
        self.MainGUI.minsize(400, 300)

        btnUpload = tk.Button(self.MainGUI, width=15, height=2, text='Upload File')
        btnUpload.place(x=10, y=20)
        btnUpload.bind('<ButtonRelease-1>', self.__btnUpLoad_click)

        self.lbl1 = tk.Label(self.MainGUI, height=2, text='No File Selected')
        self.lbl1.place(x=150, y=22)

        lbl2 = tk.Label(self.MainGUI, height=2, text='Enter Encryption:')
        lbl2.place(x=10, y=140)

        self.lblStatus = tk.Label(self.MainGUI, height=2, text='')
        self.lblStatus.place(x=120, y=120)

        self.txtUserInput = tk.Entry(self.MainGUI, width=30, )
        self.txtUserInput.place(x=120, y=150)

        btnEnter = tk.Button(self.MainGUI, width=20, height=2, text='Enter')
        btnEnter.place(x=120, y=210)
        btnEnter.bind('<ButtonRelease-1>', self.__btnEnter_click)

    def run(self):
        self.MainGUI.mainloop()


