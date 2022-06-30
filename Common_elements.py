n,m=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
r=[]
for i in l:
    for j in m:
        if i==j:
            if i not in r:
                r.append(i)
print(*r)