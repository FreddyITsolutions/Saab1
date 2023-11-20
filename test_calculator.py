import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(4, 2), 2)

if __name__ == '__main__':
    unittest.main()