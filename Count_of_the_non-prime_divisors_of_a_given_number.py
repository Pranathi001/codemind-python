def prime(n):
    if n==1:
        return 1
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 1
        return 0
        
n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0 and prime(i):
        count+=1
print(count)