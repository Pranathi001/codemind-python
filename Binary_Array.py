n=int(input())
l=list(map(int,input().split()))
f=0
for i in l:
    if i==1 or i==0:
        f+=1
if f==len(l):
    print(True)
else:
    print(False)