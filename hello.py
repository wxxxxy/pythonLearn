
print('输入输出测试:')
name=input("Please entry your name:")
num=int(input('Please entry a number:'))
print("hello"+name)
print('中文测试')

print('Hello,%s'% 'world')
print('Hello,%s'% name)
print('your number is %2d'% num)
print('your number is %02d'% num)
print('your number is %.2f'% num)


print('乘法表1')
x=1
y=1
while x<10:
	y=1
	while y<=x:
		print(x,'*',y,'=',x*y)
		y=y+1
	print('\t')
	x=x+1


print('乘法表2')
xx=(1,2,3,4,5,6,7,8,9)
y=1
for x in xx:
	y=1
	while y<=x:
		print(y,'*',x,'=',x*y)
		y=y+1
	print('\t')

print('dict set测试')

d = {'wxy':1, 'ydl':2, 'xln':3}
print(d['wxy'])
print(d['ydl'],'\n')
print(d['xln'])
print(d)
d['ydl'] = 7
print(d)
d['sj'] = 4
print(d)

