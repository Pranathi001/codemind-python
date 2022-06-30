n=input()
k=input()
f=0
for i in range(len(n)):
    if n[i]==k:
        print(True)
        print(i)
        f+=1
        break
if f==0:
    print(False)