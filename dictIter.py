#迭代（Iteration）
def iterDict(**kw):
	print(kw,'\n')

	print('iter the key:')
	for key in kw:
		print(key)

	print('iter the value:')
	for value in kw.values():
		print(value)

	print('iter the k,v:')
	for k,v in kw.items():
		print(k,v)

#Python内置的enumerate函数可以把一个list变成索引-元素对
#，这样就可以在for循环中同时迭代索引和元素本身：
#for i, value in enumerate(['A','B','C'])
	