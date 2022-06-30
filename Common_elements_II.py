a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=set(x).intersection(y)
r=[]
for i in x:
    if i not in z:
        r.append(i)
for i in y:
    if i not in z:
        r.append(i)
print(*r)