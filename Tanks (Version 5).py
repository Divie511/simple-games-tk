"""---------------CREATED BY DIVYAM JOSHI AND K. ADITYA---------------"""
"""------------------------CURRENT VERSION : 5------------------------"""
"""----------------------UPDATED 31 DECEMBER 2019---------------------"""

# you can download and make contributions to the game from Divyam's GitHub repository https://github.com/iamgroot9/iamgroot

version = '5'

from tkinter import *
from random import *
import time, importlib

try:
    import playerdata
except:
    print("ERROR: playerdata.py not found!")
    quit()
if playerdata.version < 1.1:
    print("Please update playerdata.py")
    quit()

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
    elif passcheck: LoadGame(u1,u2)
    else: login_message.config(text='Password(s) entered are incorrect!')

def DoNothing(*args): return # a useless function that would be the command of a disabled button or key press

def LoadGame(u1,u2):
    global p1,p2,hp1,hp2,a1,a2,a3,a4,messagebox,hb1,hb2,canvas2x,warriorA,warriorB,w1,w2,canvas73,game_window,l1,l2,maincanvas
    w1 = Warrior(playerdata.userlist.get(u1))
    w2 = Warrior(playerdata.userlist.get(u2))
    introFrame.destroy() # introFrame is where you recieve the introduction message. Now that the game has begun, we delete it.

    mainCanvas = Canvas(game_window,height=250,width=400, bg='#000') # This is where all the graphical stuff will be stored
    mainCanvas.pack()

    canvas73=Canvas(mainCanvas,height=250,width=400,bg="#000") # Tanks, stars and game title is displayed here
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
    
    frame2a = Frame(game_window, bg = '#000') # this frame will store health labels
    frame2a.pack()
    l1 = Label(frame2a, bg = '#222', width = 28, fg = '#fff', text=f'Level: {w1.level}')
    l2 = Label(frame2a, bg = '#222', width = 28, fg = '#fff', text=f'Level: {w2.level}')
    l1.pack(side=LEFT)
    l2.pack(side=RIGHT)

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
    global warriorA,warriorB,dmg,hit,p1,p2,hp1,hp2,a1,a2,a3,a4,messagebox,canvas2x,hb1,hb2,HT,canvas73,l1,l2
    if GameState == 1: # ATTACK mode
        warriorA, warriorB = warriorB, warriorA
        if warriorA == w1:
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
        a1.config(bg = '#000', command = atk1, cursor = 'hand2') # Enabling attack buttons
        a2.config(bg = '#000', command = atk2, cursor = 'hand2')
        a3.config(bg = '#000', command = atk3, cursor = 'hand2')
        game_window.bind('replenish',heal) # Enabling cheat codes
        game_window.bind('annihilate',destroy)
        game_window.bind('eagleeye',focus)
        messagebox.config(text = f'It\'s {warriorA}\'s turn to attack.')

    else: # INACTIVE mode
        a1.config(bg = 'grey', command = ChangeGameState, cursor = 'arrow') # disabling attack buttons
        a2.config(bg = 'grey', command = ChangeGameState, cursor = 'arrow') # ChangeGameState will switch the game back to attack mode
        a3.config(bg = 'grey', command = ChangeGameState, cursor = 'arrow')
        canvas2x.delete(hb1) # delting original health bars
        canvas2x.delete(hb2)
        hb1=canvas2x.create_rectangle(0,0,w1.health*1.5,7,fill = w1.colour) # creating new health bars with updated health
        hb2=canvas2x.create_rectangle(400-w2.health*1.5,0,400,7,fill = w2.colour)
        game_window.bind('replenish',DoNothing) # disabling cheat codes
        game_window.bind('annihilate',DoNothing)
        game_window.bind('eagleeye',DoNothing)

    if GameState == 0: # TANSITION mode ie inactive, yet not game over
        game_window.bind('<Key>', ChangeGameState) # Press any key to continue...
        game_window.bind('<Return>',ChangeGameState)
        # ChangeGameState (in this case) sets the opponent to attack mode
        if HT=='Heal': commentline = '20 health was gained.'
        elif HT=='Focus': commentline = f'{warriorA} attains special powers.'
        elif hit == 0: commentline = 'Attack missed.' # I hope this part is understood.
        elif dmg == 0: commentline = f'Attack Blocked by {warriorB}!'
        else: commentline = f'{warriorB} takes {dmg} damage.'
        if dmg>=30: commentline = f'{HT} caused a massive {dmg} damage to {warriorB}'
        messagebox.config(text = f'{warriorA} uses {HT}.\n'+commentline)

        if HT == 'Heal': # in case of cheat code 'replenish'
            if warriorA == w1: # health label of Player 1 displays heal
                hp1.config(fg = '#10ff00', text = '+20')
            else: # health label of Player 2 displays heal
                hp2.config(fg = '#10ff00', text = '+20')
        elif HT == 'Focus': # in case of cheat code 'focus'
            if warriorA == w1: # health label of Player 1 displays special message
                hp1.config(fg = '#ffc400', text = '++')
            else: # health label of Player 2 displays special message
                hp2.config(fg = '#ffc400', text = '++')
        else: # in other cases (when attacked)
            beam()
            if warriorA == w1: # health bar of Player 2 displays damage taken
                hp2.config(fg = '#bcff00', text = f'-{dmg}')
            else: # health bar of Player 1 displays damage taken
                hp1.config(fg = '#bcff00', text = f'-{dmg}')            

    else:
        game_window.bind('<Key>', DoNothing) # disabling press any key to continue
        game_window.bind('<Return>',DoNothing)
        hp1.config(fg = w1.colour, text = w1.health) # don't display damage taken/heal etc now
        hp2.config(fg = w2.colour, text = w2.health)
        del_beam()

    if GameState == 100: # If the one of the players dies
        a1.config(command = DoNothing) # disabling attacks, GameState is not be be changed now
        a2.config(command = DoNothing)
        a3.config(command = DoNothing)
        ccc = '' if not warriorA.cheat else '\n(Cheat codes used)' # cheating will be mentioned in the final report
        messagebox.config(text = f'{warriorA} wins!' + ccc)
        canvas73.destroy()
        if not warriorA.cheat: # cheating means your player stats won't be updated
            x = 3 if warriorB.cheat else 1 # if the opponent was cheating but you still won, you deserve bonus XP!
            playerdatafile = open('playerdata.py', mode='a', encoding='utf-8') # updating playerdata
            playerdatafile.write(f'\n{warriorA}.xp+={x}')
            playerdatafile.close()

    dmg, hit, HT = 0, -1, 'nil' # resetting the values so that the it's not the same in the next turn

def ChangeGameState(*args):
    global GameState
    if warriorB.health == 0 and GameState == 0: GameState = 100 # Opponent just died? That's game over!
    elif GameState == 1: GameState = 0 # This switches to TANSITION state after Player has used his attack or cheat
    elif GameState == 0: GameState = 1 # Switches back to ATTACK mode
    SetGame() # Applying changes in GameState

'''----------------WARRIOR CLASS-------------------'''
class Warrior:
    
    def __init__(self,player):
        self.name = player.name
        self.health = self.maxHealth = player.maxHealth
        self.maxAtk = player.maxAtk
        self.maxBlock = player.maxBlock
        self.cheat = False
        self.accuracy = player.accuracy
        self.level = player.level

    def __str__(self): # This magic method makes the object return its name when called in as a string
        return self.name # i.e. You just have to write down the 'object' instead of 'object.name' to add it's name to strings

    @property # this means self.colour is a property just like self.health and self.name and not a method self.colour()
    def colour(self): # it is created as a method property because it is dependent on health and is to be reassigned whenever health changes
        if self.health < 35: self.blow()
        if self.health > 70: return '#10ff00'
        elif self.health > 60: return '#55ff00'
        elif self.health > 50: return '#77ff00'
        elif self.health > 40: return '#bbff00'
        elif self.health > 30: return '#ffdd00'
        elif self.health > 20: return '#ff8000'
        else: return '#ff0000'
        
    def blow(self): pass

    def tank(self):
        if w1==self:
            self.base=canvas73.create_rectangle(0,150,75,225,fill="#008000",outline="#008000")
            self.top=canvas73.create_rectangle(30,100,50,150,fill="#008000",outline="#008000")
            self.turret=canvas73.create_rectangle(50,125,75,135,fill="#008000",outline="#008000")
            for i in range(0,150):
                canvas73.create_line(75,75+i,120-i,225,fill="#008000")
        else:
            self.base=canvas73.create_rectangle(325,150,400,225,fill="#ff0000",outline="#ff0000")
            self.top=canvas73.create_rectangle(355,100,375,150,fill="#ff0000",outline="#ff0000")
            self.turret=canvas73.create_rectangle(320,125,355,135,fill="#ff0000",outline="#ff0000")
            for i in range(0,150):
                canvas73.create_line(280+i,225,325,75+i,fill="#ff0000")

def accurate(x): # trying probability to see if attack works or not
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
def focus(*args): # eagleeye
    global HT
    HT = 'Focus'
    warriorA.accuracy = 10 # 100% accuracy, never miss an attack!
    warriorA.cheat = True
    ChangeGameState()

def GetDamage(): # final result of damage is calculated here
    global hit, warriorA, warriorB, dmg
    block = warriorB.maxBlock*uniform(0.3,0.6)
    dmg = int(hit - block)
    if dmg<=0: dmg=0
    warriorB.health -= dmg # reducing health by the amount of damage taken
    if warriorB.health<=0: warriorB.health=0
    ChangeGameState() # switching to TRANSITION mode

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
    # STAR WARS
    for i in range(40):
        canvas73.create_text(400*random(),220*random(),fill="#fff",text="*")
    w1.tank()
    w2.tank()
    
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
def winScreen(): # incomplete function! need someone to create the ending 'CONGRATULATIONS' screen
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