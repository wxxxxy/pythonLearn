#装饰器
import functools

def dec(text):
	def log(func):
		@functools.wraps(func)
		def warpper(*args, **kw):
			print('begin call %s():' % func.__name__)
			print('%s' % text)
			func(*args, **kw)
			print('end call %s().' % func.__name__)
		return warpper
	if isinstance(text, str):
		return log
	else:
		f=text
		text=''
		return log(f)

@dec
def hello():
	print('Hello,world!')

@dec('execute')
def text_hello():
	print('Hello,world!')
