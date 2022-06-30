n=input()
c=0
for i in n:
    if i.isdecimal()==False:
        if i.isalnum()==False:
            if i.isspace()==False:
                c+=1
print(c)