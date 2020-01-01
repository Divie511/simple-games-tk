from tkinter import *
master = Tk()
canvas = Canvas(master,height=250,width=400)
canvas.pack() 
class movingBeam: 
    global canvas
    def __init__(self,master=None):
        self.master=master
        # to take care movement in x direction 
        self.x = 0
        # to take care movement in y direction 
        self.y = 0
        
        
        """self.canvas = Canvas(master,height=250,width=400)""" 
         
        self.rectangle = canvas.create_rectangle(75,125,100,135, fill = "red") 
         
  
        # calling class's movement method to  
        # move the rectangle 
        self.movement()
        
      
    def movement(self): 
  
        # This is where the move() method is called 
        # This moves the rectangle to x, y coordinates 
        canvas.move(self.rectangle, self.x, self.y) 
        #this creates a lag  of 50 milliseconds 
        canvas.after(10, self.movement)
      
    # for motion in negative x direction 
    def left(self, event=None): 
        self.x = -5
        self.y = 0
      
    # for motion in positive x direction 
    def right(self,event=None):  
        self.x = 5
        self.y = 0
      
    # for motion in positive y direction 
    def up(self, event=None):  
        self.x = 0
        self.y = -5
      
    # for motion in negative y direction 
    def down(self, event=None): 
        self.x = 0
        self.y = 5 

#master = Tk()
beam = movingBeam(master)
"""canvas = Canvas(master,height=250,width=400)
canvas.pack()"""
stupefy=Button(master,text='RIGHT',command=lambda : beam.right())
stupefy.pack(side=LEFT)
confringo=Button(master,text='LEFT',command=lambda:  beam.left())
confringo.pack()
#####VVVVVVVIIIIIIIMMMMMMMMPPPPPPPPP:
    #We will create the UP and DOWN buttons later when we  get to the turret positioning  stuff!!!!
master.mainloop()

