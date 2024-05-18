import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 600)
canvas.pack()

with open("uloha_1(1).txt", "r") as subor:
    a = subor.readline().split()      
                                                                               
    sirka, vyska = int(a[0]), int((a[1]))

    obrazok_data = [line.strip() for line in subor]                            
    print(obrazok_data)
    for y in range(vyska):                                                     
        for x in range(sirka):                                               
            if obrazok_data[y][x] == "c":                                     
                farba = "black"

            else:
                farba = "white"                                               
            canvas.create_rectangle(x, y, x, y, fill=farba, outline="")       

root.mainloop()
