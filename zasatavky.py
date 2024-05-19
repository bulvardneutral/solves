import tkinter as tk

with open("zastavky.txt") as f:
    lst = f.readlines()
    zastavky = [x.strip() for x in lst]
   


root = tk.Tk()
root.geometry("500x500")
sirka, vyska = 500, 500
r = 20
canvas = tk.Canvas(root, width=sirka, height=vyska)
canvas.pack()

canvas.create_line(100,250, 420,250, width=3)
gula1 = canvas.create_oval(100-r,250-r,100+r,250+r, fill="red")
gula2 = canvas.create_oval(420-r,250-r,420+r,250+r, fill="red")
text1 = canvas.create_text(120,200, text=zastavky[0], angle=45)
text2 = canvas.create_text(440,200, text=zastavky[-1], angle=45)
zastavky.pop(0)
zastavky.pop(-1)

dx, dy, r2 = 110, 250, 8

for i in range(len(zastavky)-2):
    dx += 22
    hello = canvas.create_oval(dx-r2,dy-r2,dx+r2,dy+r2,fill="white", outline="red")
    canvas.create_text(dx+20,215, text=zastavky[i], angle=45, anchor="s")
    

root.mainloop()

