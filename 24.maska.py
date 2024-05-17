with open("uloha_1.txt") as f:
    text = f.readline().strip()

with open("maska_1.txt") as s:
    cislo = s.readline().split()
    lst = [int(x) for x in cislo]

count = 0
nl = []
for i in range(len(lst)):
    count += lst[i]
    nl.append(count)

g = [0]
g.extend(nl)
g.pop(-1)

for j in range(len(g)):
    print(text[g[j]:nl[j]], end=" ")










# with open('maska_1.txt') as subor:
#     pocet_riadkov = len(subor.readlines())

# with open('maska_1.txt') as subor:
#     with open("uloha_1.txt") as file:

#         for _ in range(pocet_riadkov):
#             riadok = subor.readline()
#             veta = file.readline()
#             cisla = riadok.strip().split()   
#             list_cisla = []
            
#             for x in cisla:
#                 list_cisla.append(int(x))
            
#             celkovo = 0
#             novy_list = []
            
#             for i in list_cisla:
#                 celkovo = celkovo + i
#                 novy_list.append(celkovo)
            
#             print(f"{veta[:novy_list[0]]} {veta[novy_list[0]:novy_list[1]]} {veta[novy_list[1]:novy_list[2]]} {veta[novy_list[2]:novy_list[3]]} {veta[novy_list[3]:novy_list[4]]}")



            
        
    
            
