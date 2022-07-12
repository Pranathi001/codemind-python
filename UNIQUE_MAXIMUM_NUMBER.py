n=int(input())
l=list(map(int,input().split()))
a=[]
f=0
for i in l:
    if l.count(i)==1:
        f+=1
        a.append(i)
if f==0:
    print("-1")
print(max(a))