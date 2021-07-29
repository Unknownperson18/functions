def eo(n):
	if n%2==0:
		return True
	else:
		return False
a=int(input("Enter a number:"))
if(eo(a)):
	print("Even")
else:
	print("odd")