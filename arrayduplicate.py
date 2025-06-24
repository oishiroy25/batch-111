a=[5,5,7,3,3,4,4,4,2,9]
new=[]
for i in a:
    if i not in new:
        new.append(i)

print(new)