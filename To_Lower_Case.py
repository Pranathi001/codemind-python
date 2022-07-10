a=input()
for i in range(len(a)):
    if ord(a[i])>=65 and ord(a[i])<=90:
        z=a[i]
        z=ord(a[i])
        z=z+32
        z=chr(z)
        a=a[:i]+z+a[i+1:]
print(a)