import unittest
from restar import restar

class TestSuma(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(5,3), 2)
        self.assertEqual(restar(3,5), -2)
        self.assertEqual(restar(-1,1), -2)

if __name__ == '__main__':
    unittest.main()