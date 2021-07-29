#DISARIUM NUMBER
from math import *
def l(n):#finding length
	return int(log10(n)+1)
def d_s(n):#Finding sun
	s=0
	while n:
		r=n%10
		s=s+r **l(n)
		n//=10
	return s#sum 
def dis_num(n):#disarium number
	if(d_s(n)==n):
		return True
	else:
		return False
n=int(input("Enter number"))
if(dis_num(n)):
	print(n,"is Disarium Number")
else:
	print(n,"is not a disarium number")

#DISARIUM NUMBERS IN A CERTAIN RANGE
a,b=map(int,input("Enter range:").split())
for i in range(a,b+1):
	if(dis_num(i)):
		print(i,end=" ")