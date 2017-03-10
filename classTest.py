#类
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, *like):
		super(Student, self).__init__()
		self.__name = name
		self.__age = age
		self.__like = like

	def print_info(self):
		print(self.__name,self.__age,self.__like)

	def get_name(self):
		return self.__name
	def get_age(self):
		return self.__age
	def get_like(self):
		return self.__like

	def set_name(self, name):
		self.__name = name
	def set_age(self, age):
		self.__age = age
	def set_like(self, *like):
		self.__like = like

