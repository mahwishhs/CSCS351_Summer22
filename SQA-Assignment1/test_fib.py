import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    msg = "Input to fibonacci sequence must be a non-negative integer"

    def test_fib2(self):
        self.assertEqual(fibonacci.fib(2), 1)

    def test_fib14(self):
        self.assertEqual(fibonacci.fib(14),377)
    
    def test_negativeNum(self):
        self.assertEqual(fibonacci.fib(-7), "Input must be a non-negative number")

    '''def test_FailTest(self):
        self.assertEqual(fibonacci.fib(0), 1)'''

if __name__ == '__main__':
    unittest.main()
    

