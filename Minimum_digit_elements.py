n=int(input())
l=list(map(int,input().split()))
r=[]
c=0
for i in l:
    i=str(i)
    k=len(i)
    r.append(k)
m=min(r)
for i in r:
    if i==m:
        c+=1
print(c)