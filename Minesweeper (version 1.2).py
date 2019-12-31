from tkinter import *
from random import *

state, count = 1, 0

class box:
    
    def __init__(self,r,c,m):
        self.row = r
        self.col = c
        self.mine = m
        self.revealed = False
        self.display = " "
        self.marked = False
        if self.mine: self.display = "X"
        self.frame = Frame(mainframe, width = 30, height = 30, borderwidth = 1, relief="groove", bg = "light blue")
        self.frame.grid(row = self.row, column = self.col)
        self.frame.pack_propagate(0)
        self.Tile = Label(self.frame, text = " ", relief="flat", bg = "light blue", font = (None,15))
        self.Tile.pack()
        self.Tile.bind("<Button-1>",self.unlock)
        self.Tile.bind("<Button-3>",self.mark)
        self.frame.bind("<Button-1>",self.unlock)
        self.frame.bind("<Button-3>",self.mark)
        
    def unlock(self, event):
        global state
        if state == 2 or self.revealed: return
        global count
        self.revealed = True
        self.Tile.config(text = self.display, bg = "#fff")
        self.frame.config(bg = "#fff")
        self.Tile.bind("<Button-1>",DoNothing)
        self.frame.bind("<Button-1>",DoNothing)
        self.Tile.bind("<Button-3>",DoNothing)
        self.frame.bind("<Button-3>",DoNothing)
        if self.mine:
            if state == 1:
                Endgame()
            self.Tile.config(bg = "#ff0000")
            self.frame.config(bg = "#ff0000")
        elif self.display == " ": opennearby(self)
        if state == 1:
            count += 1
        if count == 85 and state != 2:
            messagebox.config(text = "You win! :D", fg = "green")
            state = 2
        
    def mark(self, event):
        if state == 2: return
        if not self.marked:
            self.Tile.config(fg = '#ff0000', text = "!")
            self.Tile.bind("<Button-1>",DoNothing)
            self.frame.bind("<Button-1>",DoNothing)
            self.marked = True
        else:
            self.Tile.config(fg = "#000", text = " ")
            self.Tile.bind("<Button-1>",self.unlock)
            self.frame.bind("<Button-1>",self.unlock)
            self.marked = False

def DoNothing(*args): return

def select(r,c):
    for i in boxlist:
        if i.row==r and i.col==c: return i

def Endgame():
    global state
    state = 1.5
    for i in boxlist:
        if i.mine: i.unlock("GameOver")
    state = 2
    messagebox.config(text = "Game Over :(", fg = "#ff0000")

def opennearby(b):
    for r in range(b.row-1,b.row+2):
        for c in range(b.col-1,b.col+2):
            for i in boxlist:
                if i.row == r and i.col == c:
                    if not i.revealed:
                        i.unlock(" ")

root = Tk()
root.title("Minesweeper by Divyam")
mainframe = Frame(root)
mainframe.pack()
mineslist = []
for i in range(15):
    while True:
        r = int(10*random())
        c = int (10*random())
        if [r,c] not in mineslist: break
    mineslist.append([r,c])
boxlist = []
for r in range(10):
    for c in range(10):
        if [r,c] in mineslist: m = True
        else: m = False
        boxlist.append(box(r,c,m))
for i in boxlist:
    if i.mine: continue
    nearby = 0
    for r in range(i.row-1,i.row+2):
        for c in range(i.col-1,i.col+2):
            if [r,c] in mineslist: nearby+=1
    if nearby>0: i.display = nearby
messagebox = Label(mainframe, text = "Made by Divyam")
messagebox.grid(row = 10, column = 0, columnspan = 10)
root.resizable(0,0)
root.mainloop()