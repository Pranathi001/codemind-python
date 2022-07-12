n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
r=[]
sum=0
for i in range(len(l)):
    k=l[i]*pow(10,i)
    sum=sum+k
x=sum+1
while x!=0:
    rem=x%10
    r.append(rem)
    x=x//10
print(*r[::-1])