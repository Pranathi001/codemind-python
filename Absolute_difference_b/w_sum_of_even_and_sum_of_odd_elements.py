n=int(input())
arr=list(map(int,input().split()))
e,o=0,0
for i in range(n):
    if arr[i]%2:
        o+=arr[i]
    else:
        e+=arr[i]
print(abs(e-o))