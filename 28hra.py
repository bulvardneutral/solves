import tkinter as tk
import random


root = tk.Tk()
root.geometry("500x500")
pocet = 0
vyska = 20
hrac1 = 0
hrac2 = 0


vysledok = tk.Label(root, font="25")
vysledok.place(x=220, y=400)

def koniec():
    root.destroy()

def generuj():
    global pocet, vyska, hrac1, hrac2
    pocet +=1
    if pocet % 2 == 1:
        vyska += 50
        x = random.randint(1,21)
        tk.Label(root, text=x, font="25").place(x=200, y=vyska)
        hrac1 = 0 +  x

    else:
        y = random.randint(1,21)
        tk.Label(root, text=y, font="25").place(x=300, y=vyska)
        hrac2 = 0 + y
        
    if pocet % 2 == 0:
        if hrac1 > hrac2:
            vysledok.config(text="Vyhral Hráč 1")
        elif hrac1 < hrac2:
            vysledok.config(text="Vyhral Hráč 2")
        else:
            vysledok.config(text="Remíza")
    elif pocet == 11:
        root.destroy()
        
tk.Button(root, text="Stop", command=generuj).place(x=250, y=350)
tk.Button(root, text="Ukončiť", command=koniec).place(x=240, y=460)
tk.Label(text="Hráč 1", font="25").place(x=188, y=10)
tk.Label(text="Hráč 2", font="25").place(x=290, y=10)

tk.Label(text="1. kolo", font="25").place(x=100, y=70)
tk.Label(text="2. kolo", font="25").place(x=100, y=120)
tk.Label(text="3. kolo", font="25").place(x=100, y=170)
tk.Label(text="4. kolo", font="25").place(x=100, y=220)
tk.Label(text="5. kolo", font="25").place(x=100, y=270)

root.mainloop()



# import tkinter as tk
# import random

# root = tk.Tk()

# root.geometry("500x500")
# sirka, vyska = 500, 400
# canvas = tk.Canvas(root, width=sirka, height=vyska, bg="white")
# canvas.pack()

# x = random.randint(1,21)
# p = 0
# h = 0 

# def stop():
#     global h, p, x 
#     h+=1
#     if p < 10:
#         if p % 2 == 0:
#             canvas.create_text(125,50*(p//2),font=('Helvetica','30','bold'),text=x, anchor="nw")
#         else:
#             canvas.create_text(350,50*(p//2),font=('Helvetica','30','bold'), text=x, anchor="nw")
#         p+=1

# button = tk.Button(root, text="Stop", command=stop)
# button.pack()

# text = ""
# while p < 10:
#     x = random.randint(1,21)
#     canvas.delete(text)
#     if p % 2 == 0:
#         text = canvas.create_text(125,50*(p//2),font=('Helvetica','30','bold'), text=x, anchor="nw")
#     else:
#         text = canvas.create_text(350,50*(p//2),font=('Helvetica','30','bold'), text=x, anchor="nw")
    
#     canvas.update()
#     root.after(50)
# root.mainloop()


