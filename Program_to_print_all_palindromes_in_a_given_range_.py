def palindrome(n):
    rev=0
    temp=n
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if n==rev:
        return True
    return False
l=int(input())
u=int(input())
for i in range(l,u+1):
    if palindrome(i):
        print(i,end=" ")