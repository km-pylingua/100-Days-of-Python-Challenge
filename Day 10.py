def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def calculate(numb1, numb2, symbol, dictionary):
    for key in dictionary:
        if key == symbol:
            return dictionary[key](numb1, numb2)
            break

operations = {
    "+": add, 
    "-": sub, 
    "*": multiply, 
    "/": divide,
}

def calculator():
    number_1 = float(input("What's the first number?: "))
    calculate_continue = True

    while calculate_continue == True:
        for symbol in operations:
            print(symbol)
        chosen_operation = input("Pick an operation: ")
        number_2 = float(input("What's the next number?: "))
        '''alternative: remove calculate function and replace with just
        answer = operations[operation_symbol](number_1, number_2)'''
        answer = calculate(number_1, number_2, chosen_operation, operations)
        print(f"{number_1} {chosen_operation} {number_2} = {answer}")

        cont_or_stop = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if cont_or_stop == 'y':
            number_1 = answer
        else:
            calculate_continued = False
            calculator()

calculator()
            


