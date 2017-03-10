#从3开始的奇数序列生成器
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

#筛选函数，删去序列中n和n的倍数
def _not_divisible(n):
	return lambda x: x % n > 0

#生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

for n in primes():
	if n < 1000:
		print(n)
	else:
		break