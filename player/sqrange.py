import math

a,x =input().split()
a=int(a)
x=int(x)
print(type(i))
count=0
for q in range(a,x):
  if int(math.sqrt(q))**2==q:
      count=count+1
print(count) 
