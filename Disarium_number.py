def length(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
n=int(input())
sum=0
rem=0
len=length(n)
num=n
while num>0:
    rem=num%10
    sum=sum+int(pow(rem,len))
    num=num//10
    len=len-1
if sum==n:
    print("True")
else:
    print("False")