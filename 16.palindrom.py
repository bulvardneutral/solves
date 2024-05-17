import string
veta = "Madam"

nl = []
for i in veta:
    if i in string.punctuation: 
        pass 
    else:
        nl.append(i)
lst = [j for j in nl if j != " "]
result = "".join(lst)
opacne = "".join(result[::-1].lower().split())
normalne = "".join(result.lower().split())

if normalne == opacne:
    print("palindrom")
else:
    print("nie je")