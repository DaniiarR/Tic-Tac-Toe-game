from tkinter import *
import os


root = Tk()
def oneVone():
    #exec('xo2buttonbind')
    root.destroy()
    os.system('python xo2buttonbind.py')



def computer():
    #exec('tictactoe')
    root.destroy()
    os.system('python tictactoe.py')
    #tictactoe.GUI().mainloop()


label = Label(root, text="Hello! Select game mode:", height=2, font="arial 16")
label.pack()
button1 = Button(root, text="1V1", width=14, font="arial 12", command= oneVone)
button1.pack()
button2 = Button(root, text="Against computer", width=14, font="arial 12", command= computer)
button2.pack()
root.mainloop()
