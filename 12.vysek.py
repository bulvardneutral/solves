import tkinter as tk 
import random
with open("uloha_1.txt") as f:
    a = f.readline().split()
    print(a)
    nl = [int(x) for x in a]



root = tk.Tk()
root.geometry("640x480")
sirka, vyska = 640, 480
canvas = tk.Canvas(root, width=sirka, height=vyska)
canvas.pack()
n = 10000
r = 0.1
# canvas.create_rectangle(nl[0],nl[1],nl[2], nl[3])
for i in range(n):
    x = random.randint(0,640)
    y = random.randint(0,480)
    if x >= nl[0] and x <= nl[2] and y >= nl[1] and y <= nl[3]: 
        canvas.create_rectangle(x-r,y-r,x+r,y+r, fill="green")
    else:
        pass 
root.mainloop()