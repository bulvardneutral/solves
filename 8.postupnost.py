
with open("uloha_1.txt") as f:
    a = f.readlines()
    nl = [x.strip() for x in a]
    print(nl)

for i in range(len(nl)):
    lst = [int(j.replace("a", "10").replace("b", "11").replace("c", "12").replace("d", "13").replace("e", "14").replace("f", "15")) for j in nl[i]]
    sor = sorted(lst)
    if lst == sor:
        print(f"{lst} vzsostupne")
    else:

        print(lst)
