__author__ = 'li'
from tkinter import *
import random
import time

class Game:
    def __int__(self):
        self.tk=Tk()
        self.tk.title("李翔的游戏1.0.0")
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost",1)
        self.cavas=Canvas(self.tk,width=500,height=500,highlightthickness=0)
        self.cavas.pack()
        self.cavas.update()
        self.canvas_width=500
        self.cavas_height=500
        self.bg=PhotoImage(file="background.gif")
        w =self.bg.width()
        h = self.bg.height()
        for x in range(0,5):
            for y in range(0,5):
                self.canvas.create_image(x*w,y*h,image=self.bg,anchor='nw')
        self.sprites=[]
        self.running = True

    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)
g = Game()
g.mainloop()
        
