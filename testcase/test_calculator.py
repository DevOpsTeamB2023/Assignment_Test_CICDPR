import sys
import unittest
from sourcecode.calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_add2(self):
        self.assertEqual(add(3, 3), 6)

if __name__ == '__main__':
    unittest.main()
