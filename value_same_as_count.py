n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if l.count(i)==i:
        if i not in r:
            r.append(i)
print(len(r))