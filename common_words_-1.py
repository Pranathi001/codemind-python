a=input()
b=input()
a=a.lower()
b=b.lower()
n=a.split()
s=b.split()
c=0
for i in n:
    for j in s:
        if i==j:
            c+=1
print(c)