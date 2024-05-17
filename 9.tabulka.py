import tkinter as tk 

root = tk.Tk()

with open("uloha_1.txt") as f:
    tabulka = int(f.readline().strip())
    cisla = f.readline().split()
    lst = [int(x) for x in cisla]


count = 0
nl = []
for _ in range(tabulka):
    count += tabulka
    nl.append(count)


g = [0]
g.extend(nl)
g.pop(-1)
canvas = tk.Canvas()
canvas.pack()
x, y = 200,50
for i in range(tabulka):
    a = str(("".join(str(lst[g[i]:nl[i]]))))
    y +=25
    canvas.create_text(x,y, text=a)

root.mainloop()













import tkinter as tk
tabulky = []
with open("uloha_1.txt", 'r') as subor:
    riadky = subor.readlines()
    for i in range(0, len(riadky), 2):
        n = int(riadky[i])
        tabulka = []
        for j in range(n):
            cisla = riadky[i+1].split()
            tabulka.append(" ".join(cisla[j*n:j*n+n]))
        tabulky.append(tabulka)

for tabulka in tabulky:
    n = len(tabulka)
    root = tk.Tk()

    for i in range(n):
        label = tk.Label(root, text=tabulka[i], width=15, height=2)
        label.grid(row=i, column=0)

    root.mainloop()