#断言
def foo(s):
	n=int(s)
	assert n != 0, 'n is zero!'
	return 10/n

def main():
	a = foo('0')
	print(a)

main()