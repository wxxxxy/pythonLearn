#错误处理
import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		x = bar('0')
		print(x)
	except Exception as e:
		print('Error', e)
#		logging.exception(e)
#		raise
	finally:
		print('finally.')

main()
print('END')