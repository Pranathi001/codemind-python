def count(d):
    if d<0:
        return 0
    if d==0:
        return 1
    return count(d-1)+count(d-2)+count(d-3)
n=int(input())
print(count(n))