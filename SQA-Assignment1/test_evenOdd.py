import unittest
import evenOdd

class TestNumEvenOdd(unittest.TestCase):
    
    def test_isEven(self):
        self.assertEqual(evenOdd.isEvenOdd(8), "The number is Even!")

    def test_isOdd(self):
        self.assertEqual(evenOdd.isEvenOdd(23), "The number is Odd!")

    '''#Check whether program fails
    #def test_CheckforFail(self):
        #self.assertEqual(evenOdd.isEvenOdd(26), "The number is Odd!")'''

if __name__ == '__main__':
    unittest.main()


