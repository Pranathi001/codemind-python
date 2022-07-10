n=int(input())
for i in range(0,n):
    a=input()
    f="0123456789"
    c=0
    for i in a:
        if i in f:
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")