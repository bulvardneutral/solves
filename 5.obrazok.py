

import tkinter as tk
from PIL import Image, ImageTk
image = Image.open("bmp.bmp.bmp")
root=tk.Tk()

file=open("TTT29.txt", "w")
file.write(str(image.width))
file.write(" ")
file.write(str(image.height))
file.write("\n")

for i in range(image.height):
    for j in range(image.width):
        pxl=image.getpixel((j, i))
        print(pxl)
        if pxl>=1:
            file.write("g")
        else:
            file.write("p")
    file.write("\n")



















import tkinter as tk 

root = tk.Tk()
root.geometry("500x500")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
img = tk.PhotoImage(file="Untitled.png")
canvas.create_image(250,250, image=img)
f = open("riesenie.txt", "w")
f.write(str(img.width()))
f.write(" ")
f.write(str(img.height()))
f.write("\n")
for i in range(int(img.height())):
    for j in range(int(img.width())):
        pixel = img.get(j, i)
        if pixel[2] == 0 and pixel[1] == 0 and pixel[0] == 0:
            f.write("b")
        else:
            f.write("c")
    f.write("\n") 

root.mainloop()





# # import tkinter as tk
# # sirka = 600
# # vyska = 480
# # canvas = tk.Canvas(height=sirka, width=vyska)
# # canvas.pack()

# # img = tk.PhotoImage(file="Untitled.png")
# # ibobor = canvas.create_image((sirka//2,vyska//2), image=img)

# # with open("output.txt", "w+") as subor:
# #     subor.write(str(img.width())+"  "+str(img.height()) + "\n") #!!!
# #     for y in range(img.height()):
# #         for x in range(img.width()):
# #             if img.get(x,y) == (int(0x00), int(0x00), int(0x00)):
# #                 subor.write("c")
# #             else:
# #                 subor.write(" ")
# #         subor.write("\n")

# # tk.mainloop()
