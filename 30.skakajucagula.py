# import tkinter as tk

# root = tk.Tk()

# sirka = 500

# vyska = 500

# root.geometry("500x500")
# canvas = tk.Canvas(root, width=sirka, height=vyska)
# canvas.pack()
# r = 20

# x,y = (sirka//2), 30
# a = canvas.create_oval(x-r, y-r, x+r, y+r)
# canvas.move(a)

# for i in range(10):
#     y += 30
#     canvas.create_oval(x-r, y-r, x+r, y+r)
#     # canvas.after(1000)
#     i+=1
#     print(y)
#     # canvas.after()
#     # x1, y1 = (sirka//2), 30
#     # x,y = (sirka//2), 30 + 30
#     # print(x1,y1)
#     # print(x,y)
#     # canvas.create_oval(x-r, y-r, x+r, y+r)
# root.mainloop()


# import tkinter as tk

# def animate():
#     global rychlost
#     canvas.move(gula, 0, rychlost)
#     pos = canvas.coords(gula)
#     if pos[1] <= 0 or pos[3] >= 500:  # top and bottom wall collision detection
#         rychlost = rychlost * -1
#     root.after(20, animate)  # repeat the animation after 20 milliseconds

# root = tk.Tk()
# root.geometry("500x500")
# canvas = tk.Canvas(root, width=500, height=500, bg='white')
# canvas.pack()
# x, y = 250,30
# r = 20
# gula = canvas.create_oval(x-r, y-r,x+r, y+r, fill='blue')  # initial position of the ball
# rychlost = 2  # initial vertical velocity

# animate()

# root.mainloop()


import tkinter as tk

def pohyb():
    global rychlost
    canvas.move(gula, 0, rychlost)
    pozicia = canvas.coords(gula)
    if pozicia[1] == 0 or pozicia[3] == 500:
        rychlost*=-1
    canvas.after(20, pohyb)

root = tk.Tk()
sirka = 500
vyska = 500

root.geometry("500x500")

canvas = tk.Canvas(width=sirka, height=vyska)
canvas.pack()

x,y = 500//2, 30

r = 20

gula = canvas.create_oval(x-r,y-r,x+r,y+r, fill="blue")

rychlost = 5

pohyb()

root.mainloop()