n=input()
v="aeiouAEIOU"
r=[]
for i in n:
    if i not in r:
        if i in v:
            r.append(i)
if len(r)==0:
    print("-1")
else:
    print(*r)