def prime_range(x,y):
    count=0
    for i in range(x,y+1):
        if i>1:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                    count+=1
    print(count)
x=int(input())
y=int(input())
prime_range(x,y)