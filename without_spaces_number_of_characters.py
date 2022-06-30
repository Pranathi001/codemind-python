n=input()
k=len(n)
for i in n:
    if i.isspace()==True:
        k-=1
print(k)