n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if i==0:
        r.append(i)
for i in l:
    if i not in r:
        print(i,end=" ")
for i in r:
    print(i,end=" ")