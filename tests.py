from hw0 import *
import unittest
class TestMethods(unittest.TestCase):
 def test_my_rotate(self):
  self.assertEqual(my_rotate(['a', 'b', 'c']), ['b','c','a'])
 def test_my_rotate_n(self):
  self.assertEqual(my_rotate_n(3, ['a', 'b', 'c', 'd']), ['d','a','b','c'])
 def test_first_sat(self):
  self.assertEqual(first_sat([1, 4, 3, 5], [2, 5, 1, 4], (lambda x, y: x > y)),
[3,1])
 def test_my_remove(self):
  self.assertEqual(my_remove('b', ['a', 'b', 'c', 'd']), ['a','c','d'])
  self.assertEqual(my_remove('b', [['a', 'b'], 'b', ['c','b','d','e','a'], ['b'],
['a'], 'c']), [['a'], ['c', 'd', 'e', 'a'], [], ['a'], 'c'])
 def test_palindromep(self):
  self.assertTrue(palindromep(['b', 'c', 'c', 'b']))
  self.assertTrue(palindromep(['c', 'a', 'c']))
  self.assertFalse(palindromep(['a', 'b', 'c']))
  self.assertTrue(palindromep(['a', ['b', 'a', 'f'], 'l', ['b', 'a', 'f'], 'a']))
  self.assertFalse(palindromep(['a', ['b', 'a', 'f'], 'l', ['f', 'a', 'b'], 'a']))

if __name__ == '__main__':
 unittest.main(verbosity=2)

