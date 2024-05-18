import string
with open("uloha.txt") as f:

    a = f.readlines()
    lst = [x.strip() for x in a]
res = []
for i in (lst):
    tl = []
    for j in i:
        if j in string.ascii_lowercase:
            tl.append(j.upper())
        elif j in string.ascii_uppercase:
            tl.append(j.lower())
        else:
            tl.append(j)
    res.append("".join(tl))
print("\n".join(res), end="")
    


