def func(x,y):
    if(x*y<=1000):
        return x*y
    else:
        return x+y
         
x=int(input())
y=int(input())
print(func(x,y))