import unittest
import primeNum

class TestPrimeNumbers(unittest.TestCase):

    def test_checkPrime(self):
        self.assertEqual(primeNum.isPrimeNum(3), True)   

    def test_checkPrime2(self):
        self.assertTrue(primeNum.isPrimeNum(23))         
        self.assertFalse(primeNum.isPrimeNum(15))        

    def test_checkPrime3(self):
        # Check that providing a string input produces an error
        with self.assertRaises(TypeError):
            primeNum.isPrimeNum('1')

if __name__ == '__main__':
    unittest.main()

