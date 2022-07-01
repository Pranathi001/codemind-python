s=input()
c=0
count=0
for i in s:
    if i=='L':
        c-=1
    else:
        c+=1
    if c==0:
        count+=1
print(count)