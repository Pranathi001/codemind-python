n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
sum=0
for i in range(len(l)):
    if l[i]==1:
        sum=sum+(2**i)
print(sum)