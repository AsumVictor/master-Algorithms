import unittest
from solution import solution

class CustomTestResult(unittest.TestResult):
    def startTest(self, test):
        super().startTest(test)
        print(f"Running test: {test.shortDescription()}")

    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"✅ Passed: {test.shortDescription()}")
        print('-----------------------------------------------------', end="\n")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"❌ Failed: {test.shortDescription()}")
        print('-----------------------------------------------------', end="\n\n")

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.results = CustomTestResult()

    def run(self, result=None):
        if result is None:
            result = self.results
        super().run(result)

    def test_with_space_and_puntatuation(self):
        '''Testing string ewith word of space and puntations'''
        self.assertEqual(solution('   Hello Geeks . Welcome   to  GeeksforGeeks   .    '), 'Hello Geeks. Welcome to GeeksforGeeks.')
        
    def test_with_space_only(self):
        '''Testing for string with space only'''
        self.assertEqual(solution('   Hello Geeks  Welcome   to       GeeksforGeeks       '), 'Hello Geeks Welcome to GeeksforGeeks')
        
    def test_all_space(self):
        '''Testing for all space of string'''
        self.assertEqual(solution('                                                                                                                    '), '')

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=CustomTestResult))
