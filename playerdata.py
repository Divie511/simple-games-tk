import math
version = 1.1

class Player:
    
    def __init__(self, username, password):
        self.name = username
        self.password = password
        self.xp = 1

    @property
    def level(self):
        return 1 + int(math.log(self.xp,1.8))
    @property
    def accuracy(self):
        return 1 + self.level/10
    @property
    def maxHealth(self):
        return 99 + int((self.level)*(self.level+1)/2)
    @property
    def maxBlock(self):
        return 20 + int(self.level*1.2)
    @property
    def maxAtk(self):
        return 20 + int(self.level*1.2)

userlist = {}

Divyam=Player("Divyam","Ktx_2")
userlist["Divyam"]=Divyam
Batman=Player("Batman","iamrich")
userlist["Batman"]=Batman
Chirag=Player("Chirag","chiragroxx")
userlist["Chirag"]=Chirag
Spider_Man=Player("Spider_Man","EDITH")
userlist["Spider_Man"]=Spider_Man
Tony=Player("Tony","youwillneverguessmypassword")
userlist["Tony"]=Tony
pajjii=Player("pajjii","op")
userlist["pajjii"]=pajjii
Divyam.xp+=1
Parneet=Player("Parneet","techsingh12")
userlist["Parneet"]=Parneet
Divyam.xp+=1
Divyam.xp+=1
_=Player("_","")
userlist["_"]=_
_=Player("_","")
userlist["_"]=_
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Divyam.xp+=1
Batman.xp+=1
SPARTACUS=Player("SPARTACUS","Nothing")
userlist["SPARTACUS"]=SPARTACUS
SUPERMAN=Player("SUPERMAN","NOBODY")
userlist["SUPERMAN"]=SUPERMAN
jarvis=Player("jarvis","cr7")
userlist["jarvis"]=jarvis
Batman.xp+=1
_.xp+=1
Batman.xp+=1
_.xp+=1
Batman.xp+=1
a=Player("a","")
userlist["a"]=a
Divyam.xp+=1
Spider_Man.xp+=1
Batman.xp+=1
Batman.xp+=1
Divyam.xp+=1
Batman.xp+=3
Batman.xp+=1
Batman.xp+=1
Divyam.xp+=1
Rajat_Joshi=Player("Rajat_Joshi","1234567890")
userlist["Rajat_Joshi"]=Rajat_Joshi
Div=Player("Div","HTML")
userlist["Div"]=Div
HTML=Player("HTML","Div")
userlist["HTML"]=HTML
Div.xp+=1
New_User=Player("New_User","username")
userlist["New_User"]=New_User
Batman.xp+=1
Batman.xp+=1
Divyam.xp+=1
Batman.xp+=1
Batman.xp+=1
Divyam.xp+=1
Divyam.xp+=1
Batman.xp+=1
Divyam.xp+=1
_.xp+=1
The1=Player("The1","hehe")
userlist["The1"]=The1
_.xp+=1
Batman.xp+=1
Divyam.xp+=1
_.xp+=1
Batman.xp+=1
Batman.xp+=1
Divyam.xp+=1
Batman.xp+=1
Batman.xp+=1
_.xp+=1
_.xp+=1
Divyam.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
Batman.xp+=1
Batman.xp+=1
_.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
Batman.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
s=Player("s","")
userlist["s"]=s
Batman.xp+=1
_.xp+=1
Divyam.xp+=1
Batman.xp+=1
Divyam.xp+=1
Divyam.xp+=1
Divyam.xp+=1
Divyam.xp+=1
Divyam.xp+=1
_.xp+=1
Batman.xp+=1
a.xp+=1
_.xp+=1
q=Player("q","")
userlist["q"]=q
_.xp+=1
a.xp+=1
Divyam.xp+=1
Divyam.xp+=1
Batman.xp+=1
_.xp+=1
Batman.xp+=1
_.xp+=1
_.xp+=1
Batman.xp+=1
a.xp+=1
Batman.xp+=1
_.xp+=1
Batman.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
a.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
Batman.xp+=1
_.xp+=1
_.xp+=1
a.xp+=1
Batman.xp+=1
Divyam.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1
_.xp+=1