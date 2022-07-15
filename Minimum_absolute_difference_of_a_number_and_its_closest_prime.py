n=int(input())
for i in range(n,n-10,-1):
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
            break
    if c==0:
        d1=n-i
        break
for i in range(n,n+10):
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
            break
    if c==0:
        d2=i-n
        break
if d1<d2:
    print(d1)
else:
    print(d2)