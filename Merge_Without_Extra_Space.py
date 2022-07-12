n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    k=l+m
    print(*sorted(k))