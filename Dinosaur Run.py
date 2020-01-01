from tkinter import *

root = Tk()
canvas = Canvas(root,width = 1000,height = 300,bg="#FFF")
ground = Canvas(root,width = 1000,height = 100,bg="#000",highlightbackground = "#000")
canvas.pack()
ground.pack()

root.mainloop()