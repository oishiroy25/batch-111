 

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


while True:

           a=int(input("Enter first number: "))
           b=int(input("Enter second number: "))
           if(a==0 or b==0):
              break
           ch=input("Enter operation(+,-,*,/): ")

           if ch=='+':
            print(f"Addition is:{add(a,b)}")
           elif ch=='-':
            print(f"Subtraction is:{sub(a,b)}")
           elif ch=='*':
            print(f"Multiplication is:{mul(a,b)}")
           elif ch=='/':
            print(f"Divided by is:{div(a,b)}")