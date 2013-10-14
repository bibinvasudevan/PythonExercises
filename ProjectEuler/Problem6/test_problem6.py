import unittest
from problem6 import diff_sumsquare

class TestDSS(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_max10(self):
        self.assertEqual(diff_sumsquare(10), 2640)

    def test_max20(self):
        self.assertEqual(diff_sumsquare(20), 41230)

if __name__ == '__main__':
    unittest.main()
