n=input()
f=0
for i in n:
    if n.count(i)==1:
        print(i,end=" ")
        f+=1
        break
if f==0:
    print("-1")