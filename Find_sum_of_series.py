n=int(input())
s=0
for i in range(n,0,-1):
    r=1/i
    s+=r
print('{:.2f}'.format(s))