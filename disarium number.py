#DISARIUM NUMBER
from math import *
def l(n):#finding length
	return int(log10(n)+1)
def d_s(n):#disarium number
	s=0
	while n:
		r=n%10
		s=s+r **l(n)
		n//=10
	return s#sum 
n=int(input("Enter number:"))
if(d_s(n)==n):
		print(n,"Disarium number")
else:
		print(n,"is not disariun number")
		