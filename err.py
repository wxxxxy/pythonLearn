#单步调试
#n-单步执行
#c-往下执行
#p 变量名-查看变量
#l-查看代码
#q-退出pdb模式
import pdb

s = '0'
n = int(s)
a = n*2
b = n+2
pdb.set_trace()
print(10/n)