with open("uloha_1.txt") as f:
    a = f.readlines()
    lst = []
    for x in a:
        lst.append(x.strip())


for i in range(len(lst)):
    j = lst[i]
    year = (j.split())
    rok = int(year[2])
    if rok % 4 == 0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                print(rok, "priestupny")
            else:
                print("nie")
        else:
            print(rok, "priestupny")
    
    else:
        print("nie")


