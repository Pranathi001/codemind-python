n=int(input())
l=list(map(int,input().split()))
flag=0
for i in l:
    if l.count(i)==1:
        print(i,end=" ")
        flag=1
if flag==0:
    print("-1")