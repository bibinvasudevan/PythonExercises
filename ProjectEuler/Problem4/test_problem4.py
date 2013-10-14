import unittest
from problem4 import largest_palindrom

class TestLP(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_lp2(self):
        self.assertEqual(largest_palindrom(10,99), '9009')

    def test_lp3(self):
        self.assertEqual(largest_palindrom(100,999), '906609')

if __name__ == '__main__':
    unittest.main()
