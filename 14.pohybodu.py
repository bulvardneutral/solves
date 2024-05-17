import tkinter as tk

with open("uloha_1.txt") as f:
    suradnice = f.readline().split()
    smer = f.readline().strip()
    nl = [j for j in smer]
    lst = [int(x.strip()) for x in suradnice]



root = tk.Tk()
root.geometry("500x500")
sirka, vyska = 500, 500
r = 2
ryhchlost = 1
canvas = tk.Canvas(root, width=sirka, height=vyska)
canvas.pack()
x, y = lst[0], lst[1]
bod = canvas.create_rectangle(x-r, y-r, x+r, y+r, fill="green")



for i in range(len(nl)):
    if nl[i]=="v":
        dx = x + 1 
        dy = y  
        canvas.create_line(x,y,dx,dy,width=1, fill="green" )
        root.update()
        canvas.after(100)
        x = dx
        y = dy
    elif nl[i] == "j":
        dx = x  
        dy = y + 1 
        canvas.create_line(x,y,dx,dy,width=1, fill="green" )
        root.update()
        canvas.after(100)
        x = dx
        y = dy
    elif nl[i] == "z":
        dx = x - 1  
        dy = y  
        canvas.create_line(x,y,dx,dy,width=1, fill="green" )
        root.update()
        canvas.after(100)
        x = dx
        y = dy
    elif nl[i] == "s":
        dx = x   
        dy = y - 1 
        canvas.create_line(x,y,dx,dy,width=1, fill="green" )
        root.update()
        canvas.after(100)
        x = dx
        y = dy
root.mainloop()


