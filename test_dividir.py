import unittest
from dividir import dividir

class TestSuma(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(10,2), 5)
        self.assertEqual(dividir(20,4), 5)
        self.assertEqual(dividir(80,0), "Error")

if __name__ == '__main__':
    unittest.main()