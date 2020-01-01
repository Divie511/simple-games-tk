<<<<<<< HEAD:Number Puzzle v1.1.py
from tkinter import *
import random

counter, state, empty = 15, 1, None
# counter will count number of tiles which are at the right position
# state = 1: the game continues...
# state = 2: You win!
# empty will refer to the empty tile
class tile:
    
    def __init__(self,value):
        self.value = value
        self.row = self.rfinal = (self.value - 1) // 4
        self.col = self.cfinal = (self.value - 1) % 4
        if self.value == 16: # value 16 was initially given to get the row and column no. for grid
            global empty
            self.value = " "
            empty = self # empty will now refer to the empty tile
        self.frame = Frame(mainframe, width = 30, height = 30, borderwidth = 1, relief="groove")
        self.frame.grid(row = self.row, column = self.col)
        self.frame.pack_propagate(0) # to fix the frame size
        self.Tile = Label(self.frame, text = self.value, font = (None,15))
        self.frame.bind("<Button-1>",lambda x: move(self))
        self.Tile.bind("<Button-1>",lambda x: move(self))
        self.Tile.pack()
        
    def update(self, row, col): # this method will be called when the tile is being moved to an empty grid
        if (self.row == self.rfinal) and (self.col == self.cfinal): score(-1) # if initially the tile was at right position, it not anymore
        # score function changes the value of counter variable while checking if it has reached 15 or not
        self.row = row # assigning new position to tile
        self.col = col
        self.frame.grid(row = self.row, column = self.col)
        if (self.row == self.rfinal) and (self.col == self.cfinal): score(+1) # if the tile is now at the right position

def scramble():
    for i in range(500):
        t = random.choice(tileslist)
        move(t)
        if state == 2: win(False) # since accidental reversal of moves may take place in a totally random scramble leading to game win

def score(i): # as mentioned above
    global counter
    counter += i
    if counter == 15: win(True)

def win(c):
    global state
    if c:
        empty.Tile.config(text = 16)
        state = 2
        tileslist[0].Tile.config(text = "Y")
        tileslist[1].Tile.config(text = "O")
        tileslist[2].Tile.config(text = "U")
        tileslist[3].Tile.config(text = " ")
        tileslist[4].Tile.config(text = "W")
        tileslist[5].Tile.config(text = "I")
        tileslist[6].Tile.config(text = "N")
        tileslist[7].Tile.config(text = "!")
    else: # undoing false win due to accidental reversal of moves
        empty.Tile.config(text = " ")
        state = 1
        for i in tileslist:
            i.Tile.config(text = i.value)

def select(r,c):
    for i in tileslist:
        if i.row == r and i.col == c: return i

def swap(x): # adjescent tiles swap places with empty grid
    r,c = x.row, x.col
    x.update(empty.row, empty.col)
    empty.update(r,c)

def move(x): # to move multiple tiles at once
    global state
    if state == 2: return # you can't move after game completion, right?
    if x.row == empty.row:
        if x.col < empty.col:
            while x.col < empty.col: # looping swap() function so each tile will shift one by one until the selected tile moves
                swap(select(empty.row, empty.col - 1))
            return
        while(x.col > empty.col):
            swap(select(empty.row, empty.col + 1))
        return
    elif x.col == empty.col:
        if x.row < empty.row:
            while x.row < empty.row:
                swap(select(empty.row - 1, empty.col))
            return
        while(x.row > empty.row):
            swap(select(empty.row + 1, empty.col))
        return

window = Tk()
mainframe = Frame(window)
mainframe.pack()

tileslist = []
for i in range(1,17):
    tileslist.append(tile(i))

window.resizable(0,0)
scramble()

=======
from tkinter import *
import random

counter, state, empty = 15, 1, None
# counter will count number of tiles which are at the right position
# state = 1: the game continues...
# state = 2: You win!
# empty will refer to the empty tile
class tile:
    
    def __init__(self,value):
        self.value = value
        self.row = self.rfinal = (self.value - 1) // 4
        self.col = self.cfinal = (self.value - 1) % 4
        if self.value == 16: # value 16 was initially given to get the row and column no. for grid
            global empty
            self.value = " "
            empty = self # empty will now refer to the empty tile
        self.frame = Frame(mainframe, width = 30, height = 30, borderwidth = 1, relief="groove")
        self.frame.grid(row = self.row, column = self.col)
        self.frame.pack_propagate(0) # to fix the frame size
        self.Tile = Label(self.frame, text = self.value, font = (None,15))
        self.frame.bind("<Button-1>",lambda x: move(self))
        self.Tile.bind("<Button-1>",lambda x: move(self))
        self.Tile.pack()
        
    def update(self, row, col): # this method will be called when the tile is being moved to an empty grid
        if (self.row == self.rfinal) and (self.col == self.cfinal): score(-1) # if initially the tile was at right position, it not anymore
        # score function changes the value of counter variable while checking if it has reached 15 or not
        self.row = row # assigning new position to tile
        self.col = col
        self.frame.grid(row = self.row, column = self.col)
        if (self.row == self.rfinal) and (self.col == self.cfinal): score(+1) # if the tile is now at the right position

def scramble():
    for i in range(500):
        t = random.choice(tileslist)
        move(t)
        if state == 2: win(False) # since accidental reversal of moves may take place in a totally random scramble leading to game win

def score(i): # as mentioned above
    global counter
    counter += i
    if counter == 15: win(True)

def win(c):
    global state
    if c:
        empty.Tile.config(text = 16)
        state = 2
        tileslist[0].Tile.config(text = "Y")
        tileslist[1].Tile.config(text = "O")
        tileslist[2].Tile.config(text = "U")
        tileslist[3].Tile.config(text = " ")
        tileslist[4].Tile.config(text = "W")
        tileslist[5].Tile.config(text = "I")
        tileslist[6].Tile.config(text = "N")
        tileslist[7].Tile.config(text = "!")
    else: # undoing false win due to accidental reversal of moves
        empty.Tile.config(text = " ")
        state = 1
        for i in tileslist:
            i.Tile.config(text = i.value)

def select(r,c):
    for i in tileslist:
        if i.row == r and i.col == c: return i

def swap(x): # adjescent tiles swap places with empty grid
    r,c = x.row, x.col
    x.update(empty.row, empty.col)
    empty.update(r,c)

def move(x): # to move multiple tiles at once
    global state
    if state == 2: return # you can't move after game completion, right?
    if x.row == empty.row:
        if x.col < empty.col:
            while x.col < empty.col: # looping swap() function so each tile will shift one by one until the selected tile moves
                swap(select(empty.row, empty.col - 1))
            return
        while(x.col > empty.col):
            swap(select(empty.row, empty.col + 1))
        return
    elif x.col == empty.col:
        if x.row < empty.row:
            while x.row < empty.row:
                swap(select(empty.row - 1, empty.col))
            return
        while(x.row > empty.row):
            swap(select(empty.row + 1, empty.col))
        return

window = Tk()
mainframe = Frame(window)
mainframe.pack()

tileslist = []
for i in range(1,17):
    tileslist.append(tile(i))

window.resizable(0,0)
scramble()

>>>>>>> 8186fd56404e49bbf70a903580bf5688aa21d8f0:Number Puzzle v1.1.py
window.mainloop()