n=int(input())
l=list(map(int,input().split()))
r=[]
f=0
for i in l:
    if i==l.count(i):
        f+=1
        r.append(i)
if f==0:
    print("-1")
s=set(r)
print(min(s),max(s))