import unittest
from multiplicar import multiplicar

class TestSuma(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(5,3), 15)
        self.assertEqual(multiplicar(3,5), 15)
        self.assertEqual(multiplicar(-1,1), -1)

if __name__ == '__main__':
    unittest.main()