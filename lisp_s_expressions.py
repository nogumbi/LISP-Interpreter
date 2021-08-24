import re
import lisp_parser as lp

def cons(expression):
    """
    cons
    Is used to compose larger s-expressions from smaller expressions.
    (cons a b), expects b to be a list and returns a new list with a as the
    first element followed by all the elements of b
    :param string
    :return: string
    """
    
    s_expr = expression.split(" ")
    remove_chars = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in s_expr if "cons" not in _]
    final_ans = tuple([x for x in remove_chars if x])
    return str(final_ans).replace("'", '').replace(',', '')


def car(expression):

    if(expression[-1] == ")" and expression[-2] == ")" and 
    expression[-3] == ")"):
        check = False
        count = 0

        for char in expression:
            if(char == "'"): check = True
            if(char == " " and check == True): count+=1
            if(char == ")"): break


        s_expr = expression.split(" ")
        remove_chars = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in s_expr if "car" not in _]
        remove_chars = remove_chars[1:]
        
        i = 0
        ret_str = ""
        while i < count:
            ret_str += (" " + remove_chars[i])
            i+=1
        ret_str = "(" + ret_str[1:]
        ret_str += ")"

        return ret_str

    else:
        expression = expression.replace("car '", "")
        ret_str = ""
        for char in expression:
            if(char != " "):
                ret_str += char
            else: break
        return ret_str


def cdr(expression):
    """
    cdr
    Is used to get everything but the first element
    :param s_expression
    :return: a string
    """
    
    s_expr = expression.split(" ")
    remove_chars = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in s_expr if "cdr" not in _]
    final_ans = tuple([x for x in remove_chars[1:] if x])

    if len(final_ans) > 0:
        return str(final_ans).replace("'", '').replace(',', '')
    return "()"
