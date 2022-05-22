n=int(input())
sqn=pow(n,2)
i=10
r=10
t=0
while r!=sqn:
    r=sqn%i
    if n==r:
        print('Automorphic Number')
        t=1
        break
    i*=10
if t==0:
    print('Not an Automorphic Number')