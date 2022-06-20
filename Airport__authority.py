def amount(n,ist,t):
    s=0
    for i in range(n):
        if ist[i]>t:
            s+=2
        else:
            s+=1
    return s
ist=[]
n=int(input())
for i in range(n):
    w=int(input())
    ist.append(w)
t=int(input())
print(amount(n,ist,t))