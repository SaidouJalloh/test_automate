import unittest

class SimpleTest(unittest.TestCase):
    def test_addition(self):
        """Test que l'addition fonctionne correctement"""
        self.assertEqual(1 + 1, 2)
    
    def test_subtraction(self):
        """Test que la soustraction fonctionne correctement"""
        self.assertEqual(3 - 1, 2)
    
    def test_multiplication(self):
        """Test que la multiplication fonctionne correctement"""
        self.assertEqual(2 * 3, 6)
    
    def test_division(self):
        """Test que la division fonctionne correctement"""
        self.assertEqual(6 / 2, 3)

if __name__ == '__main__':
    unittest.main()