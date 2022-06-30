n=input()
n=n.lower()
v=set("aeiou")
for i in n:
    if i in v:
        v.remove(i)
if len(v)==0:
    print("0")
else:
    v=sorted(v)
    print(*v)