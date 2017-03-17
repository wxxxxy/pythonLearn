import pdb
import json
import pickle
#函数功能：传入文件地址，传出文件信息
def read_file(address, type='str'):
	try:
		if type=='str':
			f=open(address, 'r', encoding='utf-8',errors='ignore')
			s=f.readlines()
			for line in s:
				print(line.strip())
		if type=='json':
			f=open(address, 'r', encoding='utf-8',errors='ignore')
			print(json.load(f))
		if type=='pickle':
			f=open(address, 'rb')
			print(pickle.load(f))
	except IOError as e:
		raise e
	finally:
		if f:
			f.close()

#函数功能：传入文件地址，内容，保存文件成功返回1，反则返回-1
def write_file(address, type='str', *args, **kw):
	try:
		if type=='str':
			f=open(address, 'w', encoding='utf-8')
			s1=str(args)
			s2=str(kw)
			f.write(s1+s2)
		if type=='json':
			f=open(address, 'w', encoding='utf-8')
			#pdb.set_trace()
			kw['attribute']=args
			json.dump(kw, f)
		if type=='pickle':
			f=open(address, 'wb')
			#pdb.set_trace()
			kw['attribute']=args
			b1=pickle.dump(kw, f)
	except IOError as e:
		print(-1)
	else:
		print(1)
	finally:
		if f:
			f.close()


	
	