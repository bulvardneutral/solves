import tkinter as tk 


root = tk.Tk()
sirka, vyska = 500, 500
canvas = tk.Canvas(root, width=sirka, height=vyska)
canvas.pack()

canvas.create_polygon(200,200,400,200,350,250, 250,250, fill="white", outline="black", width=3)
canvas.create_line(300,200, 300,100, width=3)
canvas.create_polygon(300,100, 350,125, 300,150, fill="white", width=3, outline="black")
root.mainloop()
