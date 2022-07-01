n=input()
m=input()
n=n.lower()
m=m.lower()
n=n.split()
m=m.split()
r=[]
for i in m:
    for j in n:
        if i==j:
            r.append(j)
print(*r)