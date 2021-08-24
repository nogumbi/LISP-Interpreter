def cond(operation):

    operation = operation.split(" ")
    while len(operation) > 0:
        if "'t" == operation[0]:
            operation.pop(0)
            return operation.pop(0).strip().strip(')')
        operation.pop(0)
    return '()'


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