with open("uloha_1.txt", "r") as f:
    a = f.readlines()
    nl = []
    for x in a:
        nl.append(x.strip())

    
    
den = int(input("Ktory den: 1 alebo 3> "))

pocet = (int(nl[den-1])//2)
c = 0
h = 0
count = 0
for i in range(pocet):
    stat = (nl[den])
    c += 2
    h = c - 2
    result = (stat[h:c])
    if result == "SZ":
        count += 1
print(count)