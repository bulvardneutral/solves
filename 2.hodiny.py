import tkinter as tk
from math import sin, cos, radians, pi


def velka(m):
    x = 500/2
    y = 500/2
    dx = cos((-90+6*m)*pi/180)
    dy = sin((-90+6*m)*pi/180)
    canvas.create_line(x,y,x+200*dx,y+200*dy)

def mala(h,m):
    x = 500/2
    y = 500/2
    dx = cos((-90+(5*h+(m/12))*6)*pi/180)
    dy = sin((-90+(5*h+(m/12))*6)*pi/180)
    canvas.create_line(x,y,x+(200/2)*dx,y+(200/2)*dy, width=2)


root = tk.Tk()
canvas = tk.Canvas(width=500, height=500)
canvas.pack()
x,y = 250,250
u = -90
r = 200

for i in range(1,13):
    u+=30
    dx = x + r*cos(radians(u))
    dy = y + r*sin(radians(u))
    canvas.create_text(dx, dy, text=str(i), font="Ariel, 20")


velka(30)
mala(9,00)

root.mainloop()
