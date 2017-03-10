#杨辉三角 生成器
def triangles():
	L=[1]
	while True:
		yield L
		L.append(0)
		L=[L[i-1] + L[i] for i in range(len(L))]

def triPrint(maxN):
	n=0
	for t in triangles():
		print(t)
		n=n+1
		if n > maxN:
			break

maxN = int(input('Please entry max Number:'))
triPrint(maxN)
