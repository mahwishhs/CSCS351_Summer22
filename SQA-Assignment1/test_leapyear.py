import unittest
import leapyear

class TestLeapYear(unittest.TestCase):

    def test_isLeapYear1(self):
        self.assertEqual(leapyear.isLeapYear(2024), "It is a leap year!")

    def test_isLeapYear2(self):
        self.assertEqual(leapyear.isLeapYear(2032), "It is a leap year!")

    def test_isLeapYear3(self):
        self.assertEqual(leapyear.isLeapYear(1999), "It is not a leap year!!")

    '''#TO CHECK WHETHER PROGRAM FAILS 
    #def test_checkforFail(self):
        #self.assertEqual(leapyear.isLeapYear(1999), "It is a leap year!!")'''

if __name__ == '__main__':
    unittest.main()