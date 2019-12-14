"""---------------CREATED BY DIVYAM JOSHI AND K. ADITYA---------------"""
"""-----------------------CURRENT VERSION : 4.7-----------------------"""
"""----------------------UPDATED 14 DECEMBER 2019---------------------"""

version = '4.7'

from tkinter import *
from random import *
import time, importlib, playerdata
# from playerdata import * This can not be done since playerdata must be imported as module for it to be reloaded
# importlib is required to reload modules

# some important definitions... window starts in the end

# GLOBAL VARIABLES:
GameState, hit, HT, dmg = 1, -1, 'nil', 0
# GameState has 3 values based on which the colours and messages etc. changes would take place
# Purpose of each state is defined in the SetGame function as follows:
###-----# 1: Active/attack mode
###-----# 0: Transition/pause mode after a player uses their attack
###-----# 100: Game Over
# hit is a result of attack and leads to damage
# dmg a.k.a DAMAGE is (hit - block)
# HT carries the attack name to be displayed

def Login(*args):
    global login_message # in case player enters incorrect password, this would be configred to display the message
    p1,p2 = pass1.get(),pass2.get()
    passcheck = True
    users = ['','']

    for u in range(2): # Checking usename and password
        get = user1.get() if u==0 else user2.get()
        password = p1 if u==0 else p2
        for i in range(len(get)): # to prevent entry of bad data
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
    elif passcheck: LoadGame(u1,u2)
    else: login_message.config(text='Password(s) entered are incorrect!')

def DoNothing(*args): return # a useless function that would be the command of a disabled button

def LoadGame(u1,u2):
    global p1,p2,hp1,hp2,a1,a2,a3,a4,messagebox,hb1,hb2,canvas2x,warriorA,warriorB,w1,w2,canvas73,game_window
    w1 = Warrior(playerdata.userlist.get(u1))
    w2 = Warrior(playerdata.userlist.get(u2))
    introFrame.destroy() # it's obvious, isn't it?

    mainCanvas = Canvas(game_window,height=250,width=400, bg='#000') # This is where all the graphical stuff will be stored
    mainCanvas.pack()

    canvas73=Canvas(mainCanvas,height=250,width=400,bg="#000") # Let's draw!
    canvas73.pack()
    frame=Frame(game_window)
    frame.pack()

    LoadObjects()
    LoadTitle()
    
    frame1 = Frame(game_window, bg="#000") # warrior name labels in here
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

    canvas2x = Canvas(game_window, bg="#000", width = 400, height = 7) # health bars
    canvas2x.pack()
    hb1=canvas2x.create_rectangle(0,0,w1.health*1.5,7,fill = w1.colour)
    hb2=canvas2x.create_rectangle(400-w2.health*1.5,0,400,7,fill = w2.colour)

    frame3 = Frame(game_window, bg = '#000') # this is where the messages are added
    frame3.pack()
    messagebox = Label(frame3, bg = '#000', fg = '#fff', width = 57, height = 3)
    messagebox.pack()

    frame4 = Frame(game_window, bg = '#000') # and attacks of course
    frame4.pack()
    a1 = Button(frame4, text = 'Stupefy', width = 18, height = 2, fg = '#fff', bg = '#000')
    a2 = Button(frame4, text = 'Confringo', width = 18, height = 2, fg = '#fff', bg = '#000')
    a3 = Button(frame4, text = 'Sectumsempra', width = 18, height = 2, fg = '#fff', bg = '#000')
    a1.pack(side=LEFT)
    a3.pack(side = RIGHT)
    a2.pack()

    warriorA, warriorB = w2, w1
    beam() # this will be deleted due to current GameState

    game_window.resizable(0,0)
    
    SetGame() # now let's define the states

def SetGame(): # this function will make display changes acc to GameState
    global warriorA,warriorB,dmg,hit,p1,p2,hp1,hp2,a1,a2,a3,a4,messagebox,canvas2x,hb1,hb2,HT,canvas73
    if GameState == 1: # attack mode
        warriorA, warriorB = warriorB, warriorA
        if warriorA == w1:
            p2.config(bg = '#222', fg = '#fff')
            p1.config(bg = '#000', fg = '#10ff00')
            hp2.config(bg = '#222')
            hp1.config(bg = '#000')
        else:
            p1.config(bg = '#222', fg = '#fff')
            p2.config(bg = '#000', fg = '#10ff00')
            hp1.config(bg = '#222')
            hp2.config(bg = '#000')
        a1.config(bg = '#000', command = atk1, cursor = 'hand2') # The attacks are all functional in these states
        a2.config(bg = '#000', command = atk2, cursor = 'hand2')
        a3.config(bg = '#000', command = atk3, cursor = 'hand2')
        game_window.bind('replenish',heal)
        game_window.bind('annihilate',destroy)
        game_window.bind('eagleeye',focus)
        # game_window.bind('avadakedavra',kill) # rare instant kill
        messagebox.config(text = f'It\'s {warriorA}\'s turn to attack.') # The game isn't paused, it's player's chance to make a move!

    else: # other GameStates don't allow using attack buttons and cheats -- and that's the PAUSE mode
        a1.config(bg = 'grey', command = ChangeGameState, cursor = 'arrow')
        a2.config(bg = 'grey', command = ChangeGameState, cursor = 'arrow')
        a3.config(bg = 'grey', command = ChangeGameState, cursor = 'arrow')
        canvas2x.delete(hb1) # delting original health bars
        canvas2x.delete(hb2)
        hb1=canvas2x.create_rectangle(0,0,w1.health*1.5,7,fill = w1.colour) # creating new health bars with new health
        hb2=canvas2x.create_rectangle(400-w2.health*1.5,0,400,7,fill = w2.colour)
        game_window.bind('replenish',DoNothing)
        game_window.bind('annihilate',DoNothing)
        game_window.bind('eagleeye',DoNothing)
        # game_window.bind('avadakedavra',DoNothing)

    if GameState == 0: # game is paused right? and it isn't over yet
        game_window.bind('<Key>', ChangeGameState)
        game_window.bind('<Return>',ChangeGameState)
        # ChangeGameState (in this case) sets the opponent to attack mode
        if HT=='Heal': commentline = '20 health was gained.'
        elif HT=='Focus': commentline = f'{warriorA} attains special powers.'
        elif hit == 0: commentline = 'Attack missed.' # I hope this part is understood.
        elif dmg == 0: commentline = f'Attack Blocked by {warriorB}!'
        else: commentline = f'{warriorB} takes {dmg} damage.'
        if dmg>=30: commentline = f'{HT} caused a massive {dmg} damage to {warriorB}'
        messagebox.config(text = f'{warriorA} uses {HT}.\n'+commentline)

        if HT == 'Heal':
            if warriorA == w1: # health label of Player 1 displays heal
                hp1.config(fg = '#10ff00', text = '+20')
            else: # health label of Player 2 displays heal
                hp2.config(fg = '#10ff00', text = '+20')
        elif HT == 'Focus':
            if warriorA == w1: # health label of Player 1 displays heal
                hp1.config(fg = '#ffc400', text = '++')
            else: # health label of Player 2 displays heal
                hp2.config(fg = '#ffc400', text = '++')
        else: # after the player has used their attack
            beam()
            if warriorA == w1: # health bar of Player 2 displays damage taken
                hp2.config(fg = '#bcff00', text = f'-{dmg}')
            else: # health bar of Player 1 displays damage taken
                hp1.config(fg = '#bcff00', text = f'-{dmg}')            

    else: # This must be easily understood
        game_window.bind('<Key>', DoNothing)
        hp1.config(fg = w1.colour, text = w1.health)
        hp2.config(fg = w2.colour, text = w2.health)
        game_window.bind('<Return>',DoNothing)
        del_beam()

    if GameState == 100: # If the one of the players dies
        a1.config(command = DoNothing)
        a2.config(command = DoNothing)
        a3.config(command = DoNothing)
        ccc = '' if not warriorA.cheat else '\n(Cheat codes used)'
        messagebox.config(text = f'{warriorA} wins!' + ccc)
        canvas73.destroy()
        if not warriorA.cheat:
            playerdatafile = open('playerdata.py', mode='a', encoding='utf-8')
            playerdatafile.write(f'\n{warriorA}.xp+=1')
            playerdatafile.close()

    dmg, hit, HT = 0, -1, 'nil' # resetting the values so that the it's not the same in the next turn

def ChangeGameState(*args):
    global GameState
    if warriorB.health == 0 and GameState == 0: GameState = 100 # Opponent just died? That's game over!
    elif GameState == 1: GameState = 0 # This switches to PAUSE state after Player has used his attack
    elif GameState == 0: GameState = 1 # Switches back to attack mode
    SetGame() # Who will apply the changes in GameState, huh?

'''----------------WARRIOR CLASS-------------------'''
class Warrior:
    
    def __init__(self,player):
        self.name = player.name
        self.health = self.maxHealth = player.maxHealth
        self.maxAtk = player.maxAtk
        self.maxBlock = player.maxBlock
        self.cheat = False
        self.accuracy = player.accuracy

    def __str__(self): # This magic method makes the object return its name when called in as a string
        return self.name # i.e. You just have to write down the 'object' instead of 'object.name' to add it's name to strings

    @property # this means self.colour is a property just like self.health and self.name and not self.colour()
    def colour(self): # it is created as a method because it is dependent on health and is to be reassigned whenever health changes
        if self.health > 70: return '#10ff00'
        elif self.health > 60: return '#55ff00'
        elif self.health > 50: return '#77ff00'
        elif self.health > 40: return '#bbff00'
        elif self.health > 30: return '#ffdd00'
        elif self.health > 20: return '#ff8000'
        else: return '#ff0000'

def accurate(x):
    if warriorA.accuracy == 10: return True
    rtrn = warriorA.accuracy*random()
    return True if rtrn > 1-x else False

def atk1(*args): # These functions will be executed when the attack buttons are clicked (in GameState 0 or 1)
    global hit, HT
    HT = 'Stupefy'
    hit = warriorA.maxAtk
    GetDamage() # Causes damage, defined just below these attacks
def atk2(*args):
    global hit, HT
    HT = 'Confringo'
    if accurate(0.7): hit = warriorA.maxAtk * 1.25
    else: hit = 0 # Simply means Attack missed
    GetDamage()
def atk3(*args):
    global hit, HT
    HT = 'Sectumsempra'
    if accurate(0.35): hit = warriorA.maxAtk * 2
    else: hit = 0
    GetDamage()
def heal(*args): # replenish
    global HT
    warriorA.health+=20
    HT = 'Heal'
    warriorA.cheat = True # keeping a track of cheat code usage
    ChangeGameState()
def destroy(*args): # annihilate
    global HT, hit
    warriorA.cheat = True
    HT = 'Super Power'
    hit = warriorA.maxAtk * 1.5
    GetDamage()
'''
def kill(*args): # avadakedavra --> instant kill
    global HT, hit
    warriorA.cheat = True
    HT = 'Killing Curse'
    if accurate(0.01): hit = warriorA.maxAtk * 100
    else: hit = 0
    GetDamage()
'''
def focus(*args): # eagleeye
    global HT
    HT = 'Focus'
    warriorA.accuracy = 10
    warriorA.cheat = True
    ChangeGameState()

def GetDamage():
    global hit, warriorA, warriorB, dmg
    block = warriorB.maxBlock*uniform(0.3,0.6)
    dmg = int(hit - block)
    if dmg<=0: dmg=0
    warriorB.health -= dmg # health is all what matters
    if warriorB.health<=0: warriorB.health=0
    # You have used your attack, right? That's the only case if this function was called. So now let's switch to PAUSE mode
    ChangeGameState()

'-------------Loading Objects---------------'
def del_beam(): # to delete tank beam
    canvas73.delete(my_rect1)
    canvas73.delete(my_rect2)
    canvas73.delete(my_rect3)
def beam(): # to create tank beam
    global my_rect1,my_rect2,my_rect3
    if warriorA == w1:
        my_rect1=canvas73.create_rectangle(75,125,300,135,fill="#ff0000")
        my_rect2=canvas73.create_rectangle(75,125,250,135,fill="#ffa500")
        my_rect3=canvas73.create_rectangle(75,125,200,135,fill="#ffff00")
    else:
        my_rect1=canvas73.create_rectangle(105,125,320,135,fill="#ff0000")
        my_rect2=canvas73.create_rectangle(155,125,320,135,fill="#ffa500")
        my_rect3=canvas73.create_rectangle(205,125,320,135,fill="#ffff00")

def LoadObjects():
    global t1_base,t1_top,t1_turret,t2_base,t2_top,t2_turret
    # STAR WARS
    for i in range(40):
        canvas73.create_text(400*random(),220*random(),fill="#fff",text="*")
    # tank1
    t1_base=canvas73.create_rectangle(0,150,75,225,fill="#008000",outline="#008000")
    t1_top=canvas73.create_rectangle(30,100,50,150,fill="#008000",outline="#008000")
    t1_turret=canvas73.create_rectangle(50,125,75,135,fill="#008000",outline="#008000")
    #front1
    for i in range(0,150):
        canvas73.create_line(75,75+i,120-i,225,fill="#008000")
    #tank2
    t2_base=canvas73.create_rectangle(325,150,400,225,fill="#ff0000",outline="#ff0000")
    t2_top=canvas73.create_rectangle(355,100,375,150,fill="#ff0000",outline="#ff0000")
    t2_turret=canvas73.create_rectangle(320,125,355,135,fill="#ff0000",outline="#ff0000")
    #front2
    for i in range(0,150):
        canvas73.create_line(280+i,225,325,75+i,fill="#ff0000")
    #ground
    ground=canvas73.create_rectangle(0,225,400,250,fill="#a52a2a")
def LoadTitle():
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
    pass

introMessage = """This game was made by Divyam Joshi and K. Aditya. Copyright (c) 2019. All rights reserved.\n
Instructions:
You have to chose from among 3 attacks as follows:
STUPEFY: Causes a maximum 20 damage, has 100% accuracy but can be blocked by the opponent
CONFRINGO: Capable of causing maximum 25 damage, accuracy is 70%.
SECTUMSEMPRA: Often deals massive damage, yet, if difficult to cast. Accuracy is 35%. Max damage: 40\n"""

def introScreen():
    global introFrame, introMessageBox, user1, user2, pass1, pass2, login_message
    introFrame = Frame(game_window, bg = '#000')
    introFrame.pack()
    introMessageBox = Label(introFrame, fg = "#10ff00", bg = '#000', text = introMessage) # 10ff00 is for green
    introMessageBox.pack()
    f1 = Frame(introFrame)
    f1.pack()
    fu1 = Frame(f1)
    fu1.pack(side=LEFT)
    u1 = Label(fu1, bg = '#000', fg = '#fff', text = 'Username: ')
    u1.pack(side=LEFT)
    user1 = Entry(fu1)
    user1.pack(side=RIGHT)
    fp1 = Frame(f1)
    fp1.pack(side=RIGHT)
    p1 = Label(fp1, bg = '#000', fg = '#fff', text = 'Password: ')
    p1.pack(side=LEFT)
    pass1 = Entry(fp1, show = '*')
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
    game_window.bind('<Return>',Login)
    ok = Button(f3, text = 'Login', bg = '#000', fg = '#10ff00', command = Login, cursor = 'hand2')
    ok.pack() # LoadGame function creates a new screen with the main game stuff
    fx2 = Canvas(introFrame,width=560, height = 15, bg = '#000',highlightbackground="#000")
    fx2.pack()
    fx2.create_text(545,7,fill="#ffff00",text=f"v{version}")

game_window = Tk()
game_window.title("TANKS")
introScreen()
game_window.mainloop()