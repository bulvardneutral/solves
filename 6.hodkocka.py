import tkinter as tk
import random
n = 50

for i in range(n):
    number = random.randint(1,6)
    print(number)
root = tk.Tk()
root.geometry("500x500")
sirka, vyska = 500, 500
a = 50
canvas = tk.Canvas(root, width=sirka, height=vyska)
canvas.pack()

canvas.create_rectangle(sirka//2-a, vyska//2-a, sirka//2+a, vyska//2+a)
canvas.create_text(sirka//2, vyska//2, text=str(number), font="Ariel, 25")


root.mainloop()