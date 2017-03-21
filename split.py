#正则表达式
import re

s = 'a b ,c ;d,e  f'
l = re.split(r'[\s\,\;]+', s)

print(l)