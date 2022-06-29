n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    if i%2!=0:
        n=a[i]
print(i)