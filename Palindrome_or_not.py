n=input()
n=n.casefold()
r=reversed(n)
if list(n)==list(r):
    print(True)
else:
    print(False)