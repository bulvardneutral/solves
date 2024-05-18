
def posun(s):
    s = s[len(s)-1] + s[0:len(s)-1]
    return s 

with open("text.txt") as f:
    a = f.readlines()
    lst = [x.strip() for x in a]
print(lst)

for i in range(len(lst)):
    print(posun(lst[i]))

