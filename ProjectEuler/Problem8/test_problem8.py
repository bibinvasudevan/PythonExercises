import unittest
from problem8 import max_pro5digit

class TestDSS(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_p5d1(self):
        self.assertEqual(max_pro5digit('787878765654343212109098686464'), 25088)

    def test_p5d2(self):
        self.assertEqual(max_pro5digit('9798748648759461809319804719864'), 31752)

if __name__ == '__main__':
    unittest.main()
