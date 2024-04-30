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
        '''Testing for Mixed Binary Numbers'''
        self.assertEqual(solution([1,0,1,1,0,1],2), 6)
        
    def test_binary_1(self):
        '''Testing for only 1 Binary Numbers with 1'''
        self.assertEqual(solution([1,1,1,1,1,1],1), 6)
        
    def test_binary_1_2(self):
        '''Testing for only 1 Binary Numbers'''
        self.assertEqual(solution([1,1,1,1,1,1],4), 3)
        
    def test_binary_0(self):
        '''Testing for only 0 Binary Numbers with 0'''
        self.assertEqual(solution([0,0,0,0,0],0), 15)
        
    def test_binary_0_2(self):
        '''Testing for only 0 Binary Numbers'''
        self.assertEqual(solution([0,0,0,0,0],2), 0)
        
    def test_empty_binary(self):
        '''Testing for empty Binary Numbers'''
        self.assertEqual(solution([], 0), 0)
        
if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=CustomTestResult))
