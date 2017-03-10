#求一元二次方程解
import math

def qua(a, b, c):
	if(a==0):
		x1=x2=-c/b
		return x1,x2
	else:
		temp=b*b-4*a*c
		print(temp)
		if(temp<0):
			return None
		else:
			num=math.sqrt(temp)
			x1=num/2*a-(b/a)
			x2=-num/2*a-(b/a)
			return x1,x2