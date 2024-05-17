n = int(input("Pocet prvkov: "))
p = []
r = ""
for i in range(1, n+1):
    for j in range(1, n+1):
        x = i*j
        if x < 10:
            y = x
            p.append(r)
            p.append(y)
        elif x > 9:
            p.append(x)
        if j == n:
            print(*p)
            p.clear()