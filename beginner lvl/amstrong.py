n = int(input("Enter a number: "))  
s = 0  
t = n  
  
while t > 0:  
   d = t % 10  
   s += d ** 3  
   t  
  
if n == s:  
   print(n,"is an Armstrong number")  
else:  
   print(n,"is not an Armstrong number")  
