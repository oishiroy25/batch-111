

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


a=int(input())
b=int(input())
ch=input()



if ch=='+':
    print(f"Addition is:{add(a,b)}")
elif ch=='-':
    print(sub(a,b))
elif ch=='*':
    print(mul(a,b))
elif ch=='/':
    print(div(a,b))