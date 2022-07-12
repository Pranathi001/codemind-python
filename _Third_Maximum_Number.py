n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
r=[]
for i in s:
    if i not in r:
        r.append(i)
length=len(r)
for i in range(0,len(r)):
    if i==length-3:
        print(r[i])
        break
else:
    print(max(r))