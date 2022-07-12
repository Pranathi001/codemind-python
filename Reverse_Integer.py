n=int(input())
rev=0
flag=0
if n<0:
    n*=-1
    flag+=1
while n:
    r=n%10
    rev=(rev*10)+r
    n=n//10
if flag!=0:
    rev=-(rev)
print(rev)