n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
l=max(x)
for i in x:
    if i>=a and i<=b:
        if i==l:
            print("-1")
            break
else:
    print(l)