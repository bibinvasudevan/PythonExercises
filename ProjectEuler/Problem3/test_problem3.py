import unittest
from problem3 import largest_pfactor

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_max13195(self):
        self.assertEqual(largest_pfactor(13195), 29)

    def test_max13199(self):
        self.assertEqual(largest_pfactor(13199), 197)

if __name__ == '__main__':
    unittest.main()
