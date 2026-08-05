from multiprocessing import Value

#function to convert digits into int objetcs
def convert_numbers(operation_list):
    for i, element in enumerate(operation_list):
        try:
            operation_list[i] = int(element)
        except ValueError:
            pass
    return operation_list

def answer(question):
    #detect if the question is non-mathematical
    if not any(char.isdigit() for char in question):
        raise ValueError("syntax error")
    elif question.endswith("?") == False:
        raise ValueError("syntax error")
    
    #remove "What is" and "?":
    operation = question.replace("What is ","")
    operation = operation.replace("?","")
    #clean operators
    operation = operation.replace("multiplied by", "multipliedby")
    operation = operation.replace("divided by", "dividedby")

    operation_list = convert_numbers(operation.split())
    operators =  ["plus", "minus", "multipliedby", "dividedby"]

    #check for unknown operators in the operation
    for i in range(len(operation_list)):
        if str(operation_list[i]).isalpha() and str(operation_list[i]) not in operators:
            raise ValueError("unknown operation")
    
    #check that the operation ends with a number
    if isinstance(operation_list[-1], str):
        raise ValueError("syntax error")

    #solve the operation
    while len(operation_list) != 1:
        try:
            sub_op = operation_list[:3] #obtain a sub-operation

            if sub_op[1] == operators[0]:
                sub_result = sub_op[0] + sub_op[2]
            elif sub_op[1] == operators[1]:
                sub_result = sub_op[0] - sub_op[2]
            elif sub_op[1] == operators[2]:
                sub_result = sub_op[0] * sub_op[2]
            elif sub_op[1] == operators[3]:
                sub_result = sub_op[0] / sub_op[2]
            else:
                raise ValueError("syntax error") #in case there isn't an operator between 1st and last element

            operation_list = operation_list[3:] #remove the first 3 elements that have just been solved
            operation_list.insert(0, sub_result) #insert the result of the sub-operation

        except (ValueError, TypeError): #in case something else didn't work
            raise ValueError("syntax error")
    
    return operation_list[0]


