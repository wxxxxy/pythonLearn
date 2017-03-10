#闭包，引用了循环变量，导致函数参数的值变化
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

#闭包，用一个新函数的参数绑定循环变量当前的值，时函数参数的值不变
def count_():
	fs=[]
	for i in range(1, 4):
		def f(x):
			return lambda x: x*x
		fs.append(f(i))
	return fs

