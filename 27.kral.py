odd = True 
    
with open('uloha_1.txt') as f: 
    nl = []
    res = []
    for line in f: 
        if odd: 
            res.append(int(line.strip()))
        else:
            nl.append(line.strip())
        odd = not odd 
lst = []
print(res)
for i in range(len(res)):
    lst = [(int(x)//2)+1 for x in nl[i] if x != " "]
    print(f"Pocet skupin: {res[i]}, potrebny pocet hlasov: {sum(lst)}")