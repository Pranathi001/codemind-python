n=int(input())
s=list(map(int,input().split()))
min=9999
f=0
for i in range(len(s)):
    if min>s[i]:
        min=s[i]
for i in range(min,0,-1):
    f=0
    for j in range(len(s)):
        if s[j]%i!=0:
            f=1
            break
    if f==0:
        print(i)
        break