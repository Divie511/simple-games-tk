from tkinter import *
class labels:
    def __init__(self):
        self.label=Label(canvas,width=2,height=2)
        self.change=0
        self.label.grid(row=r,column=c,padx=1,pady=1)
        self.label.bind("<Button-1>",lambda e:self.colour())
    def colour(self):
        if self.change==0:
            self.label.config(bg='black')
            self.change=1
        else:
            self.label.config(bg='white')
            self.change=0
def create_labels():
    global r,c
    for j in range(0,17):
        for i in range(0,17):
            labels()
            c+=1
        r+=1
        c=0
    
r=c=0
root=Tk()
canvas=Canvas(root,width=400,height=400,bg='blue')
canvas.pack()
create_labels()
root.mainloop()
