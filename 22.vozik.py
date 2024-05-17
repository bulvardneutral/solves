
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas()
canvas.pack()

def pohyb():
    global rychlost
    canvas.move(trup, rychlost, 0)
    poz = canvas.coords(trup)
    print(poz)
    if poz[2] == 400:
        rychlost = 0
    else:
        canvas.after(100, pohyb)

def pohyb1():
    global rychlost
    canvas.move(koleso0, rychlost, 0)
    poz = canvas.coords(trup)
    print(poz)
    if poz[2] == 400-20:
        rychlost = 0
    else:
        canvas.after(100, pohyb1)

def pohyb2():
    global rychlost
    canvas.move(koleso1, rychlost, 0)
    poz = canvas.coords(trup)
    print(poz)
    if poz[2] == 400:
        rychlost = 0
    else:
        canvas.after(100, pohyb2)


dx, dy = 0,50
dx1, dy1 = 100,50
trup = canvas.create_line(dx,dy,dx1,dy1)
r = 7
rychlost = 10
x,y = 25,57
x1 = 75
koleso0 = canvas.create_oval(x-r,y-r,x+r, y+r)
koleso1 = canvas.create_oval(x1-r,y-r,x1+r, y+r)

pohyb()
pohyb1()
pohyb2()

root.mainloop()