#函数参数测试
#默认参数，除必选参数外可以不传，函数会按默认的值进行计算；若需要传入默认参数，要不按顺序传入，
#要不传入时带上参数名称marry='no'
def defaultParam(name, age, city='fuzhou',marry='no'):
	print('name:',name,'age:',age,'city:',city,'marry:',marry)

#可变参数，传入一个list或tuple，长度可变。简化传入参数写法changeParam(1,2,3,4,5)
#或num=(1,2,3,4,5)	changeParam(*num)
def changeParam(*number):
	sum = 0
	for n in number:
		sum = sum + n
	return sum

#关键字参数，**kw为python关键字参数默认写法，接收任意数量的key=value键值对，
#或dic={'city':'fuzhou','marry':'yes'}	keyParams('wxy','24',**dic)
def keyParams(name, age, **kw):
	print('name:',name,'age:',age,'kw:',kw)

#命名关键字参数，用*分隔，如下，出必选参数外，只接收key为city和marry的dict
def nameKeyParams(name, age, *, city, marry):
	print('name:',name, 'age:',age, 'city:',city, 'marry:',marry)

def nameKeyDefaultParams(name, age, *args, city='fuzhou', marry):
	print('name:',name, 'age:',age, 'args:', args, 'city:',city, 'marry:',marry)

def mixParams1(a, b, c=0, *args, **kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
