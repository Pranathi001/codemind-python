n=int(input())
lst=[]
p=0
s=0
for i in range(n):
    a=list(map(int,input().split()))
    lst.append(a)
for i in range(n):
    for j in range(n):
        if i==j:
            p+=lst[i][j]
        if i==(n-j)-1:
            s+=lst[i][j]
print("Principal Diagonal:{}".format(p))
print("Secondary Diagonal:{}".format(s))