n=int(input())
l=list(map(int,input().split()))
r=[]
k=0
a,b=map(int,input().split())
for i in l:
    if i>=a and i<=b:
        r.append(i)
if len(r)==0:
    print("-1")
else:
    print(min(r))