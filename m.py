import tkinter as tk
from colorsys import hsv_to_rgb
import time
import random

class mouse:
    x,y,but=0,0,None
    
    @classmethod
    def move(cls,e):
        cls.but=e.widget
        e=e.widget.grid_info()
        cls.x,cls.y=e["row"],e["column"]
        
def onclick():
    userpath.append(mouse.but)
    if userpath==path:
        
        path.append(random.choice(random.choice(buttons)))
        showpath()
        
def colorAll(coul=None):
    for x in buttons:
        for but in x:
            but["bg"]=coul if coul else but.trueBg
            
def showpath():
    for elem in path:
        elem["bg"]=elem.trueBg
        f.update()
        time.sleep(1)
        elem["bg"]="black"
        f.update()
    userpath.clear()
    
f=tk.Tk()
game=tk.Frame(f)
buttons=[]
for y in range(5):
    buttons.append([])
    for x in range(5):
        but=tk.Button(game,width=10,height=5,command=onclick)
        but.trueBg="#%02x%02x%02x" % tuple(int(elem) for elem in hsv_to_rgb(random.random(),0.5,255))
        but["activebackground"]=but.trueBg
        but.bind('<Enter>',mouse.move)
        but.grid(row=x,column=y)
        buttons[-1].append(but)

game.pack()
tk.Button(f,text="Start",command=showpath).pack(expand=True)
path=[random.choice(random.choice(buttons)) for _ in range(3)]
userpath=[]
colorAll("black")




