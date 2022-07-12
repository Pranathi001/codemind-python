n=int(input())
k=n/2
l=list(map(int,input().split()))
r=[]
for i in l:
    if l.count(i)>=k:
        if i not in r:
            r.append(i)
print(*r)