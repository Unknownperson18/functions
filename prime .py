#strong prime
from math import *
def prime(n):
	if (n==1):
		return False
	for i in range(2,isqrt(n)+1):
		if (n%i==0):
			return False
	return True
n=int(input("Enter number:"))
if(prime(n)):
	print("prime number")
else:
	print("Not  a prime number")
	