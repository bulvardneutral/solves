 
with open("kpn.txt") as f:
    a = f.readline()
    prva = a[0:2]
    druha = a[2:4]
    tretia = a[4::]
    hrac1 = 0
    hrac2 = 0

    x = [i for i in prva]
    if x[0] == x[1]:
        pass
    elif x[0] == "k" and x[1] == "n" or x[0] == "p" and x[1] == "k" or x[0] == "n" and x[1] == "p":
        hrac1 +=1
    else:
        hrac2+=1
    
    y = [j for j in druha]
    if y[0] == y[1]:
        pass
    elif y[0] == "k" and y[1] == "n" or y[0] == "p" and y[1] == "k" or y[0] == "n" and y[1] == "p":
        hrac1 +=1
    else:
        hrac2+=1

    z = [k for k in tretia]
    if z[0] == z[1]:
        pass
    elif z[0] == "k" and z[1] == "n" or z[0] == "p" and z[1] == "k" or z[0] == "n" and z[1] == "p":
        hrac1 +=1
    else:
        hrac2+=1
    

    print(f"hrac1: {hrac1}, hrac2: {hrac2}")

