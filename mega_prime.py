def mega(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return("Not Mega Prime")
            break
    else:
        d=0
        pd=0
        while n:
            r=n%10
            n=n//10
            d+=1
            if r==3 or r==2 or r==5 or r==7:
                pd+=1
    if d==pd:
        return("Mega Prime")
    else:
        return("Not Mega Prime")
n=int(input())
print(mega(n))