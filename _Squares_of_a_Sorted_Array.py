n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    i=i**2
    r.append(i)
r.sort()
print(*r)