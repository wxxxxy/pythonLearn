#单元测试->mydict
import unittest

from mydict import Dict

class TestDict(self):

	def tet_init(self):
		d = Dict(a=1,b='wxy')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'wxy')
		self.assertTrue(isinstance(d, dict))
