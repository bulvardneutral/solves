
with open("uloha.txt") as f:
    b = f.readlines()
    nl = [x.strip() for x in b]
    for i in range(len(b)):
        print(f"{nl[i]} {len(nl[i].split())}")
    print(len(b))