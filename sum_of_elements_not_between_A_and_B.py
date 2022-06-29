n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in x:
    if i<a or i>b:
        sum=sum+i
print(sum)