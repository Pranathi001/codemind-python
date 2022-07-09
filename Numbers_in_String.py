n=input()
sum=0
d="0123456789"
for i in n:
    if i in d:
        z=int(i)
        sum=sum+z
print(sum)