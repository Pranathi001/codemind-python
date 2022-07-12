n=int(input())
for i in range(n):
    t=int(input())
    l=list(map(int,input().split()))
    r=[]
    for j in range(1,t+1):
        if j not in l:
            r.append(j)
            break
    print(*r)