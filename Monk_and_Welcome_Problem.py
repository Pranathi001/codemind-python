n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    c.append(int(a[i]+b[i]))
print(' '.join([str(i)for i in c]))