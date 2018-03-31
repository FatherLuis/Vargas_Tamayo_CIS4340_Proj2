import tkinter as tk
from File_IO import File_IO
from Analyzer import Analyser

MainGUI= tk.Tk()
#MainGUI.configure(background='black')
MainGUI.title('Finite Autonoma')
MainGUI.geometry('400x300')
MainGUI.minsize(400,300)


###################################################
def btnEnter_click(event):
    print('Enter')

def btnUpLoad_click(event):
    print('Upload')

    f = File_IO()
    f.readFile()
    lbl1.config(text=f.fileName)

    A = Analyser(f.startingState, f.acceptState, f.RuleBook)
    print(A.vocabCheck('bb'))


###################################################

btnUpload = tk.Button(MainGUI, width=15, height=2, text='Upload File')
btnUpload.place(x=10, y=20)
btnUpload.bind('<ButtonRelease-1>', btnUpLoad_click)

lbl1 = tk.Label(MainGUI, height=2, text='No File Selected')
lbl1.place(x=150, y=22)

lbl2 = tk.Label(MainGUI, height=2, text='Enter Encryption:')
lbl2.place(x=10, y= 140)

txtUserInput = tk.Entry(MainGUI,width=30,)
txtUserInput.place(x=120, y=150)

btnEnter = tk.Button(MainGUI, width=20, height=2, text='Enter')
btnEnter.place(x=120, y=210)
btnEnter.bind('<ButtonRelease-1>', btnEnter_click)


###############################################################################




##############################################################################
MainGUI.mainloop()


