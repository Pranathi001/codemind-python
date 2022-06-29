n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    sum=sum+i
avg=sum//len(a)
for i in a:
    if i==avg:
        print(True)
        break
else:
    print(False)