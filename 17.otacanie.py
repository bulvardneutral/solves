# import tkinter as tk
# from math import sin, cos, pi

# def otoc(alfa, sur):
#     if sur == 1:
#         return cos(alfa * pi / 180)
#     if sur == 0:
#         return sin(alfa * pi / 180)

# def obdlznik(alfa, x1, y1, x2, y2):
#     px = x1 + round((x2 - x1) * otoc(alfa, 1))
#     py = y2 - round((x2 - x1) * otoc(alfa, 0))
#     dx = x1 - round((y2 - y1) * otoc(alfa, 0))
#     dy = y2 - round((y2 - y1) * otoc(alfa, 1))
#     canvas.create_line(x1, y2, px, py, tag="")
#     canvas.create_line(x1, y2, dx, dy, tag="")
#     canvas.create_line(px - (-dx + x1), py - (-dy + y2), dx, dy, tag="")
#     canvas.create_line(px - (-dx + x1), py - (-dy + y2), px, py, tag="")

# root = tk.Tk()
# root.geometry("400x400")


# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()


# obdlznik(0, 270, 180, 390, 290)

# obdlznik(90, 270, 180, 390, 290)

# root.mainloop()


import tkinter as tk
from math import sin,cos,pi
import time


with open("uloha_260224.txt") as f:

    a = f.readline().strip().split()
    nl = [int(x) for x in a]
    print(nl)

def otoc(alfa,sur):
    if sur==1:
        return cos(alfa*pi/180)
    if sur==0:
        return sin(alfa*pi/180)        

def obdlznik(alfa,x1,y1,x2,y2, wid):
    px = x1+round((x2-x1)*otoc(alfa,1))
    py = y2-round((x2-x1)*otoc(alfa,0))
    dx = x1-round((y2-y1)*otoc(alfa,0))
    dy = y2-round((y2-y1)*otoc(alfa,1))
    canvas.create_line(x1,y2,px,py,tag="", width=wid)
    canvas.create_line(x1,y2,dx,dy,tag="",  width=wid)
    canvas.create_line(px-(-dx+x1),py-(-dy+y2),dx,dy,tag="",  width=wid)
    canvas.create_line(px-(-dx+x1),py-(-dy+y2),px,py,tag="",  width=wid)

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
alfa = 0
# for i in range(10):
#     obdlznik(alfa,nl[0], nl[1], nl[2], nl[3],3)
#     canvas.update()
#     canvas.after(500)
#     alfa-=15

obdlznik(90,nl[0], nl[1], nl[2], nl[3],1)
obdlznik(0,nl[0], nl[1], nl[2], nl[3],3)

root.mainloop()