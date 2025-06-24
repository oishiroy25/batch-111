def func(x):
   prev=0
   cur=1

   for i in range(x):
    print(prev)
    new=cur +prev
    prev=cur
    cur=new


x=int(input())
func(x)
