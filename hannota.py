def hannota(n,a,b,c):
	if(n == 1):
		print(a,'->',c)
	else:
		hannota(n-1,a,c,b)
		hannota(1,a,b,c)
		hannota(n-1,b,a,c)
