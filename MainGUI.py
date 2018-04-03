import tkinter as tk
from File_IO import File_IO
from Analyzer import Analyser

class MainGUI:

    def __btnEnter_click(self,event):
        print('Entered')

    def __btnUpLoad_click(self,event):
        print('Uploaded')

    def __init__(self):
        self.MainGUI = tk.Tk()
        self.MainGUI.title('Finite Autonoma')
        self.MainGUI.geometry('400x300')
        self.MainGUI.minsize(400, 300)

        btnUpload = tk.Button(self.MainGUI, width=15, height=2, text='Upload File')
        btnUpload.place(x=10, y=20)
        btnUpload.bind('<ButtonRelease-1>', self.__btnUpLoad_click)

        lbl1 = tk.Label(self.MainGUI, height=2, text='No File Selected')
        lbl1.place(x=150, y=22)

        lbl2 = tk.Label(self.MainGUI, height=2, text='Enter Encryption:')
        lbl2.place(x=10, y=140)

        txtUserInput = tk.Entry(self.MainGUI, width=30, )
        txtUserInput.place(x=120, y=150)

        btnEnter = tk.Button(self.MainGUI, width=20, height=2, text='Enter')
        btnEnter.place(x=120, y=210)
        btnEnter.bind('<ButtonRelease-1>', self.__btnEnter_click)

    def run(self):
        self.MainGUI.mainloop()


