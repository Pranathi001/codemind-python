n=int(input())
for i in range(0,n):
    a=input()
    flag=0
    for j in a:
        if j.isdigit()==True:
            flag+=1
        else:
            print("False")
            break
    if flag==len(a):
        print("True")