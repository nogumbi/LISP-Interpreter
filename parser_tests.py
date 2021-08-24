import unittest
import lisp_parser

class TestParser(unittest.TestCase):

    def testParserSingle(self):
        test_string = "(a)"
        return_val = lisp_parser.break_down(test_string)
        self.assertEqual(return_val, 'a')

    def testParseDeep(self):
        test_string = "(a (b (c (d))))"
        ret_val =  lisp_parser.break_down(test_string)
        self.assertN(ret_val, "a b c d")

    def testExpressions(self):
        test_string = "(quote a (cons a (c d)))"
        ret_val = lisp_parser.break_down(test_string)
        self.assertNotEqual(ret_val, "quote a cons a c d")