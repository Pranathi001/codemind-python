def palin(n):
    if n==n[::-1]:
        return True
    else:
        return False
n=input()
k=n.split()
c=0
for i in k:
    s=i.casefold()
    if(palin(s)):
        c+=1
print(c)