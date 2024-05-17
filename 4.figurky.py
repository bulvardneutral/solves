figurky = "vjsKksjv"
opacne = figurky[::-1]

nove = ""

for i in range(len(figurky)//2):
    nove += figurky[i]
    nove += opacne[i]

print(nove)