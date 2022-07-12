n=int(input())
l=list(map(int,input().split()))
k=int(input())
first,last=-1,-1
for i in range(len(l)):
    if l[i]!=k:
        continue
    if first==-1:
        first=i
    last=i
if(first!=-1):
    print(first,last)
else:
    print("-1 -1")