from tkinter import *
from random import *

points, win = 0, 0

def score(pts):
    global points
    points += pts
    scoreboard.config(text = points)

tile_colors = {
    " ": "#cdc0b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59663",
    32: "#f67d5f",
    64: "#f65d3b",
    128: "#fad177",
    256: "#f7d067",
    512: "#fccb59",
    1024: "#edc540",
    2048: "#f9c62d",
    4096: "#f36775",
    8192: "#f14b61",
    16384: "#eb423f",
    32768: "#74b5db"
    }

class Cell:
    
    def __init__(self,r,c):
        self.row = r
        self.column = c
        self.value = " "
        self.frame = Frame(cells_frame, width = 99, height = 99, bg = self.color, borderwidth = 2, relief="groove")
        self.frame.grid(row = self.row, column = self.column)
        self.frame.pack_propagate(0) # to prevent frame resizing
        self.tile = Label(self.frame, bg = self.color, text = self.value)
        self.tile.pack()

    def update(self, v):
        temp = self.value
        self.value = v
        fontheight = 10* (7 - len(str(self.value)) )
        self.frame.config(bg = self.color)
        self.tile.config(text = self.value, font = ("Helvetica", fontheight), bg = self.color)
        if self.value != " ":
            if self.value > 6: self.tile.config(fg = "#fff")
            else: self.tile.config(fg = "#000")
            if temp != " ": score(self.value)
            if win == 0 and self.value == 2048: config_header(1)
            elif win == 1 and self.value == 4096: config_header(2)
            elif win == 2 and self.value == 8192: config_header(3)

    @property
    def color(self):
        if self.value in tile_colors: return tile_colors[self.value]
        else: return "#ff0000"

def select(r,c):
    for i in cellslist:
        if i.row == r and i.column == c: return i

def spawn():
    global last
    r = randint(0,3)
    c = randint(0,3)
    CELL = select(r,c)
    if (CELL.value == " "):
        v = 2 if random() < 0.9 else 4
        CELL.update(v)
    else: spawn()
    
def config_header(alpha):
    global win
    win = alpha
    if win == 0:
        header.config(bg = "#f9c62d")
        title.config(bg = "#f9c62d")
        something.config(text = "Join the numbers to\nmake the 2048 tile!\n\n", bg = "#f9c62d")
        somethingframe.config(bg = "#f9c62d")
        Divyam.config(bg = "#f9c62d")
        scores.config(bg = "#f9c62d")
        scoreboard.config(bg = "#f9c62d")
        titlelabel.config(text = 2048, bg = "#f9c62d")
        scorelabel.config(bg = "#f9c62d")
        scoreboardframe.config(bg = "#f9c62d")
    elif win == 1:
        something.config(bg = "#f36775", text = "Too easy, right?\nLet's see if you\ncould make 4096!\n\n")
        header.config(bg = "#f36775")
        titlelabel.config(text = 4096, bg = "#f36775")
        header.config(bg = "#f36775")
        title.config(bg = "#f36775")
        somethingframe.config(bg = "#f36775")
        scores.config(bg = "#f36775")
        scoreboard.config(bg = "#f36775")
        Divyam.config(bg = "#f36775")
        scorelabel.config(bg = "#f36775")
        scoreboardframe.config(bg = "#f36775")
    elif win == 2:
        something.config(bg = "#f14b61", text = "Excellent!\n8192 must be a\ngood challenge\nto you.\n")
        header.config(bg = "#f14b61")
        titlelabel.config(text = 8192, bg = "#f14b61")
        header.config(bg = "#f14b61")
        title.config(bg = "#f14b61")
        somethingframe.config(bg = "#f14b61")
        scores.config(bg = "#f14b61")
        scoreboard.config(bg = "#f14b61")
        Divyam.config(bg = "#f14b61")
        scorelabel.config(bg = "#f14b61")
        scoreboardframe.config(bg = "#f14b61")
    elif win == 3:
        something.config(bg = "#74b5db", text = "Hats Off!\nWe have found\nThe Champion!\n\n")
        header.config(bg = "#74b5db")
        titlelabel.config(text = "BRAVO!", bg = "#74b5db", font = ("Helvetica", 35))
        header.config(bg = "#74b5db")
        title.config(bg = "#74b5db")
        somethingframe.config(bg = "#74b5db")
        scores.config(bg = "#74b5db")
        scoreboard.config(bg = "#74b5db")
        Divyam.config(bg = "#74b5db")
        scorelabel.config(bg = "#74b5db")
        scoreboardframe.config(bg = "#74b5db")

def move_y(event):
    e = event.keysym
    change = False
    x = 1 if e == 'Down' else -1
    xs = 0 if e == 'Down' else 3
    xe = 3 if e == 'Down' else 0
    for c in range(4):
        r=xe-x
        fixed_tile = 0
        while 0 <= r <=3:
            if r==xe: r=xs+x
            t1, t2 = select(r,c), select(r+x,c)
            if t1.value != " ":
                if t2.value == " ":
                    t2.update(t1.value)
                    t1.update(" ")
                    r += x
                    change = True
                    continue
                elif t1.value == t2.value and fixed_tile != t2:
                    t2.update(2*t2.value)
                    t1.update(" ")
                    fixed_tile = t2
                    change = True
            r -= x
    if change: spawn()

def move_x(event):
    e = event.keysym
    change = False
    x = 1 if e == 'Right' else -1
    xs = 0 if e == 'Right' else 3
    xe = 3 if e == 'Right' else 0
    for r in range(4):
        c=xe-x
        fixed_tile = 0
        while 0 <= c <=3:
            if c==xe: c=xs+x
            t1, t2 = select(r,c), select(r,c+x)
            if t1.value != " ":
                if t2.value == " ":
                    t2.update(t1.value)
                    t1.update(" ")
                    c += x
                    change = True
                    continue
                elif t1.value == t2.value and fixed_tile != t2:
                    t2.update(2*t2.value)
                    t1.update(" ")
                    fixed_tile = t2
                    change = True
            c -= x
    if change: spawn()

window = Tk()
window.geometry("400x500")
window.resizable(0,0)
window.title("2048 by Divyam")

header = Frame(window, width = 400, height = 100)
header.pack()
header.pack_propagate(0)
title = Frame(header, width = 200, height = 100)
title.pack(side=LEFT)
title.pack_propagate(0)
titlelabel = Label(title, text = 2048, font = ("Helvetica", 50), bg = "#f9c62d", fg = "#fff")
titlelabel.pack(side = TOP)
Divyam = Label(title, text = "Made by Divyam Joshi", font = ("Helvetica", 10), fg = "#fff")
Divyam.pack(side=BOTTOM)

scores = Frame(header, width = 50, height = 100)
scores.pack(side = RIGHT)
somethingframe = Frame(header, width = 150, height = 100)
somethingframe.pack()
somethingframe.pack_propagate(0)
something = Label(somethingframe, fg = "#fff")
something.pack(side = BOTTOM)
scorelabel = Label(scores,text = " SCORE ", fg = "#fff")
scorelabel.grid(row = 0, column = 1)
scoreboardframe = Frame(scores, height = 20, width = 48)
scoreboardframe.grid(row = 1, column = 1)
scoreboardframe.pack_propagate(0)
scoreboard = Label(scoreboardframe,text = points, fg = "#fff")
scoreboard.pack()

cells_frame = Frame(window, width = 400, height = 400, highlightbackground = "#fff")
cells_frame.pack_propagate(0)
cells_frame.pack()
cellslist = []
for i in range(4):
    for j in range(4):
        cellslist.append(Cell(i,j))

config_header(0)

spawn()

window.bind('<Right>',move_x)
window.bind('<Left>',move_x)
window.bind('<Up>',move_y)
window.bind('<Down>',move_y)

window.mainloop()
