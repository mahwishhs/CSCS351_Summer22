import unittest

# import your test modules
import test_prime
import test_palindrome
import test_leapyear
import test_fib
import test_evenOdd


# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_prime))
suite.addTests(loader.loadTestsFromModule(test_palindrome))
suite.addTests(loader.loadTestsFromModule(test_leapyear))
suite.addTests(loader.loadTestsFromModule(test_fib))
suite.addTests(loader.loadTestsFromModule(test_evenOdd))


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=5)
result = runner.run(suite)



