import unittest
from StringCalculator import add
class TestStringCalculator(unittest.TestCase):
        
        def test_expectZeroForEmptyInput(self):
                self.assertEqual(add(""), 0)
                
        def test_expectZeroForSingleZero(self):
                self.assertEqual(add("0"), 0)
                
        # def expectSumForTwoNumberst(self):
        #         self.assertEqual(add("1,2"), 3)
                
        # def ignoreNumbersGreaterThan1000(self):
        #         self.assertEqual(add("1,1001"), 1)
                
        # def expectSumWithCustomDelimiter(self):
        #         self.assertEqual(add("//;\n1;2"), 3)
                
        # def expectSumWithNewlineDelimiter(self):
        #         self.assertEqual(add("1\n2,3"),6);
        




if __name__ == '__main__':
    unittest.main()


