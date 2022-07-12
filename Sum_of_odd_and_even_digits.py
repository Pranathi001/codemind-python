n=int(input())
a=list(map(int,input().split()))
sum=0
sum1=0
for i in range(len(a)):
    if i%2!=0:
        sum=sum+a[i]
    elif i%2==0:
        sum1=sum1+a[i]
if(sum-sum1)==0:
    print("YES")
else:
    print("NO")