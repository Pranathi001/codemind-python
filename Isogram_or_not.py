n=input()
f=0
for i in n:
    if n.count(i)>1:
        f=1
if f==0:
    print(True)
else:
    print(False)