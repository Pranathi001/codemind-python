def perfect(n):
    for i in range(1,n+1):
        if i*i==n:
            return True
    else:
        return False
n=int(input())
for i in range(1,n+1):
    x=int(input())
    print(perfect(x))