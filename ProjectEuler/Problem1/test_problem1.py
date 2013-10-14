import unittest
from problem1 import sum_multiple35

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_max10(self):
        self.assertEqual(sum_multiple35(10), 23)

    def test_max100(self):
        self.assertEqual(sum_multiple35(100), 2318)

    def test_max1000(self):
        self.assertEqual(sum_multiple35(1000), 233168)
  
if __name__ == '__main__':
    unittest.main()
