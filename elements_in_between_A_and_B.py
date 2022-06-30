n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
count=0
for i in l:
    if i>=a and i<=b:
        count+=1
        print(i,end=" ")
if count==0:
    print("-1")