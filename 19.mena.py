mena = "Denisa, Karol, Anna, Julia, Peter, Barbara, Zoltan, Zofia"

a = mena.split(", ")
b = sorted(a)

import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
sirka, vyska = 500, 500
canvas = tk.Canvas(root, width=sirka, height=vyska)
canvas.pack()
x, y = sirka//2, 50
for i in range(len(a)):
    canvas.create_text(sirka//2, y, text=b[i])
    y += 25

root.mainloop()

with open("mena.txt", "w") as subor:
    for j in range(len(a)+1):
        print(b[j], file=subor)