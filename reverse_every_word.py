n=input()
n=n.split()
r=[]
for i in n:
    i=i[::-1]
    r.append(i)
print(*r)