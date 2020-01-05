"""---------------CREATED BY DIVYAM JOSHI AND K. ADITYA---------------"""
"""-----------------------CURRENT VERSION : 5.9-----------------------"""
"""-------------------------UPDATED 4 JAN 2019------------------------"""

# you can download and make contributions to the game from Divyam's GitHub repository https://github.com/iamgroot9/iamgroot

try:
    import playerdata
except:
    print("ERROR: playerdata.py not found!")
    quit()
if playerdata.version < 1.1:
    print("Please update playerdata.py")
    quit()

version = '5.9'

try:
    from tkinter import *
except:
    from Tkinter import *
from random import *
import importlib

# GLOBAL VARIABLES:
GameState, hit, HT, dmg = 1, -1, 'nil', 0
# GameState has 3 values based on which the colours and messages etc. changes would take place
# Purpose of each state is defined in the SetGame function as follows:
###-----# 1: Active/attack mode
###-----# 0: When the apponent takes damage
###-----# 10: During attack
###-----# 100: Game Over
# hit is a result of attack and leads to damage
# dmg a.k.a DAMAGE is (hit - block)
# HT carries the attack name to be displayed

def Login(*args):
    global login_message,u1,u2,w1,w2 # in case player enters incorrect password, this would be configred to display the message
    p1,p2 = pass1.get(),pass2.get() # pass1 and pass2 are entry boxes which recieve entered passwords
    passcheck = True
    users = ['',''] # this will store usernames

    for u in range(2): # Checking usename and password
        get = user1.get() if u==0 else user2.get() # user1 and user2 are entry boxes which recieve entered usernames
        password = p1 if u==0 else p2
        for i in range(len(get)): # correcting usernames to prevent entry of bad data
            if ( not get[i].isalnum() ): users[u]+='_' # bad data will be converted to _
            else: users[u]+=get[i]
        if len(get)==0: users[u]='_' # in case of empty username
    
        if users[u] in playerdata.userlist: # check passwords for registered users
            if playerdata.userlist.get(users[u]).password != password: passcheck = False
        else: # register new users
            playerdatafile = open('playerdata.py', mode='a', encoding = 'utf-8')
            playerdatafile.write(f'\n{users[u]}=Player("{users[u]}","{password}")\nuserlist["{users[u]}"]={users[u]}')
            playerdatafile.close()

    u1, u2 = users[0], users[1]
    importlib.reload(playerdata) # loads modified playerdata file with new users registered
    
    if u1==u2: login_message.config(text='Please enter different usernames.')
    elif passcheck: tank_colour(u1,u2)
    else: login_message.config(text='Password(s) entered are incorrect!')

def DoNothing(*args): return # a useless function that would be the command of a disabled button or key press

def on_enter(b,event,*args): # on mouse hover over attack buttons...
    global messagebox
    
    messagebox.config(fg = "yellow")
    if b=='a1':
        messagebox.configure(text="Max Damage:100%\n  Accuracy:100%")
        a1.config(fg='yellow')
    elif b=='a2':
        messagebox.configure(text="Max Damage:130%\n Accuracy:70%")
        a2.config(fg='yellow')
    else:
        messagebox.configure(text="Max Damage:200%\n Accuracy:35%")
        a3.config(fg='yellow')

def on_leave(event=None,*args):
    global messagebox
    messagebox.configure(text = f'It\'s {TankA}\'s turn to attack.', fg = "#fff")
    a1.config(fg='#fff')
    a2.config(fg='#fff')
    a3.config(fg='#fff')

def tank_colour(u1,u2):
    global frame,w1,w2
    w1 = Tank(playerdata.userlist.get(u1))
    w2 = Tank(playerdata.userlist.get(u2))
    introFrame.destroy() # introFrame is where you recieve the introduction message. Now that the game has begun, we delete it.
    frame=Frame(game_window,bg='#000')
    frame.pack()
    frame.pack_propagate(0)
    
    Label(frame,bg="#000",fg="#fff",text='Select you tank', font=(None,20)).grid(row=0,column=1,columnspan = 2)
    Label(frame,bg="#000",fg="#fff",text=f'{w1}').grid(row=1,column=1)
    Label(frame,bg="#000",fg="#fff",text=f'{w2}').grid(row=1,column=2)
    
    w1Canvas = Canvas(frame,bg='#000')
    w1Canvas.grid(row = 2, column = 1)
    
    blue1=Canvas(w1Canvas, bg='#000', width=150, highlightbackground = "#000")
    blue1.grid(row=1,column=1)
    green1=Canvas(w1Canvas, bg='#000', width=150, highlightbackground = "#000")
    green1.grid(row=1,column=2)
    red1=Canvas(w1Canvas, bg='#000', width=150, highlightbackground = "#000")
    red1.grid(row=2,column=1)
    orange1=Canvas(w1Canvas, bg='#000', width=150, highlightbackground = "#000")
    orange1.grid(row=2,column=2)
    
    w2Canvas = Canvas(frame,bg='#000')
    w2Canvas.grid(row = 2, column = 2)
    
    blue2=Canvas(w2Canvas, bg='#000', width=150, highlightbackground = "#000")
    blue2.grid(row=1,column=3)
    green2=Canvas(w2Canvas, bg='#000', width=150, highlightbackground = "#000")
    green2.grid(row=1,column=4)
    red2=Canvas(w2Canvas, bg='#000', width=150, highlightbackground = "#000")
    red2.grid(row=2,column=3)
    orange2=Canvas(w2Canvas, bg='#000', width=150, highlightbackground = "#000")
    orange2.grid(row=2,column=4)
    
    def setColour(canvas,tank,colour):
        tank.colour = colour
        if tank == w1:
            for i in [blue1,green1,red1,orange1]:
                if i == canvas: continue
                else: i.config(highlightbackground = "#000")
        else:
            for i in [blue2,green2,red2,orange2]:
                if i == canvas: continue
                else: i.config(highlightbackground = "#000")
        canvas.config(highlightbackground = 'yellow')
        
    w1.tank(blue1,"blue")
    w1.tank(red1,"red")
    w1.tank(green1,"green")
    w1.tank(orange1,"orange")
    w2.tank(blue2,"blue")
    w2.tank(red2,"red")
    w2.tank(green2,"green")
    w2.tank(orange2,"orange")
    
    blue1.bind("<Button-1>",lambda x: setColour(blue1,w1,'blue'))
    red1.bind("<Button-1>",lambda x: setColour(red1,w1,'red'))
    green1.bind("<Button-1>",lambda x: setColour(green1,w1,'green'))
    orange1.bind("<Button-1>",lambda x: setColour(orange1,w1,'orange'))
    blue2.bind("<Button-1>",lambda x: setColour(blue2,w2,'blue'))
    red2.bind("<Button-1>",lambda x: setColour(red2,w2,'red'))
    green2.bind("<Button-1>",lambda x: setColour(green2,w2,'green'))
    orange2.bind("<Button-1>",lambda x: setColour(orange2,w2,'orange'))
    
    Button(frame,text="OK",command = lambda: LoadGame(frame)).grid(row=3,column=1,columnspan=2)
    
def LoadGame(frame):
    global p1,p2,hp1,hp2,a1,a2,a3,a4,messagebox,hb1,hb2,canvas2x,TankA,TankB,w1,w2,canvas73,game_window,l1,l2
    frame.destroy()

    canvas73=Canvas(game_window,height=250,width=400,bg="#000") # Tanks, stars and game title is displayed here
    canvas73.pack()
    frame=Frame(game_window)
    frame.pack()

    LoadObjects()
    LoadTitle()

    frame1 = Frame(game_window, bg="#000") # Tank name labels in here
    frame1.pack(side = TOP)
    p1 = Label(frame1, text = w1, bg = '#222', fg = '#fff', width = 28)
    p1.pack(side=LEFT)
    p2 = Label(frame1, text = w2, bg = '#222', fg = '#fff', width = 28)
    p2.pack(side=RIGHT)

    frame2 = Frame(game_window, bg = '#000') # this frame will store health labels
    frame2.pack()
    hp1 = Label(frame2, bg = '#000', width = 28)
    hp2 = Label(frame2, bg = '#222', width = 28)
    hp1.pack(side=LEFT)
    hp2.pack(side=RIGHT)
    
    frame2a = Frame(game_window, bg = '#000') # this frame will store health labels
    frame2a.pack()
    l1 = Label(frame2a, bg = '#222', width = 28, fg = '#fff', text=f'Level: {w1.level}')
    l2 = Label(frame2a, bg = '#222', width = 28, fg = '#fff', text=f'Level: {w2.level}')
    l1.pack(side=LEFT)
    l2.pack(side=RIGHT)

    canvas2x = Canvas(game_window, bg="#000", width = 400, height = 7) # health bars
    canvas2x.pack()
    hb1=canvas2x.create_rectangle(0,0,w1.health*1.5,7,fill = w1.hcolour)
    hb2=canvas2x.create_rectangle(400-w2.health*1.5,0,400,7,fill = w2.hcolour)

    frame3 = Frame(game_window, bg = '#000') # this is where the messages are added
    frame3.pack()
    messagebox = Label(frame3, bg = '#000', fg = '#fff', width = 57, height = 3)
    messagebox.pack()
    
    TankA, TankB = w2, w1

    frame4 = Frame(game_window, bg = '#000') # and attacks of course
    frame4.pack()
    a1 = Button(frame4, text = TankA.a1, width = 18, height = 2, fg = '#fff', bg = '#000')
    a2 = Button(frame4, text = TankA.a2, width = 18, height = 2, fg = '#fff', bg = '#000')
    a3 = Button(frame4, text = TankA.a3, width = 18, height = 2, fg = '#fff', bg = '#000')
    a1.pack(side=LEFT)
    a3.pack(side = RIGHT)
    a2.pack()

    game_window.resizable(0,0)
    
    SetGame() # now let's define the states

def SetGame(): # this function will make display changes acc to GameState
    global TankA,TankB,dmg,hit,p1,p2,hp1,hp2,a1,a2,a3,a4,messagebox,canvas2x,hb1,hb2,HT,canvas73,l1,l2

    if GameState == 1: # ATTACK mode
        TankA, TankB = TankB, TankA
        hp1.config(fg = w1.hcolour, text = w1.health) # don't display damage taken/heal etc now
        hp2.config(fg = w2.hcolour, text = w2.health)
        if TankA == w1:
            p2.config(bg = '#222', fg = '#fff') # highlighting name and health labels according to active player
            p1.config(bg = '#000', fg = '#10ff00')
            hp2.config(bg = '#222')
            l2.config(bg = '#222')
            l1.config(bg = '#000')
            hp1.config(bg = '#000')
        else:
            p1.config(bg = '#222', fg = '#fff')
            p2.config(bg = '#000', fg = '#10ff00')
            hp1.config(bg = '#222')
            hp2.config(bg = '#000')
            l1.config(bg = '#222')
            l2.config(bg = '#000')
        a1.config(bg = '#000', command = atk1, cursor = 'hand2', text = TankA.a1) # Enabling attack buttons
        a2.config(bg = '#000', command = atk2, cursor = 'hand2', text = TankA.a2)
        a3.config(bg = '#000', command = atk3, cursor = 'hand2', text = TankA.a3)
        a1.bind("<Enter>",lambda event: on_enter('a1',event))
        a1.bind("<Leave>",lambda event: on_leave('a1',event))
        a2.bind("<Enter>",lambda event: on_enter('a2',event))
        a2.bind("<Leave>",lambda event: on_leave('a2',event))
        a3.bind("<Enter>",lambda event: on_enter('a3',event))
        a3.bind("<Leave>",lambda event: on_leave('a3',event))
        #game_window.bind('replenish',heal) # Enabling cheat codes
        #game_window.bind('annihilate',destroy)
        #game_window.bind('eagleeye',focus)
        messagebox.config(text = f'It\'s {TankA}\'s turn to attack.')

    elif GameState == 10:
        a1.config(bg = 'grey', fg = '#fff', command = DoNothing, cursor = 'arrow') # disabling attack buttons
        a2.config(bg = 'grey', fg = '#fff', command = DoNothing, cursor = 'arrow') # ChangeGameState will switch the game back to attack mode
        a3.config(bg = 'grey', fg = '#fff', command = DoNothing, cursor = 'arrow')
        a1.bind("<Enter>",DoNothing)
        a1.bind("<Leave>",DoNothing)
        a2.bind("<Enter>",DoNothing)
        a2.bind("<Leave>",DoNothing)
        a3.bind("<Enter>",DoNothing)
        a3.bind("<Leave>",DoNothing)
        messagebox.config(text = f'{TankA} uses {HT}.', fg = "#fff")
        if hit != -1: beam()

    elif GameState == 0:
        if hit == 0: commentline = 'Attack missed.' # I hope this part is understood.
        elif dmg == 0: commentline = f'Attack successfully blocked by {TankB}!'
        else: commentline = f'{TankB} takes {dmg} damage.'
        if dmg>=30: commentline = f'{HT} caused a massive {dmg} damage to {TankB}'
        messagebox.config(text = commentline, fg = "#fff")
        
        canvas2x.delete(hb1) # delting original health bars
        canvas2x.delete(hb2)
        hb1=canvas2x.create_rectangle(0,0,w1.health*1.5,7,fill = w1.hcolour) # creating new health bars with updated health
        hb2=canvas2x.create_rectangle(400-w2.health*1.5,0,400,7,fill = w2.hcolour)
    
        if TankA == w1: # health bar of Player 2 displays damage taken
            hp2.config(fg = '#bcff00', text = f'-{dmg}')
        else: # health bar of Player 1 displays damage taken
            hp1.config(fg = '#bcff00', text = f'-{dmg}')
        
            dmg, hit, HT = 0, -1, 'nil' # resetting the values so that the it's not the same in the next turn

    if GameState == 100: # If the one of the players dies
        ccc = '' if not TankA.cheat else '\n(Cheat codes used)' # cheating will be mentioned in the final report
        messagebox.config(text = f'{TankA} wins!' + ccc)
        canvas73.delete(TankB.top)
        canvas73.delete(TankB.turret)
        canvas73.delete(TankB.base)
        canvas73.delete(TankB.behind)
        canvas73.delete(TankB.front)
        hp1.config(fg = w1.hcolour, text = w1.health) # don't display damage taken/heal etc now
        hp2.config(fg = w2.hcolour, text = w2.health)
        winScreen()
        if not TankA.cheat: # cheating means your player stats won't be updated
            x = 3 if TankB.cheat else 1 # if the opponent was cheating but you still won, you deserve bonus XP!
            playerdatafile = open('playerdata.py', mode='a', encoding='utf-8') # updating playerdata
            playerdatafile.write(f'\n{TankA}.xp+={x}')
            playerdatafile.close()

def ChangeGameState(*args):
    global GameState
    if TankB.health == 0 and GameState == 0: GameState = 100 # Opponent just died? That's game over!
    elif GameState == 1: GameState = 10 # This calls the beam when an attack is clicked
    elif GameState == 10: GameState = 0 # This causes blast when beam hits the opponent tank
    elif GameState == 0: GameState = 1 # Switches back to ATTACK mode
    SetGame() # Applying changes in GameState

'''----------------TANK CLASS-------------------'''
class Tank:
    
    def __init__(self,player):
        try:
            self.name = player.name
            self.health = self.maxHealth = player.maxHealth
            self.maxAtk = player.maxAtk
            self.maxBlock = player.maxBlock
            self.cheat = False
            self.level = player.level
        except:
            print("ERROR: playerdata.py is corrupted!")
            quit()
        self.a1 = "Stupefy" if self.level < 5 else "Bombarda"
        self.a2 = "Confringo" if self.level < 10 else "Reducto"
        self.a3 = "Reducto" if self.level < 10 else "Sectumsempra"

    def __str__(self): # This magic method makes the object return its name when called in as a string
        return self.name # i.e. You just have to write down the 'object' instead of 'object.name' to add it's name to strings

    @property # this means self.colour is a property just like self.health and self.name and not a method self.colour()
    def hcolour(self): # it is created as a method property because it is dependent on health and is to be reassigned whenever health changes
        if self.health < 35: self.blow()
        if self.health > 70: return '#10ff00'
        elif self.health > 60: return '#55ff00'
        elif self.health > 50: return '#77ff00'
        elif self.health > 40: return '#bbff00'
        elif self.health > 30: return '#ffdd00'
        elif self.health > 20: return '#ff8000'
        else: return '#ff0000'
        
    def blow(self): pass

    def tank(self,master,colour):
        self.colour = colour
        if w1==self:
            self.base=master.create_rectangle(0,150,75,225,fill=self.colour,outline=self.colour)
            self.top=master.create_rectangle(30,100,50,150,fill=self.colour,outline=self.colour)
            self.turret=master.create_rectangle(50,125,75,135,fill=self.colour,outline=self.colour)
            self.front=master.create_polygon([75,150,75,225,100,225,75,150],fill=self.colour)
            self.behind=master.create_polygon([0,150,0,70,75,90,20,90,20,150,0,150],fill=self.colour)
    
        else:
            x = int(master['width'])
            self.base=master.create_rectangle(x-75,150,x,225,fill=self.colour,outline=self.colour)
            self.top=master.create_rectangle(x-50,100,x-30,150,fill=self.colour,outline=self.colour)
            self.turret=master.create_rectangle(x-75,125,x-50,135,fill=self.colour,outline=self.colour)
            self.front=master.create_polygon([x-75,150,x-75,225,x-100,225,x-75,150],fill=self.colour)
            self.behind=master.create_polygon([x,150,x,70,x-75,90,x-20,90,x-20,150,x,150],fill=self.colour)

    def move_tank(self):
        x = 1 if self == w1 else -1
        canvas73.move(self.base,x,0)
        canvas73.move(self.top,x,0)
        canvas73.move(self.turret,x,0)
        canvas73.move(self.behind,x,0)
        canvas73.move(self.front,x,0)
        canvas73.after(10,self.move_tank)
                
class beam:
    def __init__(self):
        if TankA == w1:
            self.laser = canvas73.create_rectangle(75,125,100,135, fill = "red")
            self.x = 5
        else:
            self.laser = canvas73.create_rectangle(295,125,320,135, fill = "red")
            self.x = -5
        self.a = 0
        self.move()
    def move(self):
        if self.a == 50:
            blast(self)
            ChangeGameState()
            return
        self.a += 1
        canvas73.move(self.laser, self.x, 0)
        canvas73.after(10, self.move)
        
class blast:
    def __init__(self,laser):
        self.x = 0
        x1,y1,x2,y2 = canvas73.coords(laser.laser)
        x, y = (x1+x2)/2, (y1+y2)/2
        self.a = canvas73.create_text(x,y, text = "*", fill="yellow",font=(None,20))
        self.b = canvas73.create_text(x,y, text = "*", fill="yellow",font=(None,20))
        self.c = canvas73.create_text(x,y, text = "*", fill="yellow",font=(None,20))
        self.d = canvas73.create_text(x,y, text = "*", fill="yellow",font=(None,20))
        self.e = canvas73.create_text(x,y, text = "*", fill="yellow",font=(None,20))
        self.f = canvas73.create_text(x,y, text = "*", fill="yellow",font=(None,20))
        self.g = canvas73.create_text(x,y, text = "*", fill="yellow",font=(None,20))
        self.h = canvas73.create_text(x,y, text = "*", fill="yellow",font=(None,20))
        canvas73.delete(laser.laser)
        self.move()
    def move(self):
        if self.x == 20:
            canvas73.delete(self.a)
            canvas73.delete(self.b)
            canvas73.delete(self.c)
            canvas73.delete(self.d)
            canvas73.delete(self.e)
            canvas73.delete(self.f)
            canvas73.delete(self.g)
            canvas73.delete(self.h)
            ChangeGameState()
            return
        canvas73.move(self.a, -1, -1)
        canvas73.move(self.b, 0, -1)
        canvas73.move(self.c, 1, -1)
        canvas73.move(self.d, -1, 0)
        canvas73.move(self.e, 1, 0)
        canvas73.move(self.f, -1, 1)
        canvas73.move(self.g, 0, 1)
        canvas73.move(self.h, 1, 1)
        self.x += 1
        canvas73.after(10, self.move)

def accurate(x): # trying probability to see if attack works or not
    rtrn = random()
    return True if rtrn > 1-x else False

def atk1(*args): # These functions will be executed when the attack buttons are clicked (in GameState 1)
    global hit, HT
    HT = TankA.a1
    c = 1 if TankA.level < 5 else 1.5
    if accurate(1 if TankA.level < 5 else 0.8): hit = TankA.maxAtk * c
    else: hit = 0
    GetDamage() # Causes damage, defined just below these attacks
def atk2(*args):
    global hit, HT
    HT = TankA.a2
    c = 1.3 if TankA.level < 10 else 2
    if accurate(0.7 if TankA.level < 10 else 0.6): hit = TankA.maxAtk * c
    else: hit = 0 # Simply means Attack missed
    GetDamage()
def atk3(*args):
    global hit, HT
    HT = TankA.a3
    c = 2 if TankA.level < 10 else 2.5
    if accurate(0.35 if TankA.level < 10 else 0.2): hit = TankA.maxAtk * c
    else: hit = 0
    GetDamage()

def GetDamage(): # final result of damage is calculated here
    global hit, TankA, TankB, dmg
    block = TankB.maxBlock*uniform(0.3,0.6)
    dmg = int(hit - block)
    if dmg<=0: dmg=0
    TankB.health -= dmg # reducing health by the amount of damage taken
    if TankB.health<=0: TankB.health=0
    ChangeGameState() # switching to TRANSITION mode

'-------------Loading Objects---------------'

def LoadObjects():
    # STAR WARS
    for i in range(40):
        canvas73.create_text(400*random(),220*random(),fill="#fff",text="*")
    w1.tank(canvas73,w1.colour)
    w2.tank(canvas73,w2.colour)
    
    #ground
    ground=canvas73.create_rectangle(0,225,400,250,fill="#a52a2a")
def LoadTitle(): # very hefty work... you can ignore this part as it requires no modifications
    T_top=canvas73.create_rectangle(80,20,130,40,outline="#ffff00")
    T_bot=canvas73.create_rectangle(100,40,110,80,outline="#ffff00")
    A_left1=canvas73.create_line(170,20,140,80,fill="#ffff00")
    A_left2=canvas73.create_line(170,40,160,80,fill="#ffff00")
    A_right1=canvas73.create_line(170,40,180,80,fill="#ffff00")
    A_right2=canvas73.create_line(170,20,200,80,fill="#ffff00")
    A_bot1=canvas73.create_line(140,80,160,80,fill="#ffff00")
    A_bot2=canvas73.create_line(180,80,200,80,fill="#ffff00")
    N_left1=canvas73.create_rectangle(210,20,220,80,outline="#ffff00")
    N_diag_left=canvas73.create_line(220,40,240,80,fill="#ffff00")
    N_diag_right=canvas73.create_line(220,20,240,75,fill="#ffff00")
    N_right2=canvas73.create_rectangle(240,20,250,80,outline="#ffff00")
    K_left=canvas73.create_rectangle(260,20,270,80,outline="#ffff00")
    K_mid=canvas73.create_rectangle(270,40,275,50,outline="#ffff00")
    K_bot_left=canvas73.create_line(270,50,277,80,fill="#ffff00")
    K_bot_right=canvas73.create_line(275,50,285,80,fill="#ffff00")
    K_bot_line=canvas73.create_line(277,80,285,80,fill="#ffff00")
    K_top_left=canvas73.create_line(270,40,277,20,fill="#ffff00")
    K_top_right=canvas73.create_line(275,40,285,20,fill="#ffff00")
    K_top_line=canvas73.create_line(275,20,285,20,fill="#ffff00")
    S_top=canvas73.create_rectangle(295,20,315,40,outline="#ffff00")
    S_left=canvas73.create_rectangle(295,40,300,50,outline="#ffff00")
    S_mid=canvas73.create_rectangle(295,50,315,55,outline="#ffff00")
    S_right=canvas73.create_rectangle(310,55,315,75,outline="#ffff00")
    S_bot=canvas73.create_rectangle(295,75,315,80,outline="#ffff00")
    
def winScreen():
    global canvas73
    canvas73.create_text(200,150,text=f"\n{TankA} wins!",font=('showcard gothic',30),fill="yellow")
    TankA.move_tank()

introMessage = """This game was made by Divyam Joshi and K. Aditya. Copyright (c) 2019. All rights reserved.\n\n"""

def introScreen():
    global introFrame, introMessageBox, user1, user2, pass1, pass2, login_message
    introFrame = Frame(game_window, bg = '#000')
    introFrame.pack()
    introMessageBox = Label(introFrame, fg = "#10ff00", bg = '#000', text = introMessage)
    introMessageBox.pack()
    f1 = Frame(introFrame)
    f1.pack()
    fu1 = Frame(f1)
    fu1.pack(side=LEFT)
    u1 = Label(fu1, bg = '#000', fg = '#fff', text = 'Username: ')
    u1.pack(side=LEFT)
    user1 = Entry(fu1) # this is where username is entered
    user1.pack(side=RIGHT)
    fp1 = Frame(f1)
    fp1.pack(side=RIGHT)
    p1 = Label(fp1, bg = '#000', fg = '#fff', text = 'Password: ')
    p1.pack(side=LEFT)
    pass1 = Entry(fp1, show = '*') # and this is where password is entered
    pass1.pack(side=RIGHT)
    fx1 = Frame(introFrame, height = 10, bg = '#000')
    fx1.pack()
    f2 = Frame(introFrame)
    f2.pack()
    fu2 = Frame(f2)
    fu2.pack(side=LEFT)
    u2 = Label(fu2, bg = '#000', fg = '#fff', text = 'Username: ')
    u2.pack(side=LEFT)
    user2 = Entry(fu2)
    user2.pack(side=RIGHT)
    fp2 = Frame(f2)
    fp2.pack(side=RIGHT)
    p2 = Label(fp2, bg = '#000', fg = '#fff', text = 'Password: ')
    p2.pack(side=LEFT)
    pass2 = Entry(fp2, show='*')
    pass2.pack(side=RIGHT)
    fx = Frame(introFrame, height = 10, bg = '#000')
    fx.pack()
    f3 = Frame(introFrame, bg = '#000')
    login_message = Label(f3, bg='#000', fg='#ff0000')
    login_message.pack()
    f3.pack()
    game_window.bind('<Return>',Login) # press enter to login
    ok = Button(f3, text = 'Login', bg = '#000', fg = '#10ff00', command = Login, cursor = 'hand2') # Login function
    ok.pack()
    fx2 = Canvas(introFrame,width=560, height = 15, bg = '#000',highlightbackground="#000")
    fx2.pack()
    fx2.create_text(545,7,fill="#ffff00",text=f"v{version}")

game_window = Tk()
game_window.title("TANKS")
introScreen()
game_window.mainloop()
