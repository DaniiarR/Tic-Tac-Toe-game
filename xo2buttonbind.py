from tkinter import *

turn = True
btns = None
root = None
Moves = 0


def clicked(y, x):
    """Sets the button to needed value when clicked"""
    global turn, btns, Moves
    char = ""
    if turn:
        char = "X"
        bgcolor = "black"
    else:
        char = "O"
        bgcolor = "white"

    btns[y][x].config(text=char, bg=bgcolor,
                      state=DISABLED)
    Moves += 1
    isWinner(char)
    turn = not turn
    

def buttonPressed(e, y, x):
    global turn, btns
    char=""
    if turn:
        char="X"
        bgcolor = "black"
    else:
        char = "O"
        bgcolor = "white"
    btns[y][x].config(text=char, bg=bgcolor,
                      state=DISABLED)
    isWinner(char)
    turn = not turn


def restart(root):
    """Restarts the game"""
    global turn, Moves
    turn = True
    Moves = 0
    root.destroy()
    main()

def draw(char):
    """Congratulation message pops up"""
    global root
    top = Toplevel()
    top.title("Congratulations!")
    top.minsize(300, 150)
    #top.geometry("200x150")
    topText = Label(top, text="Draw!", font=("Helvetica", 20), pady=20)
    topButton = Button(top, text="Restart", width=10, height=2, command=lambda: restart(root))
    topText.pack(fill=X)
    topButton.pack()

    
def topMessage(char):
    """Congratulation message pops up"""
    global root
    top = Toplevel()
    top.title("Congratulations!")
    top.minsize(300, 150)
    #top.geometry("200x150")
    topText = Label(top, text=f"{char} is the winner!", font=("Helvetica", 20), pady=20)
    topButton = Button(top, text="Restart", width=10, height=2, command=lambda: restart(root))
    topText.pack(fill=X)
    topButton.pack()


def isWinner(char):
    """Determines the winner"""
    global root, Moves
        # horizontal
    if (((btns[1][1].cget("text") == char) and (btns[1][2].cget("text") == char) and (btns[1][3].cget("text") == char)) or
        ((btns[2][1].cget("text") == char) and (btns[2][2].cget("text") == char) and (btns[2][3].cget("text") == char)) or
        ((btns[3][1].cget("text") == char) and (btns[3][2].cget("text") == char) and (btns[3][3].cget("text") == char)) or
        # vertical
        ((btns[1][1].cget("text") == char) and (btns[2][1].cget("text") == char) and (btns[3][1].cget("text") == char)) or
        ((btns[1][2].cget("text") == char) and (btns[2][2].cget("text") == char) and (btns[3][2].cget("text") == char)) or
        ((btns[1][3].cget("text") == char) and (btns[2][3].cget("text") == char) and (btns[3][3].cget("text") == char)) or
        # diagonal
        ((btns[1][1].cget("text") == char) and (btns[2][2].cget("text") == char) and (btns[3][3].cget("text") == char)) or
        ((btns[1][3].cget("text") == char) and (btns[2][2].cget("text") == char) and (btns[3][1].cget("text") == char))):
        for y in range(3):
            for x in range(3):
                 btns[x+1][y+1].config(state=DISABLED)
        topMessage(char)
    elif Moves == 9:
        draw(char)
        


def main():
    """Creates the main window and buttons"""
    global btns
    global root
    root = Tk()
    root.title("My Tic-Tac-Toe")
    root.resizable(False, False)
    btns = [None]
    restartbtn = Button(root, text="Restart",width=5, height=2, command=lambda: restart(root))
    for y in range(1, 4):
        row = [None]
        for x in range(1, 4):
            row.append(Button(root,
                              width=5,
                              height=3,
                              font="time 12 bold",
                              command=lambda x=x, y=y: clicked(y, x)))
            #root.bind(str((y-1)*3+x), lambda e, x=x, y=y: buttonPressed(e, y, x)) 
            row[x].grid(row=y, column=x)
        btns.append(row)
    restartbtn.grid(row=4, column=2)
    root.mainloop()
main()
