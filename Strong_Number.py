n=int(input())
num=n
sum=0
while n>0:
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(sum==num):
    print("The number %d is a strong number"%num)
else:
    print("The number %d is not a strong number"%num)