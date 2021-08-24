import operation_detection as od

print('Welcome to LISP interpreter')

def parse_input(str_expr, index):

    expr_copy = str_expr
    final_expression = []

    while(index < len(expr_copy)):
        if(expr_copy[index] != "("):

            if(expr_copy[index] == ")" and (index < len(expr_copy) - 1) and 
            expr_copy[index + 1] == ")" 
            and expr_copy[index + 1] == len(expr_copy) -1): break

            final_expression.append(expr_copy[index])

            if(expr_copy[index] == ")"):
                #print(final_expression)
                return(final_expression, index+1)

        elif(expr_copy[index] == "("):
            ret_val = parse_input(expr_copy, index+1)
            final_expression.append(ret_val[0])
            index = ret_val[1] - 1

        index+=1

    return (final_expression, index)
            
def build_output(str_expr):

    evaluated_output = ""
    new_char = ""
    
    for char in str_expr:
        if(isinstance(char, list)):
            new_char = build_output(char)
            evaluated_output += new_char

        else: evaluated_output += str(char)

    evaluated_output = od.detect_operation(evaluated_output)

    return evaluated_output

def await_input():

    in_str = input("::")

    if(in_str[0] == "'"):
        return in_str[1:]

    elif (in_str[:6] == "(quote"):
        return in_str[7:-1]

    elif in_str == "exit": return "exit"

    else:
        ret_val = parse_input(in_str, 0)
        return build_output(ret_val[0])

def main():
    returned_val = await_input()
    if(returned_val == "exit"):
        exit
    else:
        print(returned_val)
        main()

if __name__ == "__main__":
    main()