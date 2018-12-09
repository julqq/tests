from tkinter import *
import random
import time
tk = Tk()
tk.title("game whit Tkinter")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.configure(bg="orange")
canvas.pack()
tk.update()

class Ball:
    def __init__(self,canvas,shovel,color):
        self.canvas = canvas
        self.shovel = shovel
        self.id = canvas.create_oval(10,10,25,25, fill= color)
        self.canvas.move(self.id, 245, 100)
        start = [-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()  
        self.hit_Bottom = False 

    def hit_shovel(self,pos):
        shovel_pos = self.canvas.coords(self.shovel.id)
        if pos[2] >= shovel_pos[0] and pos[0] <= shovel_pos[2]:
            if pos[3] >= shovel_pos[1] and pos[3] <= shovel_pos[3]:
                return True
                return False


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_Bottom = True
            canvas.create_text(245,100,text="GAMEOVER !", font=('arial',15)) 
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if self.hit_shovel(pos) == True:
            self.y = -3

class Shovel:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill= color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0

        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw (self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        self.x = -2
    def turn_right(self,evt):
        self.x = 2 
shovel = Shovel(canvas, 'black')      
ball = Ball(canvas, shovel, 'yellow')

while 1:
    if ball.hit_Bottom == False:        
        shovel.draw()
        ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


