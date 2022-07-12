def len(n):
    len=0
    while n>0:
        len+=1
        n=n//10
    return len
n,x=map(int,input().split())
power=pow(10,x)
last=n%power
l=len(n)
while l!=x:
    n=n//10
    l=l-1
first=n
diff=abs(first-last)
print(diff)