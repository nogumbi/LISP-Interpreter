import math

math_ops = ["+", "*", "-", "/"]

def addition(x, y):
    """Sums up the input arguments."""
    return x + y

def subtraction(x, y):
    """Subtracts the input arguments."""
    return x - y
def divide(x, y):
    """Divides the input arguments."""
    return x / y

def multiply(x, y):
    """Multiplies the input arguments."""
    return x * y


def basicMath(expression):

    #Changing the expression to a list
    #operator = expression.split("(")

    internal_expr = expression.split(" ")#[1:-1]
    
    operator = internal_expr[0].split("(")

    num = expression.split(" ")
    last_int = num[2].split(")")

    if num[1].isdigit():
        x = int(num[1])
    else:
        return expression

    if last_int[0].isdigit():
        y = int(last_int[0])
    else:
        return expression
   
    for value in operator:
        if value == "+":
            add = addition(x, y)
            return int(add)
        elif value == "-":
            sub = subtraction(x, y)
            return int(sub)
        elif value == "/":
            div = divide(x, y)
            return int(div)
        elif value == "*":
            mul = multiply(x, y)
            return int(mul)
