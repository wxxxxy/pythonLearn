import operator

def is_palindrome(n):
	st = str(n)
	ts = st[::-1]
	return operator.eq(st,ts)

output = filter(is_palindrome, range(1, 1000))
print(list(output))