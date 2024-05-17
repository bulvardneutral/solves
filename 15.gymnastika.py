with open("znamky.txt", "r") as f:
    lst = f.readlines()
    nl = []
    for i in range(len(lst)):
        a = (lst[i].strip())
        x, y = float(a[0:a.index(" ")]), float(a[a.index(" ")::])
        c = (x + y)
        nl.append(c)
mini = (min(nl))

porad = nl.index(mini)

print(f"Najnizsiu znamku {mini} dosiahol sutaziaci cislo {porad+1}")