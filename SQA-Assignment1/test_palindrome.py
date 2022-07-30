import unittest
import palindrome

class TestPalindrome(unittest.TestCase):
    
    def test_PalindromTrue(self):
        self.assertEqual(palindrome.IsPalindrome('noon'), True)
        self.assertEqual(palindrome.IsPalindrome('kayak'), True)

    def test_PalindromeFalse(self):
        self.assertEqual(palindrome.IsPalindrome('aroma'), False)

    '''#to check whether program fails
    #def test_checkFAIL(self):
        #self.assertEquals(palindrome.IsPalindrome('apple'), True)'''

if __name__ == '__main__':
    unittest.main()


