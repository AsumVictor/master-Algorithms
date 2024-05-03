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
        
    def test_test1(self):
        ''' containing only ABB should return 4'''
        self.assertEqual(solution('ABAB',2), 4)
        
    def test_test2(self):
        ''' containing only AABABBA should return 4'''
        self.assertEqual(solution('AABABBA',1), 4)
        
    def test_test3(self):
        ''' Countaing multiple letters'''
        self.assertEqual(solution('ABCBBXBBABCCABABAAB',2), 7)
        
    def test_test4(self):
        ''' Countaing single letter words'''
        self.assertEqual(solution('AAAAAAAAAAAAAAAAAAAAA',7), 21)
    

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=CustomTestResult))
     