#单元测试->mydict
#运行命令 python -m unittest <filename>
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...\n')

	def test_init(self):
		print('test_init...')
		d = Dict(a=1,b='wxy')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'wxy')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		print('test_key...')
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		print('test_attr...')
		d = Dict()
		d.key = 'value'
		self.assertTrue("key" in d)
		self.assertEqual(d['key'], 'value')

	def test_keyerror(self):
		print('test_keyerror...')
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		print('test_attrerror...')
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
