l=int(input())
n=int(input())
for i in range(0,n):
    w,h=map(int,input().split())
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w==h:
        print("ACCEPTED")
    elif w>1 or h>l:
        print("CROP IT")