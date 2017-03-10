def every_one_pay(pub, pri_wang, pri_liu):
	sum = 0
	for k,v in pub.items():
		sum = sum + v
		print('%s:%f' % (k, v))
	everyone = sum/3
	print('sum:%f, every_one_pay:%f' % (sum, everyone))
	print('Wang private items:', pri_wang)
	print('Liu private items:', pri_liu)

{'doufupi': 14.66, 'sezi': 8.7, 'lianou': 3.64, 'xilanhua': 2.25, 'jinzhengu': 2.18, 'niurou': 22.8, 'baicai': 4.96, 'luobo': 1.1, 'yuzi': 5.78, 'yuni': 19.9,'tudou': 2.18, 'yuwan': 7.9, 'yumi': 4.24}

 {'jirou1': 7.88, 'cu': 11.5, 'suannai': 17.9, 'jirou2': 8.15}

 {'niunai': 10.8, 'mantou': 6}