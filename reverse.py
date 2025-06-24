#Enter Python code here and hit the Run button.

def reverse(s):
   b=s.split()
   b.reverse()
   c=" ".join(b)
   print(c)
   return c[::-1]



a="My Name is Jessa"
print(reverse(a))