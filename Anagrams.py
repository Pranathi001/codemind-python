n=input()
n=n.lower()
m=input()
m=m.lower()
f=0
for i in n:
    if i not in m:
        f=1
if f==0:
    print(True)
else:
    print(False)