import unittest
import lisp

class MyTestCase(unittest.TestCase):

    def testSolver(self):
        self.assertEqual( lisp.solver("(+ 10 10 )"), 20)


    """

    def testSolverCond1(self):
        self.assertEqual( lisp.solver("(cond ( (eq 10 20) 'a) ((eq 2 20) 'b) ('t 'c))"), "'c")


    def testSolverCond2(self):
        self.assertEqual( lisp.solver("(cond ( (eq 'a 'b) 'first) ( 't 'last))"), "'last")

    def testSolver(self):
        self.assertEqual( lisp.solver("(eq 10 10 )"), "'t")


      

    def test_eq1(self):
        self.assertEqual('\'t', lisp.eq("( eq 10 10 )"))

    def test_eq2(self):
        self.assertEqual("()", lisp.eq("( eq 10 20 )"))

    def test_atom1(self):
        self.assertEqual('\'t', lisp.atom("( atom '10 )"))

    def test_atom2(self):
        self.assertEqual('()', lisp.atom("( atom '(sma 10 10 )"))


    def test_cond1(self):
        self.assertEqual('\'c', lisp.cond("( cond (  ( () 'a )  ( ()  'b) )  ( 't 'c) )"))

    def test_cond2(self):
        self.assertEqual('\'is_ten', lisp.cond("( cond ( 't 'is_ten))"))

    def test_cond3(self):
        self.assertEqual('\'last', lisp.cond("( cond ( () 'first) ( 't 'last))	"))

    def test_cond4(self):
        self.assertEqual('()', lisp.cond("( cond ( () 'first) ( () 'last))	"))

    #Test Extract Brackets

    def testExtract_brackets1(self):
        self.assertEqual("()", lisp.Extract_Bracket("(car this that)"))

    def testExtract_brackets2(self):
        self.assertEqual("(())", lisp.Extract_Bracket("(car (that again))"))

    def testExtract_brackets3(self):
        self.assertEqual("(()())", lisp.Extract_Bracket("(car (this) (that))"))

    def testExtract_brackets4(self):
        self.assertEqual("((()))", lisp.Extract_Bracket("(car (this (that)))"))

    def testExtract_brackets4(self):
        self.assertEqual("()()()", lisp.Extract_Bracket("(car) (this) (that)"))


    #Test Bracket correcteness

    def test_correct1(self):
        self.assertEqual(True, lisp.correct_brackets("()"))

    def test_correct2(self):
        self.assertEqual(True, lisp.correct_brackets("(())()"))

    def test_correct3(self):
        self.assertEqual(True, lisp.correct_brackets("((()()))"))

    def test_incorrect1(self):
        self.assertEqual(False, lisp.correct_brackets("()("))

    def test_incorrect2(self):
        self.assertEqual(False, lisp.correct_brackets("())"))

    def test_incorrect3(self):
        self.assertEqual(False, lisp.correct_brackets("((()))()))"))

    def test_incorrect4(self):
        self.assertEqual(False, lisp.correct_brackets(")()()()()"))


"""



if __name__ == '__main__':
    unittest.main()