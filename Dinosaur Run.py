from tkinter import *

def jump(e):
    global grounded
    if e == 50:
        if not grounded: return
        else: grounded = False
    if e==0: e-=1
    x = -3 if e>0 else 3
    canvas.move(dino,0,x)
    if e == -50:
        grounded = True
        return
    canvas.after(2,lambda: jump(e-1))

def spawn():
    pass

root = Tk()
canvas = Canvas(root,width = 1000,height = 300,bg="#FFF")
ground = Canvas(root,width = 1000,height = 100,bg="#000",highlightbackground = "#000")
canvas.pack()
ground.pack()
dino = canvas.create_rectangle(150,250,180,300, fill = "#000")
grounded = True
root.bind("a",lambda x: jump(50))
root.mainloop()