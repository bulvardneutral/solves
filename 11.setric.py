import tkinter as tk

def pohyb():
    global rychlost
    canvas.move(retazec, rychlost, 0)
    poz = canvas.coords(retazec)
    poza = canvas.bbox(retazec)
    print(poza)
    if poza[2] == 500:
        rychlost = 0     
    canvas.after(20, pohyb)


root = tk.Tk()
text = input("text> ")
sirka, vyska = 500, 500

canvas = tk.Canvas(root, width=sirka, height=vyska)
canvas.pack()

retazec = canvas.create_text(0-2*((len(text))+5), 50, text=text)
rychlost = 1


pohyb()
root.mainloop()


###########################
# zľava do prava 
# import tkinter as tk

# root = tk.Tk()

# sirka, vyska = 500, 500 
# root.geometry("500x500")
# canvas = tk.Canvas(root, width=sirka, height=vyska)
# canvas.pack()

# with open("setric.txt") as subor:
#     nl = []
#     slova = subor.readlines()
#     for x in slova:
#         a = x.strip()
#         nl.append(a)
    

# def pohyb(index, x, y, rychlost):
#     vypis = canvas.create_text(x, y, text=nl[index], font="20")  
#     pozicia = canvas.bbox(vypis)
#     while pozicia[2] <= sirka:
#         canvas.move(vypis, rychlost, 0)
#         pozicia = canvas.bbox(vypis)
#         root.update()
#         root.after(75)
    
#     canvas.delete(vypis)
#     y += 25
#     if index + 1 < len(nl):
#         pohyb(index + 1, -100, y, 3)  

# pohyb(0, -100, 20, 3)  

# root.mainloop()


# ####################################################
# zprava do ľava
# import tkinter as tk

# root = tk.Tk()

# sirka, vyska = 500, 500 
# root.geometry("500x500")
# canvas = tk.Canvas(root, width=sirka, height=vyska)
# canvas.pack()

# with open("setric.txt") as subor:
#     nl = []
#     slova = subor.readlines()
#     for x in slova:
#         a = x.strip()
#         nl.append(a)
    

# def pohyb(index, x, y, rychlost):
#     vypis = canvas.create_text(x, y, text=nl[index], font="20")  
#     pozicia = canvas.bbox(vypis)
    
#     while pozicia[0] > 0:
#         canvas.move(vypis, -rychlost, 0)
#         pozicia = canvas.bbox(vypis)
#         root.update()
#         root.after(75)
    
#     canvas.delete(vypis)
#     y += 25
#     if index + 1 < len(nl):
#         pohyb(index + 1, sirka + 100, y, 3) 

# pohyb(0, sirka + 100, 20, 3) 

# root.mainloop()
