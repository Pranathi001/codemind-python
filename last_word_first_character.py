n=input()
n=n.split()
r=[]
for i in range(len(n)):
    m=n[len(n)-1]
    for j in m:
        if j not in r:
            r.append(j)
        break
print(*r)