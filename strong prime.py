#strong prime
from math import *
def prime(n):
	if (n==1):
		return False
	for i in range(2,isqrt(n)+1):
		if (n%i==0):
			return False
	return True
def sp(n):
	c=1
	for i in range(3,n+1,2):
		if(prime(i)):
			c+=1
	if(prime(c) and prime(n)):
		return True
	else:
		return False
#strong prime
n=int(input("Enter a number:"))
if(sp(n)):
		print(n,"is strong prime")
else:
	print(n,"is not a strong prime")


#print strong prime in certain range 
a,b=map(int,input("Enter range:").split())
#how many strong primes in certain range
d=0
for i in range(a,b+1):
	if(sp(i)):
		print("strong prime:",i)
		d+=1
print("Total strong primes in the range of ",a,"-",b,"is:",d)
	