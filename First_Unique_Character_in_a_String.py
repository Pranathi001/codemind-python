n=input()
for i in n:
    if n.count(i)<2:
        print(n.index(i))
        break
else:
    print("-1")