def rev(n):
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
    return rev
n=int(input())
for i in range(1,n+1):
    x=int(input())
    revnum=rev(x)
    if revnum==x:
        print("True")
    else:
        print("False")