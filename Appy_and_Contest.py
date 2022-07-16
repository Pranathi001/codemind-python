x=int(input())
for i in range(0,x):
    n,a,b,k=map(int,input().split())
    I=0
    if(a%b==0):
        I=a
    elif(b%a==0):
        I=b
    else:
        I=a*b
    f=n//I
    c=n//a
    d=n//b
    c=c-f
    d=d-f
    if c+d>=k:
        print('Win')
    else:
        print('Lose')