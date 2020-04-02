"----------------------------MADE BY DIVYAM JOSHI----------------------------"
"------------------------------------v0.1------------------------------------"
"----------------------------CREATED 2 APRIL 2020----------------------------"

version = '0.1'

try:
    from tkinter import *
except:
    from Tkinter import *

turn = "White"
gamestate = 1
moves = [] # list of possible moves

class rook:
    
    def __init__(self,tile,team):
        self.type = "R"
        self.tile = tile
        self.state = 0
        self.team = team
        tile.update(self)
        
    def select(self):
        r = self.tile.row
        c = self.tile.column
        for i,j in [[-1,0],[0,1],[0,-1],[1,0]]:
            x,y = r+i,c+j
            while (0 <= x <= 7) and (0 <= y <= 7):
                if (select(x,y).piece == None) or (select(x,y).piece.team != self.team): moves.append([x,y])
                if (select(x,y).piece != None): break
                x+=i
                y+=j

class knight:
    
    def __init__(self,tile,team):
        self.type = "K"
        self.tile = tile
        self.team = team
        tile.update(self)
    
    def select(self):
        r = self.tile.row
        c = self.tile.column
        for i,j in [[-2,1],[-2,-1],[2,-1],[2,1],[-1,2],[-1,-2],[1,2],[1,-2]]:
            x,y = r+i,c+j
            if (0 <= x <= 7) and (0 <= y <= 7):
                if (select(x,y).piece == None) or (select(x,y).piece.team != self.team): moves.append([x,y])

class bishop:
    
    def __init__(self,tile,team):
        self.type = "B"
        self.tile = tile
        self.team = team
        tile.update(self)
    
    def select(self):
        r = self.tile.row
        c = self.tile.column
        for i,j in [[-1,-1],[-1,1],[1,-1],[1,1]]:
            x,y = r+i,c+j
            while (0 <= x <= 7) and (0 <= y <= 7):
                if (select(x,y).piece == None) or (select(x,y).piece.team != self.team): moves.append([x,y])
                if (select(x,y).piece != None): break
                x+=i
                y+=j
        
class queen:
    
    def __init__(self,tile,team):
        self.type = "Q"
        self.tile = tile
        self.team = team
        tile.update(self)
    
    def select(self):
        r = self.tile.row
        c = self.tile.column
        for i,j in [[-1,0],[0,1],[0,-1],[1,0],[-1,-1],[-1,1],[1,-1],[1,1]]:
            x,y = r+i,c+j
            while (0 <= x <= 7) and (0 <= y <= 7):
                if (select(x,y).piece == None) or (select(x,y).piece.team != self.team): moves.append([x,y])
                if (select(x,y).piece != None): break
                x+=i
                y+=j

class king:
    
    def __init__(self,tile,team):
        self.type = "^^^"
        self.tile = tile
        self.state = 0
        self.team = team
        tile.update(self)
    
    def select(self):
        r = self.tile.row
        c = self.tile.column
        if (self.state == 0):
            pass # castling
        for i in range(r-1,r+2):
            if not 0 <= i <= 7: continue
            for j in range(c-1,c+2):
                if ([i,j] == [r,c]) or (not 0 <= c <= 7): continue
                if (select(i,j).piece == None) or (select(i,j).piece.team != self.team): moves.append([i,j])

class pawn:
    
    def __init__(self,tile,team):
        self.type = "o"
        self.tile = tile
        self.state = 0
        self.team = team
        tile.update(self)
    
    def select(self):
        r = self.tile.row
        c = self.tile.column
        i = -1 if self.team == "White" else 1
        if r != 0 and r != 7:
            if select(r+i,c).piece == None:
                moves.append([r+i,c])
                if (select(r+2*i,c).piece == None) and (self.state == 0): moves.append([r+2*i,c])
            if (c!=7) and (select(r+i,c+1).piece != None) and (select(r+i,c+1).piece.team != self.team): moves.append([r+i,c+1])
            if (c!=0) and (select(r+i,c-1).piece != None) and (select(r+i,c-1).piece.team != self.team): moves.append([r+i,c-1])
            
class Tile:
    
    def __init__(self,r,c):
        self.row = r
        self.column = c
        self.colour = "#59402a" if (r+c)%2 else "#c8a676"
        self.piece = None
        self.frame = Frame(mainframe, width = 50, height = 50, bg = self.colour, borderwidth = 2, relief="flat")
        self.frame.grid(row = self.row, column = self.column)
        self.frame.pack_propagate(0)
        self.display = Label(self.frame, bg = self.colour ,text=" ", font=('showcard gothic',20))
        self.display.pack()
        self.display.bind("<Button-1>",lambda x: clicked(self))
        self.frame.bind("<Button-1>",lambda x: clicked(self))
        
    def update(self,new):
        prev = self.piece
        self.piece = new
        if new != None:
            if (prev != None) and (prev.type) == "^^^":
                global gamestate, box
                box.config(text = f"{new.team} Team Won")
                gamestate = 2
            self.display.config(text = new.type, fg = new.team)
            self.piece.tile = self
            if ( (self.row == 0) or (self.row == 7) ) and (new.type == "o"): queen(self, new.team)
        else: self.display.config(text=" ")

def select(r,c):
    return tiles_list[8*r + c]
def win(x):
    msgbox = Tk()
    framex = Frame(msgbox)
    framex.pack()
    Label(framex,text = f"{x.team} team wins!".upper()).pack
    msgbox.mainloop()
def clicked(t):
    if gamestate == 2: return
    global moves, turn, dx
    temp = moves
    dx.display.config(bg=dx.colour)
    if t.piece == None or t.piece.team != turn:
        if [t.row,t.column] in moves:
            turn = "White" if turn=="Black" else "Black"
            box.config(text = f"{turn}\'s turn")
            t.update(dx.piece)
            dx.update(None)
            #if gamestate == 2: win(t.piece)
            if (t.piece.type == "o") and (t.piece.state == 0): t.piece.state = 1
        moves = []
    else:
        moves= []
        t.display.config(bg="#d7be69")
        t.piece.select()
    if len(temp) > 0:
        for i in temp:
            select(i[0],i[1]).display.config( bg = select(i[0],i[1]).colour )
    if len(moves) > 0:
        for i in moves:
            _ = select(i[0],i[1])
            if _.piece != None: _.display.config(bg = "#ff0000")
            else: _.display.config(bg = "#00b7eb")
    dx = t

chessboard=Tk()
chessboard.title("Two-Player Chess by Divyam")
mainframe=Frame(chessboard,width=400,height=500,bg="#000")
mainframe.pack_propagate(0)
mainframe.pack()
tiles_list=[]
for i in range(0,8):
    for j in range(0,8):
        tiles_list.append(Tile(i,j))
rook(select(7,0),"White")
rook(select(7,7),"White")
rook(select(0,0),"Black")
rook(select(0,7),"Black")
knight(select(0,6),"Black")
knight(select(0,1),"Black")
knight(select(7,1),"White")
knight(select(7,6),"White")
bishop(select(0,2),"Black")
bishop(select(0,5),"Black")
bishop(select(7,2),"White")
bishop(select(7,5),"White")
queen(select(7,3),"White")
king(select(7,4),"White")
queen(select(0,3),"Black")
king(select(0,4),"Black")
for i in range(8):
    pawn(select(1,i),"Black")
    pawn(select(6,i),"White")
    
frame2 = Frame(mainframe, bg = "#000", height = 50, width = 400)
frame2.grid(row = 8, column = 1, columnspan = 8)
box = Label(frame2, text = f"{turn}\'s turn", bg = "#000", fg = "#00b7eb")
box.pack(side = TOP)
Label(frame2, text = "Made by Divyam Joshi", bg = "#000", fg = "#00b7eb").pack(side = BOTTOM)

chessboard.resizable(0,0)

dx = select(4,4) # random declaration, (4,4) is not important

chessboard.mainloop()
