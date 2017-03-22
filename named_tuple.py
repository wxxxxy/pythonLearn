#namedtple命名元组的使用
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

Circle = namedtuple('Circle', ['x','y','r'])