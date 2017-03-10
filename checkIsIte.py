#判断是否为迭代对象
from collections import Iterable

def checkIsIterable(object):
	return isinstance(object, Iterable)