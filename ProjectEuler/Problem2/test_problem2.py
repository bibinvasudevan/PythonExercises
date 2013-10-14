import unittest
from problem2 import even_fib_sum

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_max10(self):
        self.assertEqual(even_fib_sum(10), 10)

    def test_max20(self):
        self.assertEqual(even_fib_sum(20), 10)

    def test_max50(self):
        self.assertEqual(even_fib_sum(50), 44)
 
    def test_max100(self):
        self.assertEqual(even_fib_sum(100), 44)
 
if __name__ == '__main__':
    unittest.main()
