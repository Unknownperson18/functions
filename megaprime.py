def dp(n):
	while(n):
		r=n%10
		if(r!=2 and r!=3 and r!=5 and r!=7):
			return False
		n=n//10
	return True
def prime(n):
	if (n==1):
		return False
	for i in range(2,n//2+1):
		if(n%i==0):
			return False
	return True
def mp(n):
	return dp(n) and prime(n)
n=int(input("Enter a number:"))
if(mp(n)):
	print(n,"is mega prime number")
else:
	print(n,"is not a mega prime")