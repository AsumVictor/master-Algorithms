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

    def test_mixed_binary(self):
        '''Testing for case 1'''
        self.assertEqual(solution('AB+CD-*'), '*+AB-CD')
        
    def test_binary_1(self):
        '''Testing for case 2'''
        self.assertEqual(solution('ABC/-AK/L-*', '*-A/BC-/AKL'))
    
if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=CustomTestResult))
