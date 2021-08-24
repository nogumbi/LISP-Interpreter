
def  correct_brackets(bracketsList):

    control = 0
    for bractet in bracketsList:
        if bractet == "(":
            control= control +1
        else:
            control= control - 1
        if control < 0:
            return False
        
    if control == 0:
        return True
    return False


def cond(operation):

    operation = operation.split(" ")
    while len(operation) > 0:
        if "'t" == operation[0]:
            operation.pop(0)
            return operation.pop(0).strip().strip(')')
        operation.pop(0)
    return '()'

def Extract_Bracket(User_input):

    brackets_String = ""
    for bracket in User_input:
        if bracket == "(":
            brackets_String = brackets_String + "("
        
        if bracket == ")":
                brackets_String = brackets_String + ")"
    return brackets_String


def solve(operation):

    operation_tokens = operation.replace("(", "")
    operation_tokens = operation_tokens.replace(")", "").strip()
    operation_tokens = operation_tokens.split()

    math_operations = ["+", "-", "/", "*"]

    print(operation_tokens, "operta")

    if operation_tokens[0] in math_operations:
        return basicMath(operation)
    
    if operation_tokens[0] ==  "eq":
        return eq(operation)

    if operation_tokens[0] ==  "atom":
        return atom(operation)

    if operation_tokens[0] ==  "cond":
        return cond(operation)
    
    return operation

def solver(UserInput):

    if isinstance(UserInput, str):
        UserInput = UserInput.replace("(", " ( ")
        UserInput = UserInput.replace(")", " ) ").strip()
        UserInput = UserInput.split()

    operation = UserInput.pop(0)

    while len(UserInput) > 0 :

        operation = operation + " "

        if UserInput[0] == "(":
            operation = operation + str(solver(UserInput)); 
        elif UserInput[0] == ")":
            operation = operation + UserInput.pop(0)
            return solve(operation)
        else:
            operation = operation + str(UserInput.pop(0))

def eq(operation):

    operation = operation.replace("(", "")
    operation = operation.replace(")", "").strip()
    operation = operation.split()

    if operation[-1] == operation[-2]:
        return "\'t "
    return "() "

def atom(operation):

    operation = operation.replace("(", "")
    operation = operation.replace(")", "").strip()
    operation = operation.split()

    if len(operation) > 2:
        return "()"
    return '\'t'


def basicMath(expression):

    #Changing the expression to a list
    #operator = expression.split("(")


    print("maths called")

    operation_tokens = expression.replace("(", "")
    operation_tokens = operation_tokens.replace(")", "").strip()
    operation_tokens = operation_tokens.split()


    if operation_tokens[1].isdigit():
        x = int(operation_tokens[1])
    else:
        return expression

    if operation_tokens[2].isdigit():
        y = int(operation_tokens[2])
    else:
        return expression
    
    value = operation_tokens[0]

    if value == "+":
        return x + y
    elif value == "-":
        return x - y
    elif value == "/":
        return x/y
    elif value == "*":
        return x*y

