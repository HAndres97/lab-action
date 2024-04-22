import unittest
from suma import sumar

class TestSuma(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5,3), 8)
        self.assertEqual(sumar(3,5), 8)
        self.assertEqual(sumar(-1,1), 0)
        self.assertEqual(sumar(-1,-1), -2)
        self.assertEqual(sumar(1,0), 1)

if __name__ == '__main__':
    unittest.main()