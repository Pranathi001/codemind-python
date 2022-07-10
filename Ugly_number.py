n=int(input())
x=0
while n!=1:
    if n%5==0:
        n/=5
    elif n%3==0:
        n/=3
    elif n%2==0:
        n/=2
    else:
        x=1
        print("Not Ugly Number")
        break
if x==0:
    print("Ugly Number")