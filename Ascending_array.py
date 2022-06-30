n=int(input())
a=list(map(int,input().split()))
c=0
x=0
min=0
for i in a:
    if min<i:
        min=i
        c+=1
    else:
        x+=1
if(c==len(a)):
    print("yes")
else:
    print("no")