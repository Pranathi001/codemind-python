n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if l.count(i)==i:
        if i not in r:
            r.append(i)
if len(r)==0:
    print("-1")
for i in r:
    print(i,end=" ")