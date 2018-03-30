import tkinter as tk

MainGUI= tk.Tk()
#MainGUI.configure(background='black')
MainGUI.title('Finite Autonoma')
MainGUI.geometry('400x300')
MainGUI.minsize(400,300)

btnUpload = tk.Button(MainGUI, width=15, height=2, text='Upload File')
btnUpload.place(x=10, y=20)

lbl1 = tk.Label(MainGUI, height=2, text='No File Selected')
lbl1.place(x=150, y=22)

lbl2 = tk.Label(MainGUI, height=2, text='Enter Encryption:')
lbl2.place(x=10, y= 140)

txtUserInput = tk.Entry(MainGUI,width=30,)
txtUserInput.place(x=120, y=150)

btnEnter = tk.Button(MainGUI, width=20, height=2, text='Enter')
btnEnter.place(x=120, y=210)

MainGUI.mainloop()