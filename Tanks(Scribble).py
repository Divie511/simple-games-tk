from tkinter import *

def make_label(parent, img):
    global frame
    label = Label(parent, image=img)
    label.grid(row=5,column=5)
    message=Label(frame,text='1.It is the launch day of an AR(Augmented Reality) game that issuing to revolutionise \nthe gaming industry. \nIt is called’ TANK WARS’. The only requirement to play\n that game is Wi-fi and electricity \nwhich will power the headgear(HELLECTRICITY aka HELO)\n used to play this game which the\n players will have to buy. It costs \nonly $200 so the gear is expected to sell out.').grid(row=5,column=1)
    my_rect=frame.create_polygon([200,300,200,350,300,350,200,300],fill='red')
    frame.move(my_rect,0,-135)
root = Tk()
frame = Canvas(root, width=400, height=400, background='white')
frame.pack_propagate(0)    
frame.pack()
img = PhotoImage(file='Villager.png')
make_label(frame, img)

root.mainloop()
