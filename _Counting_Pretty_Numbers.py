n=int(input())
for i in range(1,n+1):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        p=i%10
        if p==2 or p==3 or p==9:
            c+=1
    print(c)