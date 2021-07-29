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
	c=0
	for i in range(1,n+1):
		if(prime(i)):
			c+=1
	if(prime(c)):
		return True
	else:
		return False
n=int(input("Enter a number:"))
if(sp(n)):
		print(n,"is strong prime")
else:
	print(n,"is not a strong prime")