"""
    This module handles the detection of different operations
    given in the s expressions 
"""

import basic_math as math
import lisp_s_expressions as xprs
import cond_eq_atom as condition

symbols_ls = ["+", "*", "-", "/", "cons", "car", "cdr", "cond", "eq", "atom"]
math_ops = ["+", "*", "-", "/"]
s_xprs = ["cons", "car", "cdr"]
cond = ["cond", "eq", "atom"]


def isList(expression):
    if(expression[0] == "(" and expression[-1] == ")"):
        internal_expr = expression[1:-1]
        for symbol in symbols_ls:
            if(symbol in internal_expr):
                return False
        return True

def isMath(expression):
    internal_expr = expression
    for symbol in math_ops:
        if(symbol in internal_expr):
            return True
    return False

def isSxprs(expression):
    internal_expr = expression
    for symbol in s_xprs:
        if(symbol in internal_expr):
            return True
    return False

def isCond(expression):
    internal_xpr = expression
    for symbol in cond:
        if(symbol in internal_xpr):
            return True
    return False


def detect_operation(expression):
    
    if(isMath(expression)):
        expression = expression.replace(")", "")
        expression = "(" + expression + ")"
        return str(math.basicMath(expression))

    elif(isSxprs(expression)):
        if(s_xprs[0] in expression): return xprs.cons(expression)
        elif(s_xprs[1] in expression): return xprs.car(expression)
        elif(s_xprs[2] in expression): return xprs.cdr(expression)

        return expression
    elif(isCond(expression)):
        
        """
        Someone please finish this, same idea as above
        import cond_eq_atom.py
        """
        if(cond[0] in expression): return condition.cond(expression)
        elif(cond[1] in expression): return condition.eq(expression)
        elif(cond[2] in expression): return condition.atom(expression)

        return expression #Don't forget to remove thsi

    else: return expression

def main():
    #for testing only
    print(detect_operation("(* (+ 3 2) (- 10 (/ 6 3)))"))

if __name__ == "__main__":
    main()
