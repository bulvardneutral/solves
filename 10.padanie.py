import tkinter as tk 

def padanie_1():
    global rychlost_1
    canvas.move(rovnobeznik, 0, rychlost_1)
    pozicia = canvas.coords(rovnobeznik)
    if pozicia[3] == 500:
        rychlost_1 = 0
        padanie()
    else:
        canvas.after(20, padanie_1)

def padanie():
    global rychlost_2
    canvas.move(gula, 0, rychlost_2)
    poz = canvas.coords(gula)
    if poz[3] == 500:
        rychlost_2 = 0
        padanie_2()
    else:
        canvas.after(20, padanie)

def padanie_2():
    global rychlost_3
    canvas.move(troj, 0, rychlost_3)
    poz = canvas.coords(troj)
    if poz[3] == 500:
        rychlost_3 = 0
    else:
        canvas.after(20, padanie)
root = tk.Tk()
root.geometry("500x500")

sirka = 500
vyska = 500

canvas = tk.Canvas(root, width=sirka, height=vyska)
canvas.pack()

x,y = sirka//2, 30
r = 15 
gula = canvas.create_oval(x-r,y-r,x+r,y+r, fill="blue")
rovnobeznik = canvas.create_rectangle(100 ,10, 150,40, fill="blue")
troj = canvas.create_polygon(350 ,10, 320,40, 380, 40, fill="blue")

rychlost_3 = 5
rychlost_2 = 5
rychlost_1 = 5


padanie_1()
root.mainloop()


