import unittest
import operation_detection

class TestOpDetect(unittest.TestCase):

    def testIsListTrue(self):
        test_string = "(a b)"
        ret_val = operation_detection.isList(test_string)
        self.assertTrue(ret_val)
    
    def testIsListFalse(self):
        test_string = "(+ a b)"
        ret_val = operation_detection.isList(test_string)
        self.assertFalse(ret_val)

    def testIsListEmpty(self):
        test_string = "()"
        ret_val = operation_detection.isList(test_string)
        self.assertTrue(ret_val)

    def testIsMathTrue(self):
        test_string = "(+ a b)"
        ret_val = operation_detection.isMath(test_string)
        self.assertTrue(ret_val)

    def testIsMathFalse(self):
        test_string = "(cons a b)"
        ret_val = operation_detection.isMath(test_string)
        self.assertFalse(ret_val)