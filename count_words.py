n=input()
n=n.lower()
n=n.split()
r=[]
v='aeiou'
for i in n:
    for j in v:
        if i.startswith(j):
            r.append(i)
print(len(r))